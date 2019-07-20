#Task1
def lighten(image):
    '''
    Gery scale of the image is incrsead by 10% 
    returns wether the image brunout after lightening
    '''
    from PIL import Image
    image = image.convert('L')
    xsize,ysize = image.size
    for x in range(xsize):
        for y in range(ysize):
            pixel = image.getpixel((x,y))
            if pixel*1.1>255:
                return True
    return False

#Task2
def flip(image):
    '''flip an image left to right'''
    from PIL import Image
    import copy
    coimage = copy.deepcopy(image)
    xsize, ysize = image.size
    slice_list=[]
    for i in range(xsize):
        slice_list.append(image.crop((i, 0, i+1, ysize)))
    for i,v in enumerate(slice_list):
        v.load()
        coimage.paste(v,(xsize-i-1,0,xsize-i,ysize))
    return coimage

#Task3
def clip(image,MaxVal):
    '''
    Limit each pixel to MaxVal
    '''
    from PIL import Image
    import numpy as np
    matirx = np.array(image.convert('L'))
    for i,x in enumerate(matirx):
        for j,y in enumerate(x):
            if y > MaxVal:
                matirx[i][j] = MaxVal
    new_image = Image.fromarray(matirx.astype(np.uint8))
    return new_image

if __name__ == "__main__":
#eample.jpg required
    from PIL import Image
    im = Image.open('example.jpg')
    o1 = flip(im)
    o2 = clip(im,int(input('Please input a integer parameter:')))
    print(lighten(im))
    o1.show()
    o2.show()