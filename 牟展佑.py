
# coding: utf-8

# In[11]:

from PIL import Image
im = Image.open("sample.jpg")

for i in range(1280):
    for j in range(851):
        r,g,b = im.getpixel((i,j))
        r=(r**0.5)*16
        r=int(r)
        im.putpixel((i,j),(r,g,b))
im.save( "output.jpg" )


# In[12]:

from PIL import Image
import random

im = Image.open("sample.jpg")
Id, R, G, B = [],[],[],[]
for i in range(256):
    Id.append(i)
    R.append(0)
    G.append(0)
    B.append(0)
    
for i in range(1280):
    for j in range(851):
        r,g,b = im.getpixel((i,j))
        R[r]+=1
        G[g]+=1
        B[b]+=1
        

get_ipython().magic('matplotlib notebook')
from matplotlib import pyplot

pyplot.figure(1)
pyplot.subplot(311)
pyplot.fill_between(Id, R, color='red')

pyplot.subplot(312)
pyplot.fill_between(Id, G, color='green')

pyplot.subplot(313)
pyplot.fill_between(Id, B, color='blue')


# In[13]:

from PIL import Image
im = Image.open("sample.jpg")

for i in range(256):
    for j in range(170):
        sr=0
        sg=0
        sb=0
        for k in range(5):
            for l in range(5):
                r,g,b = im.getpixel((5*i+k,5*j+l))
                sr+=r
                sg+=g
                sb+=b
        sr=int(sr/25)
        sg=int(sg/25)
        sb=int(sb/25)
        for k in range(5):
            for l in range(5):           
                im.putpixel((5*i+k,5*j+l),(sr,sg,sb))
im.save( "bonus.jpg" )

