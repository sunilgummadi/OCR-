import cv2
def grayimage():
    image = cv2.imread("s.png")
    GRAY_IMAGE=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    GRAY_IMAGE=cv2.medianBlur(GRAY_IMAGE,3)
    return GRAY_IMAGE

