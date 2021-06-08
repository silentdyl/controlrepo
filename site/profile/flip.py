    assert type(vertical) == bool
    
    from PIL import Image as CoreImage

    img = CoreImage.open(image)
    print(('Loading ' + repr(image)),end='',flush=True)
    im = CoreImage.load()
    #im = image.convert("RGBA",image)
    width  = im.size[0]
    height = im.size[1]
    
    if vertical == False:
        img = im.transpose(method=PIL.CoreImage.FLIP_TOP_BOTTOM)
        img.save(im)
    else:
        img = im.transpose(method=PIL.CoreImage.FLIP_LEFT_RIGHT)
        img.save(im)