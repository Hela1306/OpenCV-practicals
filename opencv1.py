import cv2 as cv

#READING IMAGES
img= cv.imread('C:\\Users\\ADMIN\\Desktop\\b\\Study\\code\\ml stuff\\opencv\\cat.jpg')
# cv.imshow('cat',img)
# cv.waitKey(0)

#VIDEO CAPTURING
capture = cv.VideoCapture('spidey gify.gif')#takes in argument either path of video or int value 0123 etc when webcam is used
while True: 
    isTrue, frame=capture.read()#we gramp the video frame by frame
    cv.imshow('Videos',frame)#display each frame of video

    # if cv.waitKey(10)& 0xFF==ord('d'):#if letter d is pressed then break out of the loop
    #     break
capture.release()
cv.destroyAllWindows(0)#you wait for a infinite amount of time for a key to be pressed

