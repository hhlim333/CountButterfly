import torch
import cv2
# Model
model = torch.hub.load('ultralytics/yolov5','custom', 'last.pt')  # yolov5n - yolov5x6 official model
#                                            'custom', 'path/to/best.pt')  # custom model

# Images
cv2.namedWindow("IMG")
#im = 'Lots of Butterfly Flying in Flowers Garden _ How Butterflies Pollinate Flowers..mp4'  # or file, Path, URL, PIL, OpenCV, numpy, list
cap=cv2.VideoCapture("Lots of Butterfly Flying in Flowers Garden _ How Butterflies Pollinate Flowers..mp4")
size=416

count=0

x,y,w,h = 0,0,400,250
while True:
    ret,img=cap.read()

    count += 1
    if count % 4 != 0:
        continue
    #img=cv2.resize(img,(600,500))
    results=model(img,size)
    #print(len(results.pandas().xyxy[0].index))
    for index , row in results.pandas().xyxy[0].iterrows():
        #print(index)
        x1 = int(row['xmin'])
        y1 = int(row['ymin'])
        x2 = int(row['xmax'])
        y2 = int(row['ymax'])
        n=(row['name'])
        if 'butterfly' in n:
            #points.append([x1,y1,x2,y2])
            cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),2)
            cv2.putText(img,str(n),(x1,y1),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
            cv2.putText(img,str(index+1),(x2,y1),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
        #cv2.rectangle(img, (x,x), (x + w, y + h), (0,0,0), -1)
        #cv2.putText(img=img, text="CAT",org=(x + int(w/10),y + int(h/1.5)), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=4, color=(255,0,0), thickness=7)
    cv2.putText(img, "Number of Butterfly: "+str(len(results.pandas().xyxy[0].index)), (5, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
        #cv2.putText(img,str(len(results.pandas().xyxy[0].index)),(0,0),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
    cv2.imshow('IMG',img)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()