from PIL import Image
import os, sys
from icecream import ic

f = os.getcwd()
fi = f+"/tobe/"
fo = f+ "/processed/"
    
    
    
    
def overide():
    files = os.listdir(fi)
    
    for file in files:
        print(f'Opening {fi}'+file)
        im = Image.open(fi + file)
        new_width = int(input("Enter width desired  :"))
        new_height = int(input("Enter height"))
        new = im.resize((new_width, new_height), Image.LANCZOS)
        new.save(fo + "re" +file )
        nf = fo + "re"+ file
        print(fi)
        print("originnal size")
        print(im.size )
        print("resized with new name")
        print(new.size)
        print(nf)
        
                
