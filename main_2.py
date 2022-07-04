import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import numpy
import cv2
import glob
import os

tkWindow = Tk()
tkWindow.geometry('600x250')
tkWindow.title('Vox Tech. Watermark App')

my_dir='' # string to hold directory path
def my_fun():
    my_fun.my_dir= filedialog.askdirectory() # select directory
    l1.config(text=my_fun.my_dir) # update the text of Label with the target directory path

def my_out():
    my_out.my_dir_out = filedialog.askdirectory()  # select directory
    l3.config(text=my_out.my_dir_out)  # update the text of Label with Output directory path
# Opening the image to be used for Watermark
logo = cv2.imread("logo.png")
#assert not isinstance(logo,type(None)), 'image not found'
h_logo, w_logo, _ = logo.shape
img_lst='/*.*' #images inside the selected directory

def my_mk():
    my_mk.lst=my_fun.my_dir+img_lst
    #l2.config(text=my_cn.lst)
    # Opening the Image path/directory of images that we want to watermark
    images_path = glob.glob(my_mk.lst)
    for img_path in images_path:
        img = cv2.imread(img_path)
        h_img, w_img, _ = img.shape
        #Position the area for which the watermark image
        center_y = int(h_img / 2)
        center_x = int(w_img / 2)
        top_y = center_y - int(h_logo / 2)
        left_x = center_x - int(w_logo / 2)
        bottom_y = top_y + h_logo
        right_x = left_x + w_logo
        # cv2.circle(img, (left_x, top_y), 10, (0, 255, 0), -1)
        # cv2.circle(img, (right_x, bottom_y), 10, (0, 255, 0), -1)

        # Get RIO
        roi = img[top_y: bottom_y, left_x: right_x]  #
        result = cv2.addWeighted(roi, 1, logo, 0.9, 0)  # Watermark result
        img[top_y: bottom_y, left_x: right_x] = result
        filename = os.path.basename(img_path)
        # Reducing image Size
        #    img_resize = cv2.resize(img, (1350, 1350))

        # Saving Watermarked imagaes
        cv2.imwrite(my_out.my_dir_out+'/Watermarked_'+ filename, img)
        # print("watermark Added!")


b1=tk.Button(tkWindow,text='Select directory',font=22,
    command=lambda:my_fun(),bg='lightgreen')
b1.grid(row=0,column=0,padx=10,pady=20)

l1=tk.Label(tkWindow,text=my_dir,bg='yellow',font=18)
l1.grid(row=0,column=1,padx=2)

#e1= Entry(tkWindow, text=my_dir, font=18)
#e1.grid(row=0,column=1,padx=2)
#e1.focus_set()
#e1.pack()

b3=tk.Button(tkWindow,text='Output directory',font=22,
    command=lambda:my_out(),bg='grey')
b3.grid(row=1,column=0,padx=10,pady=20)

l3=tk.Label(tkWindow,text=my_dir,bg='red',font=18)
l3.grid(row=1,column=1,padx=2)

b2=tk.Button(tkWindow,text='Watermark Images',font=22,command=lambda:my_mk())
b2.grid(row=2,column=1,padx=10,pady=30)

#l2=tk.Label(tkWindow,text=my_dir,bg='green',font=12)
#l2.grid(row=3,column=5,padx=2)

tkWindow.mainloop()