
#############################################################
# this is a personal implementation of the decoding process #
#############################################################


import cv2
import numpy as np
import random

def decode_img(img): #reshaping the image and checking the rgb values of each pixel ,even means 1, odd means 0
    img=cv2.imread(img)
    M=np.array(img).flatten().tolist()
    counter=0
    output=[]
    bits=''
    for i in M:
        if i%2==1:
            bits+='1'
        else:
            bits+='0'
        counter+=1
        if counter==9:
            if bits=='1'*9:
                break
            output+=[bits]
            bits=''
            counter=0
    output="".join(output)
    output=[output[i:i+9] for i in range(0,len(output),9)]
    return output

def bin_to_msg(l):#converting the extracted message into a readable one
    print(l)
    return ''.join([chr(int(i,2)) for i in l])

def decoding(img):#main function, handle some errors
    if not img:
        return "Can't found the image ."
    try:
        return bin_to_msg(decode_img(img))
    except Exception as exp:
        print(exp)



