from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.colorchooser import *
from PIL import Image
import os

class paintapp():
    def __init__(self,master):
        self.master = master
        self.old_x = None
        self.old_y = None
        self.size = 1
        self.linecolor = "black"
        self.oldcolor = "black"
        self.eraser = 0
        self.interface_build()
        self.c.bind("<B1-Motion>", self.draw)
        self.c.bind('<ButtonRelease-1>',self.drawstop)
    def interface_build(self):
        """
        self.canvasframe = Frame(self.master, borderwidth=2, relief=GROOVE)
        self.canvasframe.pack(side=LEFT, padx=30, pady=30)
        """
        self.sizeinfo = Label(self.master, text="Pencil/Eraser size :")
        self.sizeinfo.pack()
        self.size = Spinbox(self.master, from_=1, to=20)
        self.size.pack()
        self.colorchoose = LabelFrame(self.master, text="Color chooser", padx=20, pady=20, cursor="plus")
        self.colorchoose.pack(fill="both", expand="yes")
        self.c=Canvas(self.master,width = 500,height = 500,bg='white',cursor="spraycan")
        self.c.pack(expand="yes")
        #---
        self.menubar = Menu(self.master)
        #===
        self.menu1 = Menu(self.menubar, tearoff=0)
        self.menu1.add_command(label="New file", command=self.newfile)
        self.menu1.add_command(label="Open", command=self.openaf)
        self.menu1.add_command(label="Save", command=self.saveaf)
        self.menu1.add_separator()
        self.menu1.add_command(label="Quit", command=self.master.quit)
        self.menubar.add_cascade(label="File", menu=self.menu1)
        #===
        self.menu2 = Menu(self.menubar, tearoff=0)
        self.menu2.add_command(label="Eraser", command=self.erasera)
        self.menu2.add_command(label="Pen", command=self.pencil)
        #self.menu2.add_command(label="Couper", command=self.alert)
        #self.menu2.add_command(label="Copier", command=self.alert)
        #self.menu2.add_command(label="Coller", command=self.alert)
        self.menubar.add_cascade(label="Tools", menu=self.menu2)
        #===
        self.menu3 = Menu(self.menubar, tearoff=0)
        #self.menu3.add_command(label="A propos", command=self.alert)
        self.menu3.add_command(label="About", command=self.about)
        self.menubar.add_cascade(label="Help", menu=self.menu3)
        #===
        self.blackb=Button(self.colorchoose, text="X", command=self.black, bg="black", fg="white")
        self.blackb.pack(side=LEFT)
        #---
        self.redb=Button(self.colorchoose, text="X", command=self.red, bg="red")
        self.redb.pack(side=LEFT)
        #---
        self.orangeb=Button(self.colorchoose, text="X", command=self.orange, bg="orange")
        self.orangeb.pack(side=LEFT)
        #---
        self.blueb=Button(self.colorchoose, text="X", command=self.blue, bg="blue")
        self.blueb.pack(side=LEFT)
        #---
        self.greenb=Button(self.colorchoose, text="X", command=self.green, bg="green")
        self.greenb.pack(side=LEFT)
        #---
        self.grayb=Button(self.colorchoose, text="X", command=self.gray, bg="gray")
        self.grayb.pack(side=LEFT)
        #---
        self.whiteb=Button(self.colorchoose, text="X", command=self.white, bg="white")
        self.whiteb.pack(side=LEFT)
        #---
        self.othercolorb=Button(self.colorchoose, text="Other color ...", command=self.persocolor)
        self.othercolorb.pack(side=LEFT)
        #===
        self.master.config(menu=self.menubar)
    def drawstop(self, event):
        self.old_x = None
        self.old_y = None
    def draw(self, event):
        self.sizevar = self.size.get()
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x,self.old_y,event.x,event.y,width = self.sizevar, capstyle=ROUND,smooth=True, fill=self.linecolor)
        self.old_x = event.x
        self.old_y = event.y
    def openaf(self):
        if not os.path.exists("mibiimage_tmp"):
            os.makedirs("mibiimage_tmp")
        self.filepath = askopenfilename(title="Ouvrir une image",filetypes=[('Postscript files','.ps'),('Postscript files','.eps'),('Png files','.png'),('all files','.*')])
        try:
            self.c.delete(ALL)
            self.img = Image.open(self.filepath)
            self.img.save('mibiimage_tmp/tmp.png')
            self.to_load_img = PhotoImage(file="mibiimage_tmp/tmp.png")
            self.c.create_image(0, 0, anchor=NW, image=self.to_load_img)
        except OSError:
            showerror("Error""Error no. 1 : Bad image file.")
    def saveaf(self):
        self.filetosave = asksaveasfile(filetypes = [("Postscript files",".ps"),("Postscript files",".eps"),('All Files', '*.*')])
        #self.c.postscript(file=self.filetosave.name(), colormode='color')
        self.saveasfilepath = self.filetosave.name
        self.c.postscript(file=self.saveasfilepath, colormode='color')
    def newfile(self):
        self.c.delete(ALL)
    def erasera(self):
        if self.eraser == 0:
            self.oldcolor = self.linecolor
        self.linecolor = "white"
        self.eraser = 1
    def pencil(self):
        if self.eraser == 1:
            self.linecolor = self.oldcolor
    def colorset(self, color):
        self.linecolor = color
    def black(self):
        self.colorset("black")
    def red(self):
        self.colorset("red")
    def orange(self):
        self.colorset("orange")
    def blue(self):
        self.colorset("blue")
    def green(self):
        self.colorset("green")
    def gray(self):
        self.colorset("gray")
    def white(self):
        self.colorset("white")
    def persocolor(self):
        colorchoose = askcolor(title="Choose a color ...")
        self.colorset(colorchoose[1])
    def about(self):
        showinfo("About", "MiniDrawApp\n_______________\nby mibi88\n_______________\nVersion : v.0.1.4\nLicense :\nThe Unlicense\n_______________\nThank you for\nusing this app !")
"""
#old
def motion(event):
    x2 = event.x
    y2 = event.y
    x1 = event.x + 5
    y1 = event.y + 5    
    print(event)
    c.create_line(x1, y1, x2, y2, width = 3, capstyle=ROUND,smooth=True)
    if x2 == 0 and y2 == 0:
        print('x=%s y=%s' %(event.x,event.y))
        x1 = event.x
        y1 = event.y
        c.create_line(x1, y1, x2, y2)
    else:
        c.create_line(y1, x1, y2, x2)
def click(event):
    c.bind("<Motion>",motion)
"""
root=Tk()
root.title("MiniDrawApp")
paintapp(root)
"""
c=Canvas(root,bg='white')
c.pack(expand="yes")
c.bind("<B1-Motion>", paintapp.draw)
"""
root.mainloop()
