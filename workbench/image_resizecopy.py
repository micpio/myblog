#!/usr/bin/python3
from PIL import Image
import os, sys
from icecream import ic
from batch_resize import batch
from fixed_height import overide
f = os.getcwd()
fi = f+"/tobe/"
fo = f+ "/processed/"

def ProcessOne(f):

    # Create a list of files to process
    files = os.listdir(fi)
    print("do you wish to overide aspect height enter y or n")
    
    overide_height = input("Enter y or n___:")
    if overide_height =="":
        overide_height = input("Enter (not blank) y or n___:")    
        if  overide_height=="n":
            batch()
            ic("yes")
        else:
            overide()
            ic("no")

        #if __name__ == '__main__':



ProcessOne(f)


