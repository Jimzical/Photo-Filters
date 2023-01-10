import cv2
import numpy as np

'''
All the functions in this file are used to edit an image
The functions are:
    - CroppingImage
    - ImageSharpen
    - ImageCrop
    - ChangeBrightness
    - ChangeSaturation
    - ChangeContrast
    - ChangeHue
    - ImageRotate
    - ImageFlip
    - ImageResize
'''

def ColorEditor(img,show = False,ResizeValue = 1):
    '''
    ----------------------------------------------------
    WARNING: this function has not been tested yet
    ----------------------------------------------------

    # To edit the color of an image 

    - @img = the image that you want to edit the color of

    optional:
    - @show = if you want to show the image (default = False) [Doesnt Return the image, Doesnt save the image]
    - @ResizeValue = the value that you want to resize the image by (default = 1) (Range[0-1])

     Return the image with the color edited

    '''
    # img = cv2.colorEditor(img)
    return img
        
def ChangeBrightness(img,value = 30,show = False, ResizeValue = 1):
    '''
   # To change the brightness of an image

    - @img = the image that you want to change the brightness of
    optional:
    - @value = the value of the brightness (default = 30) (Range[0-255])
    - @show = if you want to show the image (default = False) [Doesnt Return the image, Doesnt save the image]
    - @ResizeValue = the value that you want to resize the image by (default = 1) (Range[0-1])

     Return the image with the brightness changed
    '''
    value = int(value)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)


    return img

def ChangeSaturation(img,value = 30,show = False, ResizeValue = 1):
    '''
    # To change the Saturation of an image
    ### not sure how this works

    - @img = the image that you want to change the Saturation of
    optional:
    - @value = the value of the Saturation (default = 30) (Range[0-255])
    - @show = if you want to show the image (default = False) [Doesnt Return the image, Doesnt save the image]
    - @ResizeValue = the value that you want to resize the image by (default = 1) (Range[0-1])

     Return the image with the Saturation changed
    '''
    value = int(value)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s[s > 255 - value] = 255
    s[s <= 255 - value] += value
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)


    return img

def ChangeHue(img,value = 100,show = False, ResizeValue = 1):
    '''
    # To change the Hue of an image
    ### not sure how this works

    - @img = the image that you want to change the Hue of
    optional:
    - @value = the value of the Hue (default = 30) (Range[0-255])
    - @show = if you want to show the image (default = False) [Doesnt Return the image, Doesnt save the image]
    - @ResizeValue = the value that you want to resize the image by (default = 1) (Range[0-1])

     Return the image with the Hue changed
    '''
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    h[h > 255 - value] = 255
    h[h <= 255 - value] += value
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)


    return img

def ImageResize(img,percent = 200,show = False):
    '''
    # To resize an image

    - @img = the image that you want to resize

    Optional:
    - @percent = the percent of the resize (default = 0.5) (Range[0-1])
    - @show = if you want to show the image (default = False) [Doesnt Return the image, Doesnt save the image]

     Return the image resized
    '''
    width = int(img.shape[1] * percent/100)
    height = int(img.shape[0] * percent/100)
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return img 

def ImageRotate(img,angle = 90,show = False, ResizeValue = 1):
    '''
    # To rotate an image

    - @img = the image that you want to rotate

    Optional:
    - @angle = the angle of the rotation (default = 90) (Range[0-360])
    - @show = if you want to show the image (default = False) [Doesnt Return the image, Doesnt save the image]
    - @ResizeValue = the value that you want to resize the image by (default = 1) (Range[0-1])

     Return the image rotated
    '''
    (h, w) = img.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    img = cv2.warpAffine(img, M, (w, h))


    return img



def ImageFlip(img,show = False, ResizeValue = 1):
    '''
    # To flip an image

    - @img = the image that you want to flip

    Optional:
    - @show = if you want to show the image (default = False) [Doesnt Return the image, Doesnt save the image]
    - @ResizeValue = the value that you want to resize the image by (default = 1) (Range[0-1])

     Return the image flipped
    '''
    img = cv2.flip(img, 1)
    return img

def ImageCrop(img,RowStart = 0,ColumnStart = 0,RowEnd = 100,ColumnEnd = 100,show = False, ResizeValue = 1):
    '''
    # To crop an image
    ## Easy way to crop an image compared to CroppingImage
    ### Not Tested Yet

    - @img = the image that you want to crop

    Optional:
    - @show = if you want to show the image (default = False) [Doesnt Return the image, Doesnt save the image]
    - @ResizeValue = the value that you want to resize the image by (default = 1) (Range[0-1])

     Return the image cropped
    '''
    img = img[RowStart:RowEnd, ColumnStart:ColumnEnd]
    return img

def ImageSharpen(img,sigma = 1.3,show = False, ResizeValue = 1):
    '''
    -----------------------------------
    WARNING: This function is not working
    SEEMS TO JUST BLUR
    -----------------------------------
    # To sharpen an image

    - @img = the image that you want to sharpen
    - @sigma = the value of the sharpening (default = 1.3) (Range[0-5])

    Optional:
    - @show = if you want to show the image (default = False) [Doesnt Return the image, Doesnt save the image]
    - @ResizeValue = the value that you want to resize the image by (default = 1) (Range[0-1])

     Return the image sharpened
    '''
    img = cv2.GaussianBlur(img, (0, 0), sigma)
    img = cv2.addWeighted(img, 1.5, img, -0.5, 0)
    return img