import cv2

'''

All the functions in this file are used to apply filters to an image
The functions are:
    - Water
    - OilPainting
    - BlackAndWhite
    - GrayScale
    - Blur  


    # under construction
    - PencilSketch
    - StyleTransfer
    - Cartoon

All the Customization fields are optional and usually between 0 and 100

'''

def OilPainting(img, size = 5, levels = 10 , show = False, ResizeValue = 1):
    '''
    # To apply oil painting effect to an image

    - @img = the image that you want to apply the effect on
    optional:
    - @size = the size of the effect (default = 5)
    - @levels = the levels of the effect (default = 10)
    - @show = if you want to show the image (default = False) [Doesnt Return the image, Doesnt save the image]
    - @ResizeValue = the ResizeValue of the effect (default = 1) [Resize the image to the original size]

     Return the image with the effect applied
    '''
    
    size = int(size)
    levels = int(levels)
    
    img = cv2.xphoto.oilPainting(img, size, levels)
    #q: whats the range of the size and levels
    #a:

 
    return img

def PencilSketch(img, FilterSize = 60, Range = 70, shade_factor = 0.05, show = False):
    '''
    -------------------------------------------------------
    WARNING: Doesnt Work Yet
    -------------------------------------------------------

    # To apply pencil sketch effect to an image

    - @img = the image that you want to apply the effect on

    optional:
    - @FilterSize = the FilterSize of the effect (default = 60)
    
    - @Range = the Range of the effect (default = 0.07) \n\t[Range of the Gaussian filter, which is a measure of how much noise will be removed.The larger the value, the more noise will be removed. But too large value will also remove image details, \n\tso it should be tuned for each image]
    
    - @shade_factor = the shade_factor of the effect (default = 0.05)

    - @show = if you want to show the image (default = False) [Doesnt Return the image, Doesnt save the image]

     Return the image with the effect applied
    '''

    # fixing range value
    range = range/1000

    imgGray,imgColor = cv2.pencilSketch(img, FilterSize, Range, shade_factor)
    if show:
        showImg(imgColor)
    else:
        return imgGray

def Cartoon(img, FilterSize = 5, CartoonMode = 0, ColorMode = 0, EdgeThreshold = 10, MaxEdgeThreshold = 100 ,show = False):
    '''
    --------------------------------------------------------------
    WARNING: Doesnt Work Yet
    --------------------------------------------------------------

    To apply cartoon effect to an image

    - @img = the image that you want to apply the effect on
    optional:
    - @FilterSize = the FilterSize of the effect (default = 5)
    - @CartoonMode = the CartoonMode of the effect (default = 0)
    - @ColorMode = the ColorMode of the effect (default = 0)
    - @EdgeThreshold = the EdgeThreshold of the effect (default = 10)
    - @MaxEdgeThreshold = the MaxEdgeThreshold of the effect (default = 100)
    - @show = if you want to show the image (default = False) [Doesnt Return the image, Doesnt save the image]

     Return the image with the effect applied
    '''
    img = cv2.cartoon(img, FilterSize, CartoonMode, ColorMode, EdgeThreshold, MaxEdgeThreshold)
    if show:
        showImg(img)
    else:
        return img

def StyleTransfer(img, model = 'models/instance_norm/udnie.t7' ,show = False):
    '''
    --------------------------------------------------------------
    WARNING: this function has not been tested yet
    --------------------------------------------------------------
    To apply style transfer effect to an image

    - @img = the image that you want to apply the effect on
    
    optional:
    - @model = the model of the effect (default = 'models/instance_norm/udnie.t7')
    - @show = if you want to show the image (default = False) [Doesnt Return the image, Doesnt save the image]

     Return the image with the effect applied
    '''
    img = cv2.colorConstancy(img, model)
    if show:
        showImg(img)
    else:
        return img 

def Water(img, NeighbourhoodSize = 60, Range = 4, show = False, ResizeValue = 1):
    '''
    # To apply WaterColor effect to an image

    - @img = the image that you want to apply the effect on
    optional:
    - @NeighbourhoodSize = the NeighbourhoodSize of the effect (default = 60) (Range[1-255])
    - @Range = the Range of the effect (default = 0.4) (Range[0-1])
    - @show = if you want to show the image (default = False) [Doesnt Return the image, Doesnt save the image]
    - @ResizeValue = the ResizeValue of the effect (default = 1) [Resize the image to the original size]

     Return the image with the effect applied
    '''

    NeighbourhoodSize = int(NeighbourhoodSize)
    Range = float(Range)
    # fixing range value
    Range = Range/10

    img = cv2.stylization(img, NeighbourhoodSize, Range)

    return img

def BlackAndWhite(img,show = False, ResizeValue = 1):
    '''
    # To apply Black and White effect to an image

    - @img = the image that you want to apply the effect on
    optional:
    - @show = if you want to show the image (default = False) [Doesnt Return the image, Doesnt save the image]
    - @ResizeValue = the ResizeValue of the effect (default = 1) [Resize the image to the original size]

     Return the image with the effect applied
    '''
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


    return img

def GrayScale(img,show = False, ResizeValue = 1):
    '''
    # To make an image gray scale

    - @img = the image that you want to make gray scale

    Optional:
    - @show = if you want to show the image (default = False) [Doesnt Return the image, Doesnt save the image]
    - @ResizeValue = the value that you want to resize the image by (default = 1) (Range[0-1])

     Return the image gray scaled
    '''
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return img

def ImageBlur(img,show=False,ResizeValue=1):
    '''
    # To blur an image

    - @img = the image that you want to blur

    Optional:
    - @show = if you want to show the image (default = False) [Doesnt Return the image, Doesnt save the image]
    - @ResizeValue = the value that you want to resize the image by (default = 1) (Range[0-1])

     Return the image blurred
    '''
    img = cv2.blur(img,(5,5))

    return img

