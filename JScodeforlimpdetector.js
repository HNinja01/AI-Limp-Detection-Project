ml.onStart(ml.event.Limping, function on_on_start() {
    basic.showIcon(IconNames.Sad)
})
ml.onStart(ml.event.Walking, function on_on_start2() {
    basic.showIcon(IconNames.Yes)
})
ml.onStart(ml.event.NotMoving, function on_on_start3() {
    basic.showIcon(IconNames.Surprised)
})