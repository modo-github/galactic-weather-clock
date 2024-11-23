DIGITS3x5 = (
    0o35556, 0o72232, #0,1
    0o71243, 0o34347, #2,3
    0o44755, 0o34717, #4,5
    0o35716, 0o11247, #6,7
    0o35256, 0o34756, #8,9
    0o00700, 0o66000, # a => -, b => .
    0o57500, 0o00252, # c => hour symbol ("h" in French, "u" in Dutch), d => degree sign
    0, 0, # e => +, f => nothing
)

BASE_COLORS = (
    (0x00, 0x00, 0x00), # 0 = BLACK
    (0xff, 0x60, 0x60), # 1 = RED
    (0x60, 0xff, 0x60), # 2 = GREEN
    (0x60, 0x60, 0xff), # 3 = BLUE
    (0xff, 0xff, 0x60), # 4 = YELLOW
    (0xff, 0x60, 0xff), # 5 = MAGENTA
    (0x60, 0xff, 0xff), # 6 = CYAN
    (0xff, 0xa5, 0x00), # 7 = ORANGE
    (0xa0, 0xff, 0xa0), # 8 = GREEN-ISH
    (0xa0, 0xa0, 0xff), # 9 = BLUE-ISH
    (0xff, 0xff, 0xa0), # a = YELLOW-ISH
    (0xff, 0xa0, 0xff), # b = MAGENTA-ISH
    (0xa0, 0xff, 0xff), # c = CYAN-ISH
    (0x80, 0x80, 0x80), # d = GRAY
    (0xcc, 0xcc, 0xcc), # e = OFF-WHITE
    (0xff, 0xff, 0xff), # f = WHITE

)


SNOW = (
    (71, 73, 75, 77, 85, 86),
    # 71, 73, 75 Snow fall: Slight, moderate, and heavy intensity
    # 77: Snow grains
    # 85, 86: Snow showers slight and heavy
    (
        0x000dddd000000,
        0x0dddddddddddd00,
        0xddddddddddddddd,
        0x0ddddddddddddd0,
        0x000000000000000,
        0x000f00000000000,
        0x0f0f0f0000f0f00,
        0x00fff000000f000,
        0x0f0f0f000fffff0,
        0x000f0000000f000,
        0x0000000000f0f00,
    ),
    (
        0x000dddddd000000,
        0x0dddddddddddd00,
        0xddddddddddddddd,
        0x0ddddddddddddd0,
        0x000000000000000,
        0x00f0f0000000000,
        0x000f0000000f000,
        0x0fffff000f0f0f0,
        0x000f000000fff00,
        0x00f0f0000f0f0f0,
        0x00000000000f000,
    ),
)

CLOUDS = (
    (2, 3),
    (
        0x000ddd000000000,
        0x0ddddddd0000000,
        0xdddddddddd00000,
        0x0dddddddd000000,
        0x000000000000000,
        0x000000ee00ee000,
        0x000eeeeeeeeee00,
        0x00eeeeeeeeeeeee,
        0x00eeeeeeeeeeeee,
        0x000eeeeeeeeeee0,
        0x000000000000000,
    ),
    (
        0x0000ddd00000000,
        0x00ddddddd000000,
        0x0dddddddddd0000,
        0x00dddddddd00000,
        0x000000000000000,
        0x00000ee00ee0000,
        0x00eeeeeeeeee000,
        0x0eeeeeeeeeeeee0,
        0x0eeeeeeeeeeeee0,
        0x00eeeeeeeeeee00,
        0x000000000000000,
    ),
)

CLOUDS_LIGHT = (
    (1, ),
    (
        0x000000000077700,
        0x000000000777770,
        0x000000007777777,
        0x000000007777777,
        0x000000007777777,
        0x000000000777770,
        0x000000ee00ee700,
        0x00eeeeeeeeee000,
        0x0eeeeeeeeeeeee0,
        0x00eeeeeeeeeee00,
        0x000000000000000,
    ),
    (
        0x000000000077700,
        0x000000000777770,
        0x000000007777777,
        0x000000007777777,
        0x000000007777777,
        0x000000000777770,
        0x00000ee00ee7700,
        0x0eeeeeeeeee0000,
        0xeeeeeeeeeeeee00,
        0x0eeeeeeeeeee000,
        0x000000000000000,
    ),
)


