#!/usr/bin/env python3
import os
from PIL import Image

mypath = os.getcwd()+"/images"
for f in os.listdir(mypath):
 try:
  #print(mypath+"/"+f)
  im = Image.open(mypath+"/"+f).convert('RGB')
  im.rotate(270).resize((128,128)).save("/opt/icons/"+f,"jpeg")
  print("/opt/icons/"+f+".jpeg")
 except OSError:
    pass