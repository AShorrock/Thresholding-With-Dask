
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
    runfun(filepath, increment, maxsize, minsize, thresh, outfolder, dress)
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

        self.SchedEntry = tk.Entry(top)
        self.SchedEntry.place(relx=0.567, rely=0.8,height=20, relwidth=0.273)
        self.SchedEntry.configure(background="white")
        self.SchedEntry.configure(disabledforeground="#a3a3a3")
        self.SchedEntry.configure(font="TkFixedFont")
        self.SchedEntry.configure(foreground="#000000")
        self.SchedEntry.configure(insertbackground="black")

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.567, rely=0.711, height=21, width=177)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Enter the adress of the scheduler''')



def godfun(image):
    global increment
    global max_size
    global min_sizes
    global thresholdfactor
    global out
    print(increment, max_size, min_sizes)
    
    #Using gaussian subtraction on the image followed by a reytping of the image so it can be passed to the next step
    filtered = skimage.filters.gaussian(image, sigma = 0.7) - skimage.filters.gaussian(image, sigma = 2)
    filtered = skimage.img_as_uint(filtered)

    #check if there is anything in the image region and if there is not skip it
    #otherwise continue on in the algorithm
    if filtered.min() == filtered.max():
        startingThreshold = 1
        return filtered
    else:
        #determine where the thresholding should start by using the otsu threshold to calculate the correct value
        #this value can then be manipulated with the threshold factor
        startingThreshold = math.ceil(threshold_otsu(filtered))
        startingThreshold = math.floor(startingThreshold * thresholdfactor)
        print("First threshold at " + str(startingThreshold))
        intermediate = filtered >= (startingThreshold) 
        
        # this is the xor funcction that is used to only keep objects that are within a specified range in the image
        firststep = np.logical_xor((remove_small_objects(intermediate, min_size = min_sizes, connectivity = 3)),(remove_small_objects(intermediate, min_size = max_size, connectivity = 3)))
        #take the image with removed objects and then threshold it again increasing the threshold value
        nextstep = filtered >= (startingThreshold + increment)
        

        print("Increment threshold to " + str(startingThreshold + increment))
        # the next command to remove objects inbetween a set size
        nextstep = np.logical_xor((remove_small_objects(nextstep, min_size = min_sizes, connectivity = 3)),(remove_small_objects(nextstep, min_size = max_size, connectivity = 3)))
        
        workingstep = (firststep + nextstep) > 0
        ##loop through all the possible threshold values and continue the pattern of thresholding 
        #and then removing all objects that are not within a certain size
        for x in range(startingThreshold + increment *2,65534, increment):
            print("Increment threshold to " + str(x))
            temp = filtered >= x
            labeled = skimage.measure.label(temp)
            maxi = 0
            #this will determine the size of the objects in the image
            #if there is no object that is greater in size then the smallest possible image
            #the loop will end as there is ntohing left to find
            #otherwise it will continue until thru the possible pixel values
            for region in skimage.measure.regionprops(labeled):
                if region.area > maxi:
                    maxi = region.area
            print("Maximum size of objects = " + str(maxi))
            if maxi < min_sizes:
                print("Ending loop due to no objects greater than the minimum size found")
                break
            diff =np.logical_xor((remove_small_objects(temp, min_size = min_sizes, connectivity = 3)),(remove_small_objects(temp, min_size = max_size, connectivity = 3)))
            workingstep = (workingstep + diff) > 0
        #add one final filter step after the loop that is identical to the first steps of algorithm
        refilter = skimage.filters.gaussian(workingstep, sigma = 0.7) - skimage.filters.gaussian(workingstep, sigma = 2)
        refilter = skimage.img_as_ubyte(refilter)
        if refilter.min() == refilter.max():
            thresh = 1
        else:
            thresh = math.ceil(threshold_otsu(refilter))
        refilter = refilter >= thresh
        nosmall = remove_small_objects(refilter, min_size = 2000)
        return nosmall
    
# a function to save the images in time so they all do not need to be put into the ram of one machience
def savefun(image,num):
    print('saving')
    saver=skimage.img_as_ubyte(image)
    path = (out + str(num) + '.tif')
    skimage.io.imsave(path,saver)
    return num
    
#the method that is run by the gui
def runfun(file_path, inc, m_size, min_size, thresh, outfolder, dress):
    global increment
    global max_size
    global min_sizes
    global thresholdfactor
    global out
    increment = int(inc)
    max_size = int(m_size)
    min_sizes = int(min_size)
    thresholdfactor =  float(thresh)
    out = outfolder
    #connects to the sheduler for the use of dask
    client = Client(dress, processes = True)
    start = time.time()
   
    set_images = imread(file_path)

    #rechunk the image in a good set of dimensions that are large and fit in ram correctly
    image = set_images.rechunk((5,2048,2048))
    print(image)

    print("computing")
    
    tup = image.shape

    #this function will loop thru the image set to cut down on the size of the entire volume
    #As dask is already going to cut down and not do the entire colume at once this will
    #cut down even more by splitting it up by a set of 75 
    #this can be modified to fit the shape of each volume it will be run with
    
    z = 0
    for x in range(2,tup[0],75):
        savedFiles = []
        temparray = image[x - 2:x + 75,0:tup[1],0:tup[2]]
        newshape = temparray.shape
        workingstep = temparray.map_overlap(godfun, depth = (2,30,30),trim = True, dtype = 'uint16')
        for y in range(0, newshape[0]):
            q = delayed(savefun)(workingstep[y],z)
            savedFiles.append(q)
            z += 1
        total = sum(savedFiles)
        total = total.compute()

    end = time.time()
    print((end - start)/60)
    
    del workingstep
    
    client.close()
    
    
if __name__ == '__main__':
    vp_start_gui()