from Tkinter import *

class AnimatedFrame(Frame):
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        self.labelx = 100
        self.labely = 100
        self.label = Label(self, text='Look at me!')
        self.label.place(x=self.labelx, y=self.labely)
        self.button = Button(self, text='Start', command=self.start)
        self.button.place(x=100, y=200)
    
    def start(self):
        if self.labelx > 20:
            self.labelx -= 1
            self.labely -= 1
            self.label.place(x=self.labelx, y=self.labely)
            self.update_idletasks()
            self.start()

def test():
    root = Tk()
    f = AnimatedFrame(root, width=300, height=300)
    f.pack()
    root.mainloop()

if __name__ == '__main__':
    test()