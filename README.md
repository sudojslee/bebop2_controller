# Parrot Bebop2 Controller

Simple controller for Parrot Bebop2 

## Installation

##### Wifi connection
```
python3
pip install untangle
pip install zeroconf
pip install pyparrot
```

##### For BLE connection (only in Linux)
```
sudo apt-get install bluetooth
sudo apt-get install bluez
sudo apt-get install python-bluez
```

## Commands

#### For default value v = 20, d = 1
- v = percentage for roll, pitch, and yaw degrees
- d = duration for each command in seconds
```
python3 controller.py
```
#### For command line arguments
```
python3 controller.py -v 30 -d 2
```

#### Line 34, 35 in controller.py - manually change for safety
```
bebop.set_max_tilt(5)  			  # maximum allowable tilt in degrees: 5(very slow) ~ 30(very fast)
bebop.set_max_vertical_speed(1)   # maximum allowable vertical speed: 0.5 m/s ~ 2.5 m/s
```

### Key commands
* w/s: forward, backward
*  a/d: left, right
* q/e: left_yaw, right_yaw
* j/k: vertical_up, vertical_down
* o/p: takeoff, land

## References

* [https://github.com/amymcgovern/pyparrot](https://github.com/amymcgovern/pyparrot)
* [https://emissarydrones.com/what-is-roll-pitch-and-yaw](https://emissarydrones.com/what-is-roll-pitch-and-yaw)


