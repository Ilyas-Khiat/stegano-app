
###########################################################
# this is a personal implementation of the coding process#
###########################################################

import cv2 #for image processing

def msg_to_bin(msg):#convert the message to binary , each character of the message is converted to a 9bit number that will be stored in 3pixels
    return [f'{ord(i):09b}' for i in msg]

def map_code(coded_msg):#reshaping the msg
    temp=list(map(lambda x:[[int(i) for i in x[j:j+3]] for j in range(0,len(x),3)],coded_msg))
    output=[]
    for triplet in temp:
        output+=[*triplet]
    return output

def hide_msg(code,img):#the main operation is done here ,each bit in the coded message is compared to the rgb value of the pixel by checking the parity of both
    w=img.shape[1]
    code+=[[1,1,1]]*3
    for i in range(len(code)):
        for j in range(3):
            if img[i//w,i%w,j]%2==1 and code[i][j]==0:
                if img[i//w,i%w,j]==255:
                    img[i//w,i%w,j]-=1
                else:
                    img[i//w,i%w,j]+=1
            elif code[i][j]==1 and img[i//w,i%w,j]%2==0:
                img[i//w,i%w,j]+=1
    return img


def coding(msg,img_dir,folder):#this function groups the previous ones and handle some errors
    if msg=='':
        return "You can't send the void. Write something!!!"
    try:
        img=cv2.imread(img_dir)
        output=hide_msg(map_code(msg_to_bin(msg)),img)
        cv2.imwrite(f"{folder}/{img_dir.split('/')[-1].split('.')[0]}-embedding.png",output)
        return 'Done :) , check the output folder you chose!'
    except:
        return 'Error, you can check directories ...'



