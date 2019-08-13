
import sys
import numpy as np
import skimage
from skimage.filters import threshold_otsu
import math
from skimage.morphology import remove_small_objects
import time
from dask.array.image import imread
from dask.distributed import Client
from dask import delayed
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def xxx(p1):
    print('first_gui_support.xxx')
    sys.stdout.flush()
    filepath = w.FileEntry.get()
    increment = w.IncrementEntry.get()
    minsize = w.MinEntry.get()
    maxsize = w.MaxEntry.get()
    outfolder = w.OutEntry.get()
    thresh = w.ThreshEntry.get()
    dress = w.SchedEntry.get()
    runfun(filepath, increment, maxsize, minsize, thresh, outfolder)
    destroy_window()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None
    
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+344+143")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Execute = tk.Button(top)
        self.Execute.place(relx=0.217, rely=0.756, height=24, width=51)
        self.Execute.configure(activebackground="#ececec")
        self.Execute.configure(activeforeground="#000000")
        self.Execute.configure(background="#d9d9d9")
        self.Execute.configure(disabledforeground="#a3a3a3")
        self.Execute.configure(foreground="#000000")
        self.Execute.configure(highlightbackground="#d9d9d9")
        self.Execute.configure(highlightcolor="black")
        self.Execute.configure(pady="0")
        self.Execute.configure(text='''Execute''')
        self.Execute.bind('<Button-1>',lambda e:xxx(e))

        self.FileEntry = tk.Entry(top)
        self.FileEntry.place(relx=0.133, rely=0.244,height=20, relwidth=0.273)
        self.FileEntry.configure(background="white")
        self.FileEntry.configure(disabledforeground="#a3a3a3")
        self.FileEntry.configure(font="TkFixedFont")
        self.FileEntry.configure(foreground="#000000")
        self.FileEntry.configure(highlightbackground="#d9d9d9")
        self.FileEntry.configure(highlightcolor="black")
        self.FileEntry.configure(insertbackground="black")
        self.FileEntry.configure(selectbackground="#c4c4c4")
        self.FileEntry.configure(selectforeground="black")

        self.MaxEntry = tk.Entry(top)
        self.MaxEntry.place(relx=0.133, rely=0.4,height=20, relwidth=0.273)
        self.MaxEntry.configure(background="white")
        self.MaxEntry.configure(disabledforeground="#a3a3a3")
        self.MaxEntry.configure(font="TkFixedFont")
        self.MaxEntry.configure(foreground="#000000")
        self.MaxEntry.configure(highlightbackground="#d9d9d9")
        self.MaxEntry.configure(highlightcolor="black")
        self.MaxEntry.configure(insertbackground="black")
        self.MaxEntry.configure(selectbackground="#c4c4c4")
        self.MaxEntry.configure(selectforeground="black")

        self.IncrementEntry = tk.Entry(top)
        self.IncrementEntry.place(relx=0.567, rely=0.244, height=20
                , relwidth=0.273)
        self.IncrementEntry.configure(background="white")
        self.IncrementEntry.configure(disabledforeground="#a3a3a3")
        self.IncrementEntry.configure(font="TkFixedFont")
        self.IncrementEntry.configure(foreground="#000000")
        self.IncrementEntry.configure(highlightbackground="#d9d9d9")
        self.IncrementEntry.configure(highlightcolor="black")
        self.IncrementEntry.configure(insertbackground="black")
        self.IncrementEntry.configure(selectbackground="#c4c4c4")
        self.IncrementEntry.configure(selectforeground="black")

        self.MinEntry = tk.Entry(top)
        self.MinEntry.place(relx=0.567, rely=0.4,height=20, relwidth=0.273)
        self.MinEntry.configure(background="white")
        self.MinEntry.configure(disabledforeground="#a3a3a3")
        self.MinEntry.configure(font="TkFixedFont")
        self.MinEntry.configure(foreground="#000000")
        self.MinEntry.configure(highlightbackground="#d9d9d9")
        self.MinEntry.configure(highlightcolor="black")
        self.MinEntry.configure(insertbackground="black")
        self.MinEntry.configure(selectbackground="#c4c4c4")
        self.MinEntry.configure(selectforeground="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.167, rely=0.178, height=21, width=104)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Enter the File Path''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.617, rely=0.178, height=21, width=113)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Enter The Increment''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.15, rely=0.333, height=21, width=101)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Enter the Max Size''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.633, rely=0.333, height=21, width=100)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Enter the Min Size''')

        self.OutEntry = tk.Entry(top)
        self.OutEntry.place(relx=0.133, rely=0.6,height=20, relwidth=0.273)
        self.OutEntry.configure(background="white")
        self.OutEntry.configure(disabledforeground="#a3a3a3")
        self.OutEntry.configure(font="TkFixedFont")
        self.OutEntry.configure(foreground="#000000")
        self.OutEntry.configure(highlightbackground="#d9d9d9")
        self.OutEntry.configure(highlightcolor="black")
        self.OutEntry.configure(insertbackground="black")
        self.OutEntry.configure(selectbackground="#c4c4c4")
        self.OutEntry.configure(selectforeground="black")

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.15, rely=0.489, height=21, width=108)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Enter the out folder''')

        self.ThreshEntry = tk.Entry(top)
        self.ThreshEntry.place(relx=0.567, rely=0.6,height=20, relwidth=0.273)
        self.ThreshEntry.configure(background="white")
        self.ThreshEntry.configure(disabledforeground="#a3a3a3")
        self.ThreshEntry.configure(font="TkFixedFont")
        self.ThreshEntry.configure(foreground="#000000")
        self.ThreshEntry.configure(highlightbackground="#d9d9d9")
        self.ThreshEntry.configure(highlightcolor="black")
        self.ThreshEntry.configure(insertbackground="black")
        self.ThreshEntry.configure(selectbackground="#c4c4c4")
        self.ThreshEntry.configure(selectforeground="black")

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.583, rely=0.511, height=21, width=140)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Enter the threshold factor''')

