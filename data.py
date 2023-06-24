import random
from tkinter import *
import tkinter

text_list = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam pulvinar sapien quis consectetur "
             "consequat. Sed at bibendum arcu, vitae gravida magna. Maecenas tempus venenatis nibh, vel interdum mauris"
             " aliquet id. Aenean venenatis ultrices urna, id imperdiet turpis ultrices eu. Vestibulum nec bibendum"
             " neque. Mauris eget massa blandit, ullamcorper lectus vitae, feugiat libero. Etiam feugiat est pretium"
             " lectus hendrerit, eget cursus sem pharetra. Phasellus elementum arcu sapien, eu tristique diam vulputate"
             " vel. Vivamus nec dolor interdum, mattis diam nec, malesuada massa. Donec bibendum ex quis ligula auctor"
             " faucibus. Sed id fringilla turpis, quis sodales mauris. Aenean suscipit tempus sodales.",
             "Nulla euismod ligula sed sapien euismod consectetur. In maximus metus non lacus malesuada sollicitudin. "
             "Suspendisse facilisis ex sem, eu condimentum justo ultricies iaculis. Donec dictum arcu ac dolor "
             "interdum, a varius enim tincidunt. Aliquam erat volutpat. Nunc dignissim urna neque, in faucibus tellus"
             " imperdiet nec. Curabitur vel rhoncus mi. Pellentesque viverra sit amet nisl quis finibus. Nam nec felis"
             " quis lacus euismod pulvinar. Fusce id elit nibh. Phasellus sodales lacus condimentum odio ultricies"
             " aliquet. Aliquam varius, ante vitae faucibus luctus, eros massa mattis justo, in consectetur neque "
             "felis eget mi. Integer cursus ante vitae eleifend finibus. Etiam vehicula sem in justo tincidunt "
             "ullamcorper.",
             "In aliquet ipsum quis augue elementum, et aliquet turpis dapibus. Quisque ac sem sagittis, congue magna"
             " at, cursus metus. Morbi et odio vel magna aliquet gravida lobortis viverra felis. Sed sed neque "
             "ultricies, malesuada mauris in, rhoncus massa. In consequat, nunc a gravida vehicula, est turpis "
             "tincidunt leo, ac commodo sem risus vitae nisl. Mauris facilisis magna eget risus bibendum, "
             "in vestibulum dolor tincidunt. Donec congue posuere libero et cursus. Sed maximus tellus sit amet "
             "gravida viverra."]

window = Tk()
window.title("Speed Test")
window.geometry("800x600")


class SpeedTest:

    def __init__(self):
        self.wordAmount = None
        self.text = None
        self.textLeft = None
        self.textRight = None
        self.currentLetter = None
        self.timer = None
        self.resultLabel = None
        self.resultButton = None
        self.writable = True
        self.passedSeconds = 0
        self.splitPoint = 0

    def reset_text(self):
        self.passedSeconds = 0
        self.text = random.choice(text_list).lower()
        self.textLeft = Label(window, text=self.text[0:self.splitPoint], fg="grey")
        self.textLeft.place(relx=0.5, rely=0.5, anchor=E)
        self.textRight = Label(window, text=self.text[self.splitPoint:])
        self.textRight.place(relx=0.5, rely=0.5, anchor=W)
        self.currentLetter = Label(window, text=self.text[self.splitPoint], fg="grey")
        self.currentLetter.place(relx=0.5, rely=0.6, anchor=N)
        self.timer = Label(window, text="0 Seconds", fg="grey")
        self.timer.place(relx=0.5, rely=0.4, anchor=S)
        window.bind("<Key>", self.pressed_key)

        window.after(60000, self.stop_test)
        window.after(1000, self.add_time)

    def stop_test(self):
        self.writable = False

        #Calculate the number of words written
        self.wordAmount = len(self.textLeft.cget("text").split(" "))

        self.timer.destroy()
        self.currentLetter.destroy()
        self.textRight.destroy()
        self.textLeft.destroy()

        #Setting the result screen
        self.resultLabel = Label(window, text=f"Words per Minute: {self.wordAmount}", fg="black")
        self.resultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.resultButton = Button(window, text="Play Again", command=self.restart)
        self.resultButton.place(relx=0.5, rely=0.6, anchor=CENTER)

    def restart(self):
        self.resultLabel.destroy()
        self.resultButton.destroy()
        self.reset_text()

    def add_time(self):
        self.passedSeconds += 1
        self.timer.configure(text=f"{self.passedSeconds} Seconds")

        if self.writable:
            window.after(1000, self.add_time)

    def pressed_key(self, event):
        try:
            if event.char.lower() == self.textRight.cget("text")[0].lower():
                self.textRight.configure(text=self.textRight.cget("text")[1:])
                self.textLeft.configure(text=self.textLeft.cget("text") + event.char)
                self.currentLetter.configure(text=self.textRight.cget("text")[0])
        except tkinter.TclError:
            pass
