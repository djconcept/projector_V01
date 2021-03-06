#!/usr/bin/env python

# configure these settings to change projector behavior
server_mount_path = '//192.168.2.10/PiShare' # shared folder on other pi
#server_mount_path = '//PHOTOBOOTHALPHA/PiShare' # shared folder on other pi
user_name = 'pi' # shared drive login user name
user_password = 'azertyuiop' # shared drive login password
client_mount_path = '/home/pi/mnt/drive_ext' # where to find the shared folder on this pi
pics_folder = '/home/pi/mnt/drive_ext/pics_w' # where to find the pics to display
pics_folder_client = '/home/pi/mnt/drive_ext/screen' # where to find the pics to display
tumblr_folder = '/home/pi/mnt/drive_ext/tumblr' # where to find the pics to display

# configure these settings to change projector behavior
photobooth_mount_path = '//192.168.2.10/Photobooth' # shared folder on other pi
#photobooth_mount_path = '//PHOTOBOOTHALPHA/Photobooth' # shared folder on other pi
photobooth_user_name = 'pi' # shared drive login user name
photobooth_user_password = 'azertyuiop' # shared drive login password
photobooth_client_mount_path = '/home/pi/mnt/Photobooth' # where to find the shared folder on this pi
photobooth_pics_folder = '/home/pi/mnt/Photobooth/images' # where to find the pics to display

waittime = 3  # default time to wait between images (in seconds)
use_prime = True # Set to true to show the prime slide, false if otherwise
waiting_slide = '/home/pi/mnt/Photobooth/images/projector_waiting.png' # image to show regularly in slideshow
prime_slide = '/home/pi/mnt/Photobooth/images/findshare.png' # image to show regularly in slideshow
prime_freq = 7 # how many pics to show before showing the prime slide again
#monitor_w = 1280#800 # width in pixels of display (monitor or projector)
#monitor_h = 1024#600 # height in pixels of display (monitor or projector)
title = "SlideShow"  # caption of the window...