#        self.SchedEntry = tk.Entry(top)
#        self.SchedEntry.place(relx=0.567, rely=0.8,height=20, relwidth=0.273)
#        self.SchedEntry.configure(background="white")
#        self.SchedEntry.configure(disabledforeground="#a3a3a3")
#        self.SchedEntry.configure(font="TkFixedFont")
#        self.SchedEntry.configure(foreground="#000000")
#        self.SchedEntry.configure(insertbackground="black")
#
#        self.Label7 = tk.Label(top)
#        self.Label7.place(relx=0.567, rely=0.711, height=21, width=177)
#        self.Label7.configure(background="#d9d9d9")
#        self.Label7.configure(disabledforeground="#a3a3a3")
#        self.Label7.configure(foreground="#000000")
#        self.Label7.configure(text='''Enter the adress of the scheduler''')
#        
        
        
def runfun(file_path, inc, m_size, min_size, thresh, outfolder):
    start = time.time()
    #set the threshold cofactor
    thresholdfactor = thresh
    #set the in increment values
    increment = inc
    #set the min and max pixel values
    max_size = m_size
    min_sizes = min_size
    #load in the image and put it in a numpy array
    #img = Image.open("H:\Alex\\brain_composite_z576_Z000.tif")
    img = skimage.open(file_path)
    #img.load()
    #img.show()
    image = np.asarray(img)
    
    #use gaussian filtering to smooth the image
    filtered = skimage.filters.gaussian(image, sigma = 0.7) - skimage.filters.gaussian(image, sigma = 2)
    #need to convert the negatives to zero first convert to unit64 then to zeros
    #nonsense at the moment need to fix it find a better way to convert to 0s
    filtered = skimage.img_as_uint(filtered)
    #filtered = np.asarray(img)
    
    #calculate the threshold with otsu's method, there are many options so can bechanged
    startingThreshold = math.ceil(threshold_otsu(filtered))
    startingThreshold = math.floor(startingThreshold * thresholdfactor)
    print("threshold at")
    print(startingThreshold)
    intermediate = filtered >= (startingThreshold) 
    
    #Image.fromarray(intermediate).save("firsthreshold.tif")
    #the xor function
    firststep = np.logical_xor((remove_small_objects(intermediate, min_size = min_sizes, connectivity = 8)),(remove_small_objects(intermediate, min_size = max_size, connectivity = 8)))
    nextstep = image >= (startingThreshold + increment)
    
    #Image.fromarray(nextstep).save("afterfirstxor.tif")
    print("threshold at")
    print(startingThreshold + increment)
    
    nextstep = np.logical_xor((remove_small_objects(nextstep, min_size = min_sizes, connectivity = 8)),(remove_small_objects(nextstep, min_size = max_size, connectivity = 8)))
    
    workingstep = (firststep + nextstep) > 0
    ##loop through all the possible threshold values
    for x in range(startingThreshold + increment *2,65534, increment):
        print("threshold at")
        print(x)
        temp = filtered >= x
        labeled = skimage.measure.label(temp)
        maxi =0
        for region in skimage.measure.regionprops(labeled):
            if region.area > maxi:
                maxi = region.area
        print(maxi)
        if maxi < min_sizes:
            break
        diff =np.logical_xor((remove_small_objects(temp, min_size = min_sizes, connectivity = 8)),(remove_small_objects(temp, min_size = max_size, connectivity = 8)))
        workingstep = (workingstep + diff) > 0
    
    #finalimage = Image.fromarray(workingstep)
    #finalimage.save("H:\Alex\\output.tif")
    toSave = skimage.img_as_ubyte(workingstep)
    path = outfolder + "/threshold_out.tif"
    skimage.io.imsave(path,toSave)
    end = time.time()
    print((end - start)/60)



if __name__ == '__main__':
    vp_start_gui()
