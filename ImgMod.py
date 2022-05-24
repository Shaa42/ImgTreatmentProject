from PIL import Image, ImageTk
import random as rd
import copy as cp

class IMAGE_TREAT:

    def __init__(self, _image):
        try:
            self._image = Image.open(_image)
            self._copy = cp.copy(self._image)
            self.width, self.height = self._image.size
        except:
            print("Error")
        
    def show(self):
        self._image.show()

    def grayscale(self):
        for x in range(self.width):
            for y in range(self.height):
                _pixel = self._image.getpixel((x, y))
                _moyenne = int((_pixel[0] + _pixel[1] + _pixel[2]) / 3)
                self._image.putpixel((x, y), ((_moyenne,) * 3))

        self._image.show()
        self._image = cp.copy(self._copy)

    def randomSubstract(self):       
        _rdList = [0, 1, 2]
        rd.shuffle(_rdList)
        for x in range(self.width):
            for y in range(self.height):
                _pixel = self._image.getpixel((x, y))
                self._image.putpixel((x, y), (_pixel[_rdList[0]-1] - _pixel[_rdList[0]], 
                                              _pixel[_rdList[1]-1] - _pixel[_rdList[1]],
                                              _pixel[_rdList[2]-1] - _pixel[_rdList[2]]))
        self._image.show()
        self._image = cp.copy(self._copy)

    def randomIndex(self):
        _rdList = [0, 1, 2]
        rd.shuffle(_rdList)
        for x in range(self.width):
            for y in range(self.height):
                _pixel = self._image.getpixel((x, y))
                self._image.putpixel((x,y), (_pixel[_rdList[0]], _pixel[_rdList[1]], _pixel[_rdList[2]]))
        self._image.show()
        self._image = cp.copy(self._copy)

    def rotate(self):
        _transposed = self._image.transpose(Image.ROTATE_90)
        _transposed.show()
        self._image = cp.copy(self._copy)


    def negative(self):
        for x in range(self.width):
            for y in range(self.height):
                _pixel = self._image.getpixel((x, y))
                self._image.putpixel((x, y), (255 - _pixel[0], 255 - _pixel[1], 255 - _pixel[2]))
        self._image.show()
        self._image = cp.copy(self._copy)
