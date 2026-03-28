def on_gesture_eight_g():
    music.play(music.string_playable("C C5 C C5 C C5 C C5 ", 43),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.EIGHT_G, on_gesture_eight_g)

def on_gesture_tilt_right():
    while input.is_gesture(Gesture.TILT_RIGHT):
        basic.show_leds("""
            . # . . .
            . . # . .
            . . . # .
            . . # . .
            . # . . .
            """)
        basic.pause(100)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.pause(100)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_tilt_left():
    while input.is_gesture(Gesture.TILT_LEFT):
        basic.show_leds("""
            . . . # .
            . . # . .
            . # . . .
            . . # . .

            . . . # .
            """)
        basic.pause(100)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.pause(100)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

my_variable = 0

def on_forever():
    if input.acceleration(Dimension.X) == 0:
        while my_variable == 0:
            basic.show_leds("""
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                """)
            basic.pause(100)
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
            basic.pause(100)
basic.forever(on_forever)

def on_forever2():
    if not (input.is_gesture(Gesture.TILT_LEFT) or input.is_gesture(Gesture.TILT_RIGHT)):
        pass
basic.forever(on_forever2)
