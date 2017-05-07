from subsystems import Drivetrain, StatusLight, Extinguisher
#from subsystems import SensorStick    # SEAS Innovation Challenge subsystems
from time import sleep

#import multiprocessing

#def worker():
#    print "Robot in running"
#    return

#p = multiprocessing.Process(target=worker)
#p.start()
#p.join()

# H-drive drivetrain
drivetrain = Drivetrain()
# sensor_stick = SensorStick()
status_light = StatusLight()
extinguisher = Extinguisher()

def drive_in_square():
    drivetrain.arcade_drive(1.0, 0.0, 0.0)
    sleep(1)
    drivetrain.arcade_drive(0.0, 0.0, 1.0)
    sleep(1)
    drivetrain.arcade_drive(-1.0, 0.0, 0.0)
    sleep(1)
    drivetrain.arcade_drive(0.0, 0.0, -1.0)
    sleep(1)

robot_on = False
found_flame = False
    
# Equivalent to Arduino loop() method
while (not (status_light.is_freq_start() or status_light.activation_switch_pressed())):
    pass
    
while (not extinguisher.has_flame()):
    # TODO: naviguess maze
    pass

drivetrain.stop()
extinguisher.on()

while (True):
    # TODO: extinguish code
    pass
