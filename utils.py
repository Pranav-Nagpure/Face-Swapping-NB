import numpy as np
from PIL import Image


def DisplayImages(images):
    h = 0
    w = 0
    for img in images:
        h = max(h, img.shape[0])
        w = w + img.shape[1]

    image = np.ones((h, w + 5 * (len(images) - 1), 3), np.uint8)

    w_offset = 0
    for img in images:
        image[:img.shape[0], w_offset:w_offset+img.shape[1], :] = img
        w_offset = w_offset + img.shape[1] + 5

    return Image.fromarray(image)
