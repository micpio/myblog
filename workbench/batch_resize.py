from PIL import Image
import os, sys
from icecream import ic

f = os.getcwd()
fi = f+"/tobe/"
fo = f+ "/processed/"
    
    
def batch():
    files = os.listdir(fi)
    new_width = int(input("Enter width desired  :"))
    for file in files:
        print(f'Opening {fi}'+file)
        im = Image.open(fi + file)
        aspect_ratio = round((im.height / im.width),2)
        print("aspect ratio")
        print(aspect_ratio)

        new_height = round(new_width * aspect_ratio)
        new = im.resize((new_width, new_height), Image.LANCZOS)
        new.save(fo + "re" +file )
        nf = fo + "re"+ file

        print(fi)
        print("originnal size")
        print(im.size )
        print("resized with new name")
        print(new.size)
        print(nf)
