import cv2 as cv
#RESCALING FUNCTION
def rescaleframe(frame,scale=0.75):
    #will work for images, videos and live videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)
#CHANGING RESOLUTION
def changeRes(width,height):
    #ONLY for live video
    capture(3,width)
    capture(4,height)
img= cv.imread(r'assests\dog.jpg')
#rescaling img
resized_img = rescaleframe(img,scale = 0.2)
cv.imshow('dog',resized_img)
cv.waitKey(0)
#VIDEO CAPTURING
capture = cv.VideoCapture(r'assests\dog_vid.mp4')#takes in argument either path of video or int value 0123 etc when webcam is used
while True: 
    isTrue, frame = capture.read()#we gramp the video frame by frame

    if not isTrue:
        break  # Break the loop if there are no more frames

    frame_resized = rescaleframe(frame, scale = 0.2)#rescaled vid
    cv.imshow('Videos',frame)#display each frame of video
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(1)& 0xFF == ord('d'):#if letter d is pressed then break out of the loop
        break
capture.release()
cv.destroyAllWindows()#you wait for a infinite amount of time for a key to be pressed
