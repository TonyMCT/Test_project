#!/usr/bin/env python3
from PIL import Image
im = Image.open("bride.jpg")
im.rotate(45).show()