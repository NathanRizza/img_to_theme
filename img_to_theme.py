#!/usr/bin/python
#Author: Nathan Rizza
#10/26/2022
import sys
from matplotlib import image
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

def rgb_to_hex(rgb):
    rgb2hex = lambda r,g,b: '#%02x%02x%02x' %(r,g,b)
    return [ rgb2hex(*rgb[i,:]) for i in range(rgb.shape[0]) ]

filename = sys.argv[1]

#Read in img

image_array = image.imread(filename) # TODO: Rezise image to make it smaller so less computation

image_h = image_array.shape[0]
image_w = image_array.shape[1]

image_pixels = image_h * image_w

image_array = image_array.reshape(image_pixels, 3)

#Extract n most common colors

n_clust = 8; # for plamora currently, will change in future to make it general

print('Generating Theme For: ', filename , " please wait...")

kmeans_output = KMeans(n_clusters=n_clust, random_state=0 ,n_init = 1, max_iter = 10).fit(image_array)

Average_Color_Int = (kmeans_output.cluster_centers_).astype(int)

#Assign colors to theme template automatically (darker colors are background ect..)

print("Theme:")
print(Average_Color_Int)
print(rgb_to_hex(Average_Color_Int))
color_img = np.tile(0, (n_clust*100,100 ,3))

color_img[150][50][1] = 0;
for i in range (0,n_clust):
    for j in range (0,3):
        for k in range (i*100,(i*100)+100):
            for l in range (0,100):
                color_img[k][l][j] = Average_Color_Int[i][j]

imgplot = plt.imshow(color_img)
plt.show()

# TODO convert output ot HEX and print to file


