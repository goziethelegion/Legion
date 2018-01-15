import cv2

detector=cv2.CascadeClassifier('/home/pi/VideoCam/haarcascades/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

Id=raw_input('enter your id: ')
sampleNum=0
while(True):
    ret, img1 = cam.read()
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,0),2)
        
        #incrementing sample number 
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        cv2.imwrite("/home/pi/VideoCam/dataSet/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('frame1',img1)
    #wait for 100 miliseconds 
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    elif sampleNum>20:
        break
cam.release()
cv2.destroyAllWindows()