from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort

root = Tk()
root.title('Sorting Algo Visualisation')
root.maxsize(900,600)
root.config(bg = 'black')

# Variables
selected_algo = StringVar()
data = []

def drawData(data,colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width/(len(data))
    spacing = 10
    normalizdData = [i/max(data) for i in data]
    for i, height in enumerate(normalizdData):
        #top left
        x0 = i * x_width + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()

def Generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))
    drawData(data, ['red' for x in range(len(data))])

def startAlgo():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort' :
        quick_sort(data, 0, len(data)-1, drawData,    speedscale.get())
    elif algMenu.get()=='Bubble Sort' :
        bubble_sort(data, drawData, speedscale.get())
    elif algMenu.get()=='Merge Sort' :
        merge_sort(data, drawData, speedscale.get())
    drawData(data, ['green' for x in range(len(data))])

#frame / base layout

UI_frame = Frame(root, width = 600, height = 200, bg = "grey")
UI_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

canvas = Canvas(root, width = 600, height = 380, bg = 'white')
canvas.grid(row = 1, column = 0, padx = 10, pady = 5)

# User Interface Area
# Row[0]

Label(UI_frame, text = "Algorithm", bg = "grey").grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable = selected_algo, value=['Bubble Sort','Merge Sort','Quick Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedscale = Scale(UI_frame, from_=0.01, to=2.0, length=200, digits=3, resolution=0.01, orient=HORIZONTAL, label="Select Speed [s]")
speedscale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=startAlgo, bg="red").grid(row=0, column=3, padx=5, pady=5)


#Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=25, length=200, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5,pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, length=200, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5,pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, length=200, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5,pady=5)

Button(UI_frame, text="Generate", command=Generate, bg="blue").grid(row=1, column=3, padx=5, pady=5)

root.mainloop()