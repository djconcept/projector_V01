# projector_V01


Edit fstab to add external storage

sudo nano /etc/fstab

//192.168.2.10/Photobooth       /home/pi/mnt/Photobooth cifs    auto,user=pi,password=azertyuiop,_netdev        0       0
//192.168.2.10/PiShare          /home/pi/mnt/drive_ext  cifs    auto,user=pi,password=azertyuiop,_netdev        0       0
