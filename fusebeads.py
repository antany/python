import math;
from PIL import Image, ImageDraw

inputImage = Image.open("D:/image-convertor/input.jpg")

noOfHorizonPegs = 100
noOfVerticalPegs = 100
mulitplier = 50

availableColors = [
        (0,0,0),
        (255,255,255),
        (255,0,0),
        (206, 139, 115)
    ]

availableAllColors = [
        (0,0,0),
        (94, 200, 203),
        (241, 111, 171),
        (67, 171, 197),
        (192, 202, 221),
        (91, 200, 202),
        (199, 183, 216),
        (169, 182, 204),
        (74, 178, 212),
        (138, 22, 74),
        (60, 63, 72),
        (215, 235, 234),
        (237, 145, 178),
        (151, 207, 114),
        (168, 133, 210),
        (143, 143, 148),
        (30, 35, 41),
        (83, 92, 179),
        (104, 109, 117),
        (176, 203, 46),
        (172, 126, 203),
        (226, 221, 210),
        (52, 139, 169),
        (121, 86, 182),
        (144, 37, 42),
        (29, 161, 100),
        (164, 206, 216),
        (215, 176, 128),
        (20, 135, 48),
        (33, 64, 166),
        (89, 50, 38),
        (216, 39, 32),
        (245, 234, 163),
        (114, 210, 247),
        (221, 172, 123),
        (246, 81, 17),
        (32, 121, 203),
        (141, 74, 54),
        (237, 196, 7),
        (152, 207, 240),
        (224, 189, 182),
        (243, 110, 30),
        (22, 163, 230),
        (242, 198, 40),
        (189, 218, 226),
        (237, 144, 111),
        (255, 193, 110),
        (33, 146, 201),
        (219, 42, 31),
        (255,255,255)
    ]



def findNearastColor(actualColor):
    r,g,b = actualColor
    color_diffs = []
    for color in availableColors:
        cr, cg, cb = color
        color_diff = math.sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1] 


resizedImage = inputImage.convert('RGB').resize((noOfHorizonPegs, noOfVerticalPegs))

generatedImage = Image.new("RGB", (noOfHorizonPegs * mulitplier, noOfVerticalPegs * mulitplier))

drawableImage = ImageDraw.Draw(generatedImage)

shape = [(0, 0),(noOfHorizonPegs * mulitplier, noOfVerticalPegs * mulitplier)] 

drawableImage.rectangle(shape, fill="#FFFFFF", outline="#000000", width=1)

for i in range(0,noOfVerticalPegs,1):
    for j in range(0,noOfHorizonPegs,1):
        shape = [(j*mulitplier, i*mulitplier),(noOfHorizonPegs * mulitplier, noOfVerticalPegs * mulitplier)] 
        actualColr = resizedImage.getpixel((j,i))
        color = findNearastColor(actualColr)
        print(color)
        #color = actualColr
        fill = '#'+"{:02x}".format(color[0],'x')+"{:02x}".format(color[1],'x')+"{:02x}".format(color[2],'x')
        drawableImage.rectangle(shape, fill=fill, outline="#000000", width=1)
           

generatedImage.show()
generatedImage.save("d:/image-convertor/output.png")
