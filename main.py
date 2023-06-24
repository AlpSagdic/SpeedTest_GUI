from data import SpeedTest, window

speed_test = SpeedTest()
speed_test.reset_text()

window.option_add("*Label.Font", "arial 30")
window.option_add("*Button.Font", "arial 30")

window.mainloop()
