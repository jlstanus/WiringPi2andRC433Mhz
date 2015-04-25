# 4 bouttons pour couper/allumer le wifi 2.4 et 5 ghz

import wiringpi2 as wiringpi
import paramiko  
import sys
import select
from time import sleep       # allows us a time delay  
wiringpi.wiringPiSetupGpio()  
wiringpi.pinMode(27, 0)      # sets GPIO 27 to input  
cmd1 = "wl radio off"
cmd2 = "wl radio on"
cmd3 = "wl -i eth2 radio off"
cmd4 = "wl -i eth2 radio on"
host = '192.168.1.1' 
portR = 69 
utilisateur = 'root'
mdp = "coucou"
timer = 0

 
try:  
	while True:  
		if wiringpi.digitalRead(27):     # If button on GPIO27 pressed 
			print "Boutton B"  
			print "Connection ssh en cours"  
			ssh = paramiko.SSHClient()     #loading SSH client
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(host, port=portR, username=utilisateur, password=mdp, look_for_keys=True) #connection to tomatousb router
			sleep(2)
			print "Connected"
			ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd1)
			print "Wifi 2.4 Ghz desactivated"
			sleep(1)
			ssh.close() 
			print "Connection closed"
 
		elif wiringpi.digitalRead(2):     # If button on GPIO02 pressed  
			print "Boutton C"
			print "Connection ssh en cours"  
			ssh = paramiko.SSHClient()     #loading SSH client
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(host, port=portR, username=utilisateur, password=mdp, look_for_keys=True) #connection to tomatousb router
			sleep(2)
			print "Connected"
			ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd4)
			print "Wifi 5 Ghz activated"
			sleep(1)
			ssh.close() 
			print "Connection closed"

		elif wiringpi.digitalRead(17):     # If button on GPIO17 pressed   
			print "Boutton D"
			print "Connection ssh en cours"			
			ssh = paramiko.SSHClient()     #loading SSH client
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(host, port=portR, username=utilisateur, password=mdp, look_for_keys=True) #connection to tomatousb router
			sleep(2)
			print "Connected"
			ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd3)
			print "Wifi 5 Ghz desactivated"
			sleep(1)
			ssh.close() 
			print "Connection closed"

		elif wiringpi.digitalRead(22):     # If button on GPIO22 pressed   
			print "Boutton A"
			print "Connection ssh en cours"                                               
			ssh = paramiko.SSHClient()     #loading SSH client
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(host, port=portR, username=utilisateur, password=mdp, look_for_keys=True) #connection to tomatousb router
			sleep(2) 
			print "Connected"
			ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd2)
			print "Wifi 2.4 Ghz activated"
			sleep(1)
			ssh.close()
			print "Connection closed"
			

		else:  
			print "Waiting something happens...."  # waiting button pressed  
		sleep(0.4)                      # delay
finally:
	print "bye"
