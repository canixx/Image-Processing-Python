import cv2

class ReadImage:
    def __init__(self, file):
        self.file = file

    def implement(self):
        return cv2.imread(self.file)

class ShowImage(ReadImage):
    def implement(self):
        image1 = ReadImage.implement(self)
        image2 = ReadImage.implement(self)
        images = cv2.hconcat([image1, image2])
        cv2.imshow("Images", images)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

image1 = ShowImage("rainbow1.jpeg")
image1.implement()

image2 = ShowImage("rainbowgray.jpeg")
image2.implement()
