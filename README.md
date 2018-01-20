# 2F Scanner Build Instructions <br />
## Chigozie Aham <br />
## Table of Contents<br />
<ol>
<li>Introduction</li>
<li>Items required</li>
<li>Installing Raspbian OS</li>
<li>Installing OpenCV and Python</li>
<li>Designing 2F Scanner:</li>
<li>Setting up V4L2 to enable video Recording</li>
<li>Facial detection</li>
<li>Train the images</li>
<li>Facial Recognition</li>
<li></li></ol>

### Introduction:<br />
2f Scanner is a device built with the Raspberry-pi 3 to perform the function of facial recognition for security purposes. It's an optional tool that could be used for biometric verification of a registered user in the android mobile application, GBMstats. OpenCV, which stands for Open Computer Vision, was utilized in performing facial detection and recognition. OpenCV is an open source library originally developed by Intel that contains functions focusing on real-time computer vision. For inclined technology students, It should take about 5-7 days to successfully complete these build instructions based on their commitment.<br />

### Items Required:<br />
•	Pi-camera<br />
•	Raspberry-pi<br />
•	HDMI adapter<br />
•	VGA – HDMI cable<br />
•	Laptop<br />
•	Monitor<br />
•	Mouse<br />
•	Keyboard<br />
•	MicroSD card<br />

### Installing Raspbian OS (Windows Users):<br />
•	Download the Raspbian image from the website. This would take a long while: https://www.raspberrypi.org/downloads/raspbian/ <br />
•	Download and install the SD card formatter for formatting the MicroSD card from: https://www.sdcard.org/downloads/formatter_4/ <br />
•	Download and install the Windows image file reader from: http://sourceforge.net/projects/win32diskimager/ <br />
•	Insert the MicroSD card into your Windows laptop, launch the SD Card Formatter and navigate to “Select Card”, choosing the right drive assigned to your MicroSD card, then “Quick Format” and Format the card. <br />
•	Launch the Win32 Disk Imager, choose the right ISO image file you downloaded and the right drive and select write. Wait a while and the ISO image file would be successfully written to your SD card. <br />
•	Next, insert the SD card into the raspberry pi. NOTE: Plug the keyboard, mouse and monitor into the raspberry pi first before powering it. <br />
•	Optionally, to use VNC viewer in controlling the raspberry pi remotely, you have to install VNC viewer on your laptop (https://www.realvnc.com/en/connect/download/viewer/). On your raspberry pi, navigate to the “Preferences”, and turn on the VNC. Next, launch the terminal on your raspberry-pi, use the command – ifconfig – to get your raspberry-pi IP address. After the VNC download is complete on your laptop, launch it. Navigate to the search box and enter your raspberry-pi IP address and hit the enter button. <br />

### Installing OpenCV and Python:<br />
•	Carefully follow the steps on the link: https://www.learnopencv.com/install-opencv3-on-ubuntu/ <br />

### Designing 2F Scanner<br />
The pi-camera is a really fragile technology, so a case was required to protect it. Using CorelDraw and accurate <a href="https://www.raspberrypi-spy.co.uk/2013/05/pi-camera-module-mechanical-dimensions/">schematics</a>, a design was produced. Find below a preview of the design and link to download CorelDraw and the schematic:<br/>
<img src="thumbnail.png" alt="2f scanner design">
<a href="https://www.coreldraw.com/en/pages/free-download/">CorelDraw</a>
<a href="https://github.com/goziethelegion/Legion/tree/master/Pi2CaseHumber">Schematics</a>

### Setting up V4L2 to enable video Recording<br />
The pi-camera is mainly designed for camera capture, so video recording is a quite complex. You would have to install V4L2 to enable video recording. Follow the steps below to successful install v4L2 and enable it. <br />

sudo apt-get install autoconf gettext libtool libjpeg62-dev<br />
cd v4l-utils<br />
autoreconf -vfi<br />
./configure<br />
make<br />
sudo make install<br />
 
sudo modprobe bcm2835-v4l2<br />

v4l2-ctl --overlay=1 # enable viewfinder<br />

v4l2-ctl --set-fmt-video=width=320,height=240,pixelformat=4<br />
v4l2-ctl --stream-mmap=3 --stream-count=100 --stream-to=somefile.264<br />

v4l2-ctl --set-fmt-video=width=320,height=240,pixelformat=3<br />
v4l2-ctl --stream-mmap=3 --stream-count=1 --stream-to=somefile.jpg<br />

v4l2-ctl --set-ctrl video_bitrate=10000000<br />

### Facial detection (Signing up user):<br />
•	Open up the terminal, navigate to the Home>pi>VideoCam directory.<br />
•	Run the datasetter.py <br />
	python datasetter.py<br />
•	A prompt message would appear asking for your name<br />
•	After you enter your username, a live video frame would appear on the computer screen, recording.<br />
•	Hold up 2f scanner to enable capture of your face.<br />
•	Look into the camera so the camera could easily detect your face<br />
•	Ensure the background lighting is good.<br />
•	Tilt your head back and forth (preferably around) to enable the camera to capture all your facial angles.<br />
•	The video frame would only exit when 20 images has been successfully captured and stored in the dataset folder. <br />
#### Relevant files and link:
<ul>
<a href="https://github.com/goziethelegion/Legion/blob/master/datasetter.py"><li>datasetter.py</li></a>
<li></li>
</ul>

### Train the images:<br />
•	Next, train the images captured in the dataset folder by running the program trainer.py – 	python trainer.py<br />

### Facial Recognition:<br />
•	Still in the same directory, run the program detector.py<br />
python detector.py<br />
•	Ensure the background lighting is good.<br />
•	Hold up 2f scanner to your face level and the camera should recognize your face with the name you entered on top of your picture frame.<br />

