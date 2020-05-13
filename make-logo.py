from write-text-logo import create_title

#read the txt file
myfile = open('text.txt', 'r')
title = myfile.readlines()

#define variable
count = 0

#loop for creating bunch of images from txt file
for x in title:
    count += 1
    name = 'example' + str(count) + '.png'
    create_title(x,name)
