# WiringPi2andRC433Mhz

Working on RasperryPi B Raspbian 2015.02 , maybe on other Rpis versions you should modify GPIO.

The python script allow to command a linux router (flashed with tomatousb, dd-wrt, ..) with ssh enabled to activade/desactivate wifi, reboot Rasperry pi, allow to reboot on other OS with berryboot

##Installation

1. Install Wiringpi 2 http://raspi.tv/how-to-install-wiringpi2-for-python-on-the-raspberry-pi
2. Install paramiko with pip install
3. 

##Configuring
1. Downlod or fork this code for your needs
2. Enter your informations like router ip id and password
3. edit crontab to launch the script at boot with sudo 
