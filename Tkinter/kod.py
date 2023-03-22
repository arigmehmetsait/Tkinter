# AhmetUğur-Gülsevinç-1200505038
# MehmetSait-Arığ-1200505043
# Yasemin-Karaloğlu-1200505004


import cv2
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import *

def apply_filters(image_path):
  
    resim = cv2.imread(image_path)

    
    a = input ("Kernel w değerini giriniz : ")
    b = input ("Kernel h değerini giriniz : ")
    c = input ("Median Filtresine w&h değerini giriniz(Tek sayı olmalı) : ")
    d = input ("GaussianBlur w değerini giriniz(Tek sayı olmalı) : ")
    e = input ("GaussianBlur h değerini giriniz(Tek sayı olmalı) : ")
    f = input ("Bilateral w değerini giriniz : ")
    g = input ("Bilateral h değerini giriniz : ")
    i = input ("Averaging Blur değerinin w giriniz : ")
    j = input ("Averaging Blur değerinin w giriniz : ")
   

    
    kernel = np.ones((int(a),int(b)),np.float32)/25
    medianBlur = cv2.medianBlur(resim, int(c),kernel)
    GaussianBlur = cv2.GaussianBlur(resim, (int(d),int(e)), 0,kernel)
    bilateral = cv2.bilateralFilter(resim,int(f),int(g),int(g),kernel)
    averaging = cv2.blur(resim, (int(i),int(j)),kernel)
    krnl= cv2.filter2D(resim,-1,kernel)
    
    

    plt.subplot(152),plt.imshow(GaussianBlur),plt.title("GaussianBlur")
    plt.xticks([]),plt.yticks([])
    plt.subplot(153),plt.imshow(medianBlur),plt.title("medianBlur")
    plt.xticks([]),plt.yticks([])
    plt.subplot(154),plt.imshow(bilateral),plt.title("Bilateral")
    plt.xticks([]),plt.yticks([])
    plt.subplot(155),plt.imshow(averaging),plt.title("Averaging")
    plt.xticks([]),plt.yticks([])

    cv2.imwrite("Yeni_goruntu.jpg", resim)
    plt.show()
    
    

def browse_file():
    file_path = filedialog.askopenfilename()
    apply_filters(file_path)
    
    

kok = tk.Tk()

kok.title("Resim Seçme")
kok.geometry("350x175")




browse_button = Button(kok, text="Gözat", command=browse_file)
browse_button.pack(pady=20)

t1 = tk.Text(height=4, width=50)
t1.pack()
t1.insert(tk.END, "Resim seçiminiz yaptıktan sonra terminalde çıkan inputları doldurmanız gerektmektedir.")

kok.mainloop()



