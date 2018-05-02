from skimage import io
import os
import matplotlib.pyplot as plt
import numpy as np

# load image into python
imagepath = os.path.join(os.getcwd(), 'face.png')
image = io.imread(imagepath)
plt.imshow(image)
plt.show()
# look at different properties of the image
Dict = {}
type(image)
image.shape
image.dtype
image.size
red_data = image[:,:,0]
green_data = image[:,:,1]
blue_data = image[:,:,2]
plt.imshow(image)
plt.show()
big_big_list = []
for x in range(image.shape[0]):
    for y in range(image.shape[1]):
        pixel = int(''.join([str(red_data[x,y]), str(blue_data[x, y]), str(green_data[x, y])]))
        if pixel not in Dict:
            Dict[pixel] = 1
        else:
            Dict[pixel] += 1
        big_big_list.append(pixel)
variance = len(Dict.keys()) // 10
keys = list(Dict.keys())
big_list = [0] * 10007
start = min(Dict.keys())
count = 0
#for item in keys:
#    if item > start + variance:
#        start += variance
#        count += 1
#    big_list[count] += Dict[item]
#for i in range(0, max(Dict.values()), variance):
plt.hist(big_big_list, bins = 100)
#plt.bar(Dict.keys(), Dict.values())
#from tkinter import Tk, Canvas, PhotoImage, mainloop
#
#WIDTH, HEIGHT = 200, 100
#
#window = Tk()
#w = Canvas(window, width=WIDTH, height=HEIGHT)
#w.pack()
#img = PhotoImage(file = 'sample.png')
#w.create_image((0,0), img)
#mainloop()

# i dont know how to procees lol
