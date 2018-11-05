import sys, termios, tty, os, time, argparse

from pyparrot.Bebop import Bebop

parser = argparse.ArgumentParser(description='Set parameters for Parrot Bebop2')
parser.add_argument('-v', type = int, default = 20, help ='variable for roll, pitch, yaw')
parser.add_argument('-d', type = int, default = 2, help ='duration for each key press')

args = parser.parse_args()
percentage = args.v
duration_s = args.d

bebop = Bebop(drone_type="Bebop2")

print("Connecting Bebop2 with percentage: {}, duration: {}".format(percentage, duration_s))
success = bebop.connect(10)
print(success)
print(bebop.sensors.battery)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

if (success):

	bebop.ask_for_state_update()
	# set safe parameters
	bebop.set_max_tilt(15)  # maximum allowable tilt in degrees: 5(very slow) ~ 30(very fast)
	bebop.set_max_vertical_speed(1)   # maximum allowable vertical speed: 0.5 m/s ~ 2.5 m/s


	while True:
		char = getch()

		if (char == "w"):
			print("forward")
			bebop.fly_direct(roll=0, pitch=percentage, yaw=0, vertical_movement=0, duration=duration_s)
			bebop.flat_trim()
		elif (char == "a"):
			print("left")
			bebop.fly_direct(roll=-percentage, pitch=0, yaw=0, vertical_movement=0, duration=duration_s)
			bebop.flat_trim()
		elif (char == "s"):
			print("backward")
			bebop.fly_direct(roll=0, pitch=-percentage, yaw=0, vertical_movement=0, duration=duration_s)
			bebop.flat_trim()
		elif (char == "d"):
			print("right")
			bebop.fly_direct(roll=percentage, pitch=0, yaw=0, vertical_movement=0, duration=duration_s)
			bebop.flat_trim()
		elif (char == "j"):
			print("up")
			bebop.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=percentage, duration=duration_s)
			bebop.flat_trim()
		elif (char == "k"):
			print("down")
			bebop.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-percentage, duration=duration_s)
			bebop.flat_trim()
		elif (char == "q"):
			print("left yaw")
			bebop.fly_direct(roll=0, pitch=0, yaw=-percentage, vertical_movement=0, duration=duration_s)
			bebop.flat_trim()
		elif (char == "e"):
			print("right yaw")
			bebop.fly_direct(roll=0, pitch=0, yaw=percentage, vertical_movement=0, duration=duration_s)
			bebop.flat_trim()
		elif (char == "o"):
			print("takeoff")
			bebop.safe_takeoff(10)
		elif (char == "p"):
			print("land")
			bebop.safe_land(10)
			bebop.smart_sleep(5)
			bebop.disconnect()
			break
		else:
			bebop.flat_trim()
			bebop.smart_sleep(5)

		# bebop.ask_for_state_update()

