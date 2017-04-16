
# coding: utf-8

# In[ ]:

from PIL import Image
import random

K = 5   # number of colors
W = 800  # width of output image
H = 600  # height of output image
MAX_ITER = 3

def find_nearest(pixels, centroids):
    re = []
    for pixcel in range(len(pixels)):
        a = [0,0,0,0,0]
        for cen in range(K):
            for rgb in range(3):
                a[cen] += int((pixels[pixcel][rgb]-centroids[cen][rgb])**2)
            a[cen]=a[cen]**0.5

        cnt=a[0]
        ans=0
        for i in range(1,5):
            if a[i]<=cnt:
                ans = i
                cnt = a[i]
        re.append(ans)
    return (re)

def compute_centroid(pixels, clusters):
    scom =[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    count = [0,0,0,0,0]
    recom = []
    for i in range(W*H):
        for j in range(3):
            cli=clusters[i]
            scom[cli][j]+=pixels[i][j]
        count[cli]+=1
            
    for i in range(W*H):
        cli = clusters[i]
        rec = []
        for j in range(3):
            scom[cli][j]/=count[cli]
            rec.append(scom[cli][j])
        recom.append(rec)
    return (recom)                     

im = Image.open('sample.jpg')
im = im.resize( (W, H) )
pixels = []
for i in range(W):
    for j in range(H):
        pixels.append(im.getpixel((i, j)))

centroids = random.sample(pixels, K)
for t in range(MAX_ITER):
    print("Iter", t+1)
    clusters = find_nearest(pixels, centroids)
    centroids = compute_centroid(pixels, clusters)
clusters = find_nearest(pixels, centroids)

for i in range(K):
    centroids[i] = tuple(map(int, centroids[i]))

nim = Image.new('RGB', (W, H))
for i in range(W):
    for j in range(H):
        nim.putpixel((i, j), centroids[clusters[i*H+j]])
nim.save('output2.jpg')

