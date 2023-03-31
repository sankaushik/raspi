from picamera import PiCamera

camera = PiCamera()
camera.resolution = (2592,1944)
#camera.start_preview()

camera.capture('image.jpg')
camera.stop_preview()
print("Done")  
