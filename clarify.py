import cv2
import numpy as np


class clarify():

    def __init__(self, path=None, img=None, gray=None):
        # open file into image array or use image itself
        if img is None:
            if path is not None:
                if gray is not None:
                    self.img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                else:
                    self.img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
            else:
                raise Exception('You have to provide a path or image itself.')
        else:
            self.img = img

    # clear image.
    # mybb captcha.php seems make its color palette of string between 0 and 200.
    # anything above 200 is noise.
    # also completely black pixels in edges must filtered
    def clarify_img(self):
        (h, w) = self.img.shape[:2]
        for x in range(0, w):
            for y in range(0, h):
                if max(self.img[y][x]) > 200 or sum(self.img[y][x]) == 0:
                    self.img[y][x] = [255, 255, 255]

    # canny image, threshold values may need some tweak
    def canny(self):
        self.img = cv2.Canny(self.img, 400, 500)

    # RGB to GRAY
    def gray(self):
        self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)

    # clear and gray
    def clarify_and_gray(self):
        self.clarify_img()
        self.gray()

    # clear and canny
    def clarify_and_canny(self):
        self.clarify_img()
        self.canny()


if __name__ == "__main__":
    clr = clarify(path="test.png")
    clr.clarify_and_canny()
    img = clr.img
    cv2.imshow('clarified', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
