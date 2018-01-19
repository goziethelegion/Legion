# Legion
#2F Scanner Build Instructions
#Chigozie Aham – N01111181
#Items Required:
#•	Pi-camera
•	Raspberry-pi
•	HDMI adapter
•	VGA – HDMI cable
•	Laptop
•	Monitor
•	Mouse
•	Keyboard
•	MicroSD card

Installing Raspbian OS (Windows Users):
•	Download the Raspbian image from the website. This would take a long while: https://www.raspberrypi.org/downloads/raspbian/
•	Download and install the SD card formatter for formatting the MicroSD card from: https://www.sdcard.org/downloads/formatter_4/
•	Download and install the Windows image file reader from: http://sourceforge.net/projects/win32diskimager/ 
•	Insert the MicroSD card into your Windows laptop, launch the SD Card Formatter and navigate to “Select Card”, choosing the right drive assigned to your MicroSD card, then “Quick Format” and Format the card. 
•	Launch the Win32 Disk Imager, choose the right ISO image file you downloaded and the right drive and select write. Wait a while and the ISO image file would be successfully written to your SD card.
•	Next, insert the SD card into the raspberry pi. NOTE: Plug the keyboard, mouse and monitor into the raspberry pi first before powering it. 
•	Optionally, to use VNC viewer in controlling the raspberry pi remotely, you have to install VNC viewer on your laptop (https://www.realvnc.com/en/connect/download/viewer/). On your raspberry pi, navigate to the “Preferences”, and turn on the VNC. Next, launch the terminal on your raspberry-pi, use the command – ifconfig – to get your raspberry-pi IP address. After the VNC download is complete on your laptop, launch it. Navigate to the search box and enter your raspberry-pi IP address and hit the enter button. 

Installing OpenCV and Python:
•	Carefully follow the steps on the link: https://www.learnopencv.com/install-opencv3-on-ubuntu/

Setting up V4L2 to enable video Recording
The pi-camera is mainly designed for camera capture, so video recording is a quite complex. You would have to install V4L2 to enable video recording. Follow the steps below to successful install v4L2 and enable it. 

sudo apt-get install autoconf gettext libtool libjpeg62-dev
cd v4l-utils
autoreconf -vfi
./configure
make
sudo make install
 
sudo modprobe bcm2835-v4l2

v4l2-ctl --overlay=1 # enable viewfinder

v4l2-ctl --set-fmt-video=width=320,height=240,pixelformat=4
v4l2-ctl --stream-mmap=3 --stream-count=100 --stream-to=somefile.264

v4l2-ctl --set-fmt-video=width=320,height=240,pixelformat=3
v4l2-ctl --stream-mmap=3 --stream-count=1 --stream-to=somefile.jpg

v4l2-ctl --set-ctrl video_bitrate=10000000

Facial detection (Signing up user):
•	Open up the terminal, navigate to the Home>pi>VideoCam directory.
•	Run the datasetter.py 
	python datasetter.py
•	A prompt message would appear asking for your name
•	After you enter your username, a live video frame would appear on the computer screen, recording.
•	Hold up 2f scanner to enable capture of your face.
•	Look into the camera so the camera could easily detect your face
•	Ensure the background lighting is good.
•	Tilt your head back and forth (preferably around) to enable the camera to capture all your facial angles.
•	The video frame would only exit when 20 images has been successfully captured and stored in the dataset folder. 

Train the images:
•	Next, train the images captured in the dataset folder by running the program trainer.py – 	python trainer.py

Facial Recognition:
•	Still in the same directory, run the program detector.py
python detector.py
•	Ensure the background lighting is good.
•	Hold up 2f scanner to your face level and the camera should recognize your face with the name you entered on top of your picture frame.

