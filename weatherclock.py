import time
import machine
import ntptime
import urequests
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN
from connect import connect, isconnected
import weatherclock_assets
import location_config


graphics = PicoGraphics(display=DISPLAY_GALACTIC_UNICORN)
gu = GalacticUnicorn()

# Initialize state variables
brightness = 0.5
sleep_mode = False


WIDTH = gu.WIDTH
HEIGHT = gu.HEIGHT

current_tz = 0 # UTC by default, can be updated via Open Meteo
REFRESH_NTP = 3600
REFRESH_WEATHER = 1200

WEATHER_URL = "http://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%s&current=temperature_2m,apparent_temperature,weather_code&timezone=%s&forecast_days=1"%(
    location_config.LATITUDE,
    location_config.LONGITUDE,
    location_config.TZ_DEF.replace('/','%2F')

)

PENS = [ graphics.create_pen(*color) for color in weatherclock_assets.BASE_COLORS ]


def update_time():
    global last_ntp_update
    print('Updating time')
    try:
        if not isconnected():
            print('Reconnecting')
            connect()
        ntptime.settime()
        last_ntp_update = time.time()
    except (RuntimeError, OSError) as e:
        print('Error fetching time', e)

def update_weather():
    global last_weather_update, current_tz, forecasts
    print('Updating weather')
    try:
        print(WEATHER_URL)
        r = urequests.get(
            WEATHER_URL)
        j = r.json()
        print(j)

        forecasts = [
            (int(j["current"]["time"][-5:-3]),
             j["current"]["temperature_2m"],
             j["current"]["weather_code"],
             j["current"]["apparent_temperature"]
             )
        ]
        print(forecasts)
        current_tz = j["utc_offset_seconds"]
        last_weather_update = time.time()
    except (Exception) as e:
        print('Error getting weather', e)


def get_weather_type(weather_code):
    for weather in weatherclock_assets.WEATHER_TYPES:
        if weather_code in weather[0]:
            return weather
    return None


@micropython.native
def draw_weather(weather_code, frame_parity, offset_x=0, offset_y=0):
    weather_tuple = get_weather_type(weather_code)
    if weather_tuple is None:
        return
    pixels = weather_tuple[1+frame_parity]
    for y in range(11):
        ypos = offset_y + y
        if (ypos >= 0) or (ypos < HEIGHT):
            line = pixels[y]
            for x in range(15):
                xpos = offset_x + x
                if (xpos >= 0 or xpos < WIDTH):
                    pixelvalue = (line >> 4*x) & 0xf
                    if pixelvalue:
                        graphics.set_pen(PENS[pixelvalue])
                        graphics.pixel(xpos, ypos)

@micropython.native
def draw_digit(i, offset_x, offset_y):
    digit = weatherclock_assets.DIGITS3x5[i]
    for y in range(5):
        ypos = offset_y + y
        if (ypos >= 0) or (ypos < HEIGHT):
            line = (digit >> y*3) & 7
            for x in range(3):
                xpos = offset_x + x
                if line & 1:
                    graphics.pixel(xpos, ypos)
                line = (line >> 1)


def char_to_digit(digit_char):
    if type(digit_char) == int:
        return digit_char & 0xf
    try:
        ch = str(digit_char)[0]
        if ch == '-':
            return 0xa
        elif ch == '.':
            return 0xb
        elif ch == '+':
            return 0xe
        return int(ch,16)
    except (Exception):
        return 0xf

def draw_number( num, offset_x, offset_y, from_right=False):
    numstr = str(num)
    x = offset_x
    if from_right:
        x = x + 1 - 4*len(numstr)
    for digit in numstr:
        draw_digit(char_to_digit(digit), x, offset_y)
        x += 4

def draw_forecast(forecast, offset_y):
    graphics.set_pen(PENS[15])
    draw_number('%.0fd'%forecast[1],32,0+offset_y,True)
    draw_weather(forecast[2],parity,38,offset_y)
    draw_number('%.0fd'%forecast[3],32,6+offset_y,True)
    # print(forecast[3])
    # print(forecast[1])


def handle_switch_actions():
    """Handle Galactic Unicorn switches for specific actions."""
    if gu.is_pressed(GalacticUnicorn.SWITCH_A):
        print("SWITCH_A pressed: Updating time")
        update_time()

    if gu.is_pressed(GalacticUnicorn.SWITCH_B):
        print("SWITCH_B pressed: Updating weather")
        update_weather()


# Brightness control and sleep mode functions
def handle_brightness_change():
    global brightness
    if gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_DOWN):
        brightness = max(0.1, brightness - 0.1)
        gu.set_brightness(brightness)
    elif gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_UP):
        brightness = min(1.0, brightness + 0.1)
        gu.set_brightness(brightness)


def handle_sleep_mode():
    global sleep_mode
    if gu.is_pressed(GalacticUnicorn.SWITCH_SLEEP):
        sleep_mode = not sleep_mode
        if sleep_mode:
            graphics.set_pen(PENS[0])
            graphics.clear()
            gu.update(graphics)


graphics.set_pen(PENS[0])
graphics.clear()
graphics.set_pen(PENS[15])
graphics.set_font('display8')
graphics.text("Hello!", 0, 0, scale=.5)
gu.set_brightness(.5)
gu.update(graphics)
connect()

forecasts = None
last_ntp_update = 0
last_weather_update = 0
last_hour = 0
last_second = 0
scrolling_pos = 0
displayed_forecast_index = 0
year, month, day, hour, minute, second, weekday = (0,0,0,0,0,0,0)
is_scrolling = False
cycles = 0

while True:
    handle_brightness_change()
    handle_sleep_mode()
    handle_switch_actions()  # Check for switch presses

    if sleep_mode:
        time.sleep(0.1)
        continue

    now = time.time()
    msecs = time.ticks_ms()
    parity = (msecs // 500) & 1

    if now != last_second:
        if (now - last_ntp_update) > REFRESH_NTP:
            print('Time to update NTP Time')
            update_time()
        if (now - last_weather_update) > REFRESH_WEATHER:
            print('Time to update weather')
            update_weather()

        local_now = now + current_tz
        year, month, day, hour, minute, second, weekday, _ = time.localtime(local_now)

    if minute == 0 and second < 20:
        for x in range(WIDTH):
            graphics.set_pen(graphics.create_pen_hsv(x / WIDTH, 1, .8))
            graphics.line(x, 0, x, HEIGHT)
    else:
        graphics.set_pen(PENS[0])
        graphics.clear()
        graphics.set_pen(PENS[1])  # Change the color of the clock
        draw_number(f"{hour:02}", 0, 0)
        draw_number(f"{minute:02}", 10, 0)
        graphics.set_pen(PENS[2])  # Change the color of the date
        draw_number(f"{day:02}", 0, 6)
        draw_number(f"{month:02}", 10, 6)

        graphics.set_pen(PENS[15])  # Change the color of the time dots
        if parity:
            graphics.pixel(8, 1)
            graphics.pixel(8, 3)

        if forecasts is not None:
            draw_forecast(forecasts[displayed_forecast_index], -scrolling_pos)

    time.sleep(0.1)
    gu.update(graphics)
    cycles += 1