FOG = (
    ( 45, 48 ),
    (
        0x000000000000000,
        0xeeeeee00eeeeee0,
        0x000000000000000,
        0x0eeeeee00eeeeee,
        0x000000000000000,
        0xeeeeee00eeeeee0,
        0x000000000000000,
        0x0eeeeee00eeeeee,
        0x000000000000000,
        0xeeeeee00eeeeee0,
        0x000000000000000,
    ),
    (
        0x000000000000000,
        0x0eeeeee00eeeeee,
        0x000000000000000,
        0xeeeeee00eeeeee0,
        0x000000000000000,
        0x0eeeeee00eeeeee,
        0x000000000000000,
        0xeeeeee00eeeeee0,
        0x000000000000000,
        0x0eeeeee00eeeeee,
        0x000000000000000,
    ),
)

RAIN = (
    ( 53, 55, 57, 63, 65, 67, 81, 82 ),
    (
        0x000eeeeee000000,
        0x0eeeeeeeeeeee00,
        0xeeeeeeeeeeeeeee,
        0x0eeeeeeeeeeeee0,
        0x000000000000000,
        0x030003000300030,
        0x000300030003000,
        0x030003000900030,
        0x000900030003000,
        0x030003000300090,
        0x000300030003000,
    ),
    (
        0x000eeeeee000000,
        0x0eeeeeeeeeeee00,
        0xeeeeeeeeeeeeeee,
        0x0eeeeeeeeeeeee0,
        0x000000000000000,
        0x000300030003000,
        0x030003000300090,
        0x000900030003000,
        0x030003000300030,
        0x000900030003000,
        0x030003000900030,
    ),
)

RAIN_LIGHT = (
    ( 51, 56, 61, 66, 80 ),
    (
        0x000eeeeee000000,
        0x0eeeeeeeeeeee00,
        0xeeeeeeeeeeeeeee,
        0x0eeeeeeeeeeeee0,
        0x000000000000000,
        0x030000000300000,
        0x000003000000030,
        0x090000000900000,
        0x000009000000090,
        0x030000000300000,
        0x000003000000030,
    ),
    (
        0x000eeeeee000000,
        0x0eeeeeeeeeeee00,
        0xeeeeeeeeeeeeeee,
        0x0eeeeeeeeeeeee0,
        0x000000000000000,
        0x000003000000030,
        0x030000000300000,
        0x000009000000090,
        0x090000000900000,
        0x000003000000030,
        0x030000000300000,
    ),
)

SUN = (
    [0],
    (
        0x000000000000000,
        0x000000000000000,
        0x000000777000000,
        0x000007777700000,
        0x000077777770000,
        0x000077777770000,
        0x000077777770000,
        0x000007777700000,
        0x000000777000000,
        0x000000000000000,
        0x000000000000000,
    ),
    (
        0x000000040000000,
        0x000400000004000,
        0x000040777040000,
        0x000007777700000,
        0x000077777770000,
        0x044077777770440,
        0x000077777770000,
        0x000007777700000,
        0x000040777040000,
        0x000400000004000,
        0x000000040000000,
    ),
)

STORM = (
    [95, 96, 99],
    (
        0x000eeeeee000000,
        0x0eeeeeeeeeeee00,
        0xeeeeeeeeeeeeeee,
        0x0eeeeeeeeeeeee0,
        0x000000000000000,
        0x000000aaa000000,
        0x000000aaa000000,
        0x00000aaa0000000,
        0x00000aaa0000000,
        0x0000000aa000000,
        0x00000000a000000,
    ),
    (
        0x000eeeeee000000,
        0x0eeeeeeeeeeee00,
        0xeeeeeeeeeeeeeee,
        0x0eeeeeeeeeeeee0,
        0x000000000000000,
        0x000000000000000,
        0x000000000000000,
        0x000000000000000,
        0x000000000000000,
        0x000000000000000,
        0x000000000000000,
    ),
)

WEATHER_TYPES = (
    SNOW, CLOUDS, CLOUDS_LIGHT, FOG, RAIN, RAIN_LIGHT, SUN, STORM,
)
