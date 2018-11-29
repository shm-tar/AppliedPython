import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as imp
from PIL import Image, ImageDraw

image = imp.imread('IMG_4141.jpg')


def plotting(im, **kwargs):
    plt.imshow(im, interpolation="none", **kwargs)
    plt.show()


plotting(image)


def rgb_split(im):

    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    for c, ax in zip(range(3), axs):
        tmp_im = np.zeros(im.shape, dtype="uint8")
        tmp_im[:, :, c] = im[:, :, c]
        ax.imshow(tmp_im)

    plt.show()


rgb_split(image)


def greyscale(im):
    plt.imshow(np.dot(im[..., :3], [0.33, 0.33, 0.33]), cmap='gray')
    plt.show()


def contrast(im):
    image = Image.open("IMG_4141.jpg")
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    factor = 33
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0] + factor
            b = pix[i, j][1] + factor
            c = pix[i, j][2] + factor
            if (a < 0):
                a = 0
            if (b < 0):
                b = 0
            if (c < 0):
                c = 0
            if (a > 255):
                a = 255
            if (b > 255):
                b = 255
            if (c > 255):
                c = 255
            draw.point((i, j), (a, b, c))

    plt.imshow(image)
    plt.show()
    # image.save("ans.jpg", "JPEG")
    del draw

greyscale(image)

contrast(image)
