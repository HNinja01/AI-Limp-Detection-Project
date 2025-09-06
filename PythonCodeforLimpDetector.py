def on_on_start():
    basic.show_icon(IconNames.SAD)
ml.on_start(ml.event.limping, on_on_start)

def on_on_start2():
    basic.show_icon(IconNames.YES)
ml.on_start(ml.event.walking, on_on_start2)

def on_on_start3():
    basic.show_icon(IconNames.SURPRISED)
ml.on_start(ml.event.not_moving, on_on_start3)