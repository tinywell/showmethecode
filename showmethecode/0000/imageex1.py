# -*- coding:utf-8 -*-

"""
图像右上角加角标
"""
import Image,ImageDraw,ImageFont

im = Image.open("20110627.png")
draw = ImageDraw.Draw(im)
width,height = im.size

#画出角标区域（暂用20*20的矩形）

box_size = 100
#box = ((width-box_size,0),(width,box_size))
#draw.rectangle(box,fill=(255, 0, 0))

font = ImageFont.truetype("msyh.ttf",80)
draw.text((width-box_size+10,10),"6",(0, 255, 0),font)

#print font.getsize("4")

#print (height,width)

im.show()