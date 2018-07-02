from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
from Tkinter import Button, Frame, Entry, END
import spectral
from spectral import *
import os
test1=False
var=None
a=[]
filename=''
img=None
variable=''
variable1=''
variable2=''
variable3=''
bandlist=[]
w=None
w1=None
w2=None
w3=None
button=None
button1=None
v=None
def specfun():
    os.startfile('spec.py')
def unmixfun():
    os.startfile('Unmixing_Coeff.py')
def helpimg():
    os.startfile("Image Visualizer Help.pdf")
def helppdf():
    os.startfile("help.pdf")
def exito():
    global root1
    root1.destroy()
def getScript1(R1):
    global var
def app():
    global var,m2
    global variable,variable1,variable2,variable3
    root=Toplevel(root1)
    root.geometry('400x200')
    root.wm_iconbitmap('Icon\hydas.ico')
    for i in range(5):
        root.columnconfigure(i, weight=1)
    for i in range(1,6):
        root.rowconfigure(i, weight=1)
    # make a master PanedWindow
    m1 = PanedWindow(root)
    m1.grid(column=0, row=0, rowspan=5, columnspan=5, sticky=E+N+W+S)
    for i in range(5):
        m1.columnconfigure(i, weight=1) # Enable vertical resizing
    for i in range(1,6):
        m1.rowconfigure(i, weight=1) #Enable horizontal resizing
    # make a PanedWindow inside m1, positioned to the left
    m2=PanedWindow(m1)
    m2.grid(column=0, row=1, columnspan=5, rowspan=5, sticky=E+N+W+S)
    for i in range(5):
        m2.columnconfigure(i, weight=1) # Enable vertical resizing
    for i in range(1,6):
        m2.rowconfigure(i, weight=1) #Enable horizontal resizing
    root.wm_title('HyDaS')
    root.option_add('*tearOff',False)
    menu=Menu(root)
    subMenu=Menu(menu)
    subMenu.add_command(label="Open",command=openFile)
    menu.add_cascade(label="File",menu=subMenu)
    hMenu=Menu(menu)
    hMenu.add_command(label="About Image Visualizer",command=helpimg)
    menu.add_cascade(label="Help",menu=hMenu)
    root.config(menu=menu)
    var=IntVar()
    selrgbgray=Frame(m2)
    rad1 = Radiobutton(selrgbgray,text='RGB', variable=var,value=1,command = lambda : rgb(rad1)).pack(anchor=CENTER)
    rad2 = Radiobutton(selrgbgray,text='GRAY', variable=var,value=2,command = lambda : gray(rad2)).pack(anchor=CENTER)
    m2.add(selrgbgray)
    variable = StringVar(m2)
    variable1 = StringVar(m2)
    variable2 = StringVar(m2)
    variable3 = StringVar(m2)
    root.mainloop()
def rgb(rad1):
    global variable,variable1,variable2,m2,bandlist,w,w1,w2,w3,button,button1
    if w3:
        w3.destroy()
        button1.destroy()
    variable.set('Select Red Band')
    w = OptionMenu(m2, variable, *bandlist)
    w.pack(pady =(50,0), padx = 80)

    variable1.set('select Green band')
    w1 = OptionMenu(m2, variable1, *bandlist)
    w1.pack(pady = 0, padx = 80)

    variable2.set('select Blue band')
    w2 = OptionMenu(m2, variable2, *bandlist)
    w2.pack(pady = 0, padx = 80)
    
    button = Button(m2, text="OK", command=ok)
    button.grid(row=0, column=0)
    button.pack()
def gray(rad1):
    global variable3,m2,bandlist,w,w1,w2,w3,button,button1
    if w:
        w.destroy()
        w1.destroy()
        w2.destroy()
        button.destroy()
    variable3.set('select band')
    w3 = OptionMenu(m2, variable3, *bandlist)
    w3.pack(pady =(50,0), padx = 80)
    button1 = Button(m2, text="OK", command=ok1)
    button1.pack()
def openFile():
    global filename
    global var,img,bandlist
    filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes =(("all files","*.*"),("jpeg files","*.jpg")))
    img=spectral.open_image(filename)
    bandlist=[]
    band=img.shape[2]
    for i in range(band):
        bandlist.append('Band'+str(i)+' '+'('+str(img.bands.centers[i])+' '+str(img.bands.band_unit)+')')
def doNothing():
    print('Nothing')
def view(a):
    global img,v
    v=imshow(img,(int(a[0]),int(a[1]),int(a[2])))
    return []
    
def ok():
    global test1
    global a
    global variable,variable1,variable2
    x=variable.get()
    x=x.split()
    a.append(x[0][4:])
    x=variable1.get()
    x=x.split()
    a.append(x[0][4:])
    x=variable2.get()
    x=x.split()
    a.append(x[0][4:])
    a=view(a)
    test1=True
def ok1():
    global test1
    global a
    global variable3
    x=variable3.get()
    x=x.split()
    a.append(x[0][4:])
    a.append(x[0][4:])
    a.append(x[0][4:])
    a=view(a)
    test1=True

root1=Tk()
root1.option_add('*tearOff',False)
root1.geometry('400x20')
root1.wm_title('HyDaS')
root1.wm_iconbitmap('Icon\hydas.ico')
menu=Menu(root1)
subMenu=Menu(menu)
subMenu.add_command(label="Open",command=app)
subMenu.add_command(label="Exit",command=exito)
menu.add_cascade(label="Image Visualizer",menu=subMenu)
specMenu=Menu(menu)
specMenu.add_command(label="Spectral Library Viewer",command=specfun)
menu.add_cascade(label="Spectral",menu=specMenu)
unMenu=Menu(menu)
lin=Menu(unMenu)
unMenu.add_cascade(label="Linear",menu=lin)
lin.add_command(label="Least Square",command=unmixfun)
unMenu.add_command(label="Non Linear",command=doNothing)
menu.add_cascade(label="Unmixing",menu=unMenu)
simMenu=Menu(menu)
menu.add_cascade(label="Data Simulation",menu=simMenu)
hMenu=Menu(menu)
hMenu.add_command(label="About HyDaS",command=helppdf)
menu.add_cascade(label="Help",menu=hMenu)
root1.config(menu=menu)
root1.mainloop()
__author__ = 'Keshav Goswami and Akriti'
