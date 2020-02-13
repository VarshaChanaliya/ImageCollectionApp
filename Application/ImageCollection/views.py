from django.shortcuts import render
import cv2
import os
from django.contrib import messages


def index(request):
    return render(request,'index.html')


def submit(request):
    name = request.POST.get('name', None)
    if name is not None:
        CaptureImage(name)
    else:
        messages.warning(request,"Please Enter your name and try again!")
    return render(request, 'index.html')


def CaptureImage(name):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    path = 'ImageFiles/{}'.format(name)
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    img_counter = 0
    while True:
        ret, frame = cam.read()
        cv2.imshow("Image", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k % 256 == 27:
            break
        elif k % 256 == 32:
            img_name = "{}/{}_{}.jpg".format(path,name,img_counter)
            cv2.imwrite(img_name, frame)
            print("{} Saved!".format(img_name))
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()

