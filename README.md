# projector_V01

This project runs on a Raspberry Pi V3
https://shop.mchobby.be/raspberry-pi-3/819-raspberry-pi-3-de-stock--3232100008199.html


NB:
Edit fstab to add external storage

sudo nano /etc/fstab

//192.168.2.10/Photobooth       /home/pi/mnt/Photobooth cifs    auto,user=pi,password=azertyuiop,_netdev        0       0
//192.168.2.10/PiShare          /home/pi/mnt/drive_ext  cifs    auto,user=pi,password=azertyuiop,_netdev        0       0
