#!/usr/bin/env python3
import os
from PIL import Image

mypath = os.getcwd()+"/images"
for f in os.listdir(mypath):
    try:
        im = Image.open(mypath+"/"+f)
        im.rotate(270).resize((128,128)).save(mypath + "/opt/icons/"+f+".jpeg")
    except OSError:
        pass
    