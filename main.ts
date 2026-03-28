input.onGesture(Gesture.EightG, function () {
    music.play(music.stringPlayable("C C5 C C5 C C5 C C5 ", 43), music.PlaybackMode.UntilDone)
})
input.onGesture(Gesture.TiltRight, function () {
    while (input.isGesture(Gesture.TiltRight)) {
        basic.showLeds(`
            . # . . .
            . . # . .
            . . . # .
            . . # . .
            . # . . .
            `)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(100)
    }
})
input.onGesture(Gesture.TiltLeft, function () {
    while (input.isGesture(Gesture.TiltLeft)) {
        basic.showLeds(`
            . . . # .
            . . # . .
            . # . . .
            . . # . .
            . . . # .
            `)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(100)
    }
})
basic.forever(function () {
	
})
basic.forever(function () {
    if (!(input.isGesture(Gesture.TiltLeft) || input.isGesture(Gesture.TiltRight))) {
        while (!(input.isGesture(Gesture.TiltLeft) || input.isGesture(Gesture.TiltRight))) {
            basic.showLeds(`
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                `)
            basic.pause(100)
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `)
            basic.pause(100)
        }
    }
})
