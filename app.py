import os
import sys

from PIL import Image

EXTS = (
    '.jpg', 
    '.png',
    '.jpeg'
    )

# padding for pasting
padding_x = 0
padding_y = 0

if len(sys.argv) < 3:
    print(
        'Usage: watermark.py \'image folder path\' \'logo path\' [topleft, topright, bottomleft, bottomright, center]')
    sys.exit()
elif len(sys.argv) == 4:
    path = sys.argv[1]
    lgo = sys.argv[2]
    pos = sys.argv[3]
elif len(sys.argv) == 5:
    path = sys.argv[1]
    lgo = sys.argv[2]
    pos = sys.argv[3]
    padding_x = sys.argv[4]
    padding_y = sys.argv[4]
elif len(sys.argv) == 6:
    path = sys.argv[1]
    lgo = sys.argv[2]
    pos = sys.argv[3]
    padding_x = sys.argv[4]
    padding_y = sys.argv[5]
else:
    path = sys.argv[1]
    lgo = sys.argv[2]

logo = Image.open(lgo)
# double the logo size
logo = logo.resize((logo.size[0] * 2, logo.size[1] * 2), Image.ANTIALIAS)
logoWidth = logo.width
logoHeight = logo.height



for filename in os.listdir(path):
    if any([filename.lower().endswith(ext) for ext in EXTS]) and filename != lgo:
        image = Image.open(path + '/' + filename)
        imageWidth = image.width
        imageHeight = image.height

        try:
            if pos == 'topleft':
                image.paste(logo, (
                    padding_x,
                    padding_y,
                ), logo)
            elif pos == 'topright':
                image.paste(logo, (
                    imageWidth - logoWidth - padding_x,
                    padding_y,
                ), logo)
            elif pos == 'bottomleft':
                image.paste(logo, (
                    padding_x,
                    imageHeight - logoHeight - padding_y,
                ), logo)
            elif pos == 'bottomright':
                image.paste(logo, (
                    imageWidth - logoWidth - padding_x,
                    imageHeight - logoHeight - padding_y,
                ), logo)
            elif pos == 'center':
                image.paste(logo, ((imageWidth - logoWidth)/2,
                            (imageHeight - logoHeight)/2), logo)
            else:
                print('Error: ' + pos + ' is not a valid position')

            image.save(path + '/' + filename)
            print('Added watermark to ' + path + '/' + filename)

        except:
            image.paste(logo, ((imageWidth - logoWidth)/2,
                        (imageHeight - logoHeight)/2), logo)
            image.save(path + '/' + filename)
            print('Added default watermark to ' + path + '/' + filename)
