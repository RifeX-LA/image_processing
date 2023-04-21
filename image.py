import cv2
import numpy as np
from matplotlib import pyplot as plt


def show_image(img):
    plt.imshow(img)
    plt.show()


def sharpen(img_filename):
    img = cv2.imread(img_filename, 0)
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened_img = cv2.filter2D(img, -1, kernel)
    stacked_images = np.hstack((img, sharpened_img))
    show_image(stacked_images)


def linear_contrast(img_filename):
    img = cv2.imread(img_filename, 0)
    contrast_img = 255 / (np.amax(img) - np.amin(img)) * (img - np.amin(img))
    stacked_images = np.hstack((img, contrast_img))
    show_image(stacked_images)


def histogram_equalization_rgb(img_filename):
    img = cv2.imread(img_filename, 0)
    result_img = cv2.equalizeHist(img)
    stacked_images = np.hstack((img, result_img))
    show_image(stacked_images)


def histogram_equalization_hsv(img_filename):
    img = cv2.imread(img_filename, cv2.COLOR_BGR2HSV)
    img[:, :, 0] = cv2.equalizeHist(img[:, :, 0])
    show_image(cv2.cvtColor(img, cv2.COLOR_HSV2BGR))
