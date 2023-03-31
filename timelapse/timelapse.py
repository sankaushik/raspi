from picamera import PiCamera
import os
import datetime
from time import sleep

#import pdb; pdb.set_trace()

tlminutes = 1 #set this to the number of minutes you wish to run your timelapse camera
secondsinterval = 2 #number of seconds delay between each photo taken
fps = 30 #frames per second timelapse video
numphotos = int((tlminutes*60)/secondsinterval) #number of photos to take
print("number of photos to take = ", numphotos)

dateraw= datetime.datetime.now()
datetimeformat = dateraw.strftime("%Y_%m_%d_%H%M")
print("RPi started taking photos for your timelapse at: " + datetimeformat)

camera = PiCamera()
camera.resolution = (2048, 1082)
camera.led= False

#system('rm /home/pi/Pictures/*.jpg') #delete all photos in the Pictures folder before timelapse start

out_dir = os.path.join('/home/skpi/Pictures',datetimeformat)
os.makedirs(out_dir)

for i in range(numphotos):
    im_fname = os.path.join(out_dir,'image{0:06d}.jpg'.format(i))
    camera.capture(im_fname)
    sleep(secondsinterval)
print("Done taking photos.")
#print("Please standby as your timelapse video is created.")
dateraw= datetime.datetime.now()
datetimeformat = dateraw.strftime("%Y_%m_%d_%H%M")
print("RPi stopped taking photos for your timelapse at: " + datetimeformat)


#system('ffmpeg -r {} -f image2 -s 1024x768 -nostats -loglevel 0 -pattern_type glob -i "/home/pi/Pictures/*.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p /home/pi/Videos/{}.mp4'.format(fps, datetimeformat))
#system('rm /home/pi/Pictures/*.jpg')
#print('Timelapse video is complete. Video saved as /home/pi/Videos/{}.mp4'.format(datetimeformat))
