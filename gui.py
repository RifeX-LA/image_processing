import os.path
import tkinter as tk
from tkinter import filedialog as fd
import image


class ImageProcessor:
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title('Image processing')
        self.__root.resizable(False, False)
        self.__root.geometry('300x150')

        self.__handlers = [image.sharpen, image.linear_contrast, image.histogram_equalization_rgb, image.histogram_equalization_hsv]

        fd_button = tk.Button(self.__root, text='Open a file', command=self.process_image)
        fd_button.pack()

    def process_image(self):
        filetypes = (('All files', '*.*'), ('text files', '*.txt'))
        filename = fd.askopenfilename(title='Open a file', initialdir=os.path.curdir, filetypes=filetypes)

        for handler in self.__handlers:
            handler(filename)

    def mainloop(self):
        self.__root.mainloop()
