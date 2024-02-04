"""naopy controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Keyboard, Motion

timestep = 32

robot = Robot()

keyboard = Keyboard()
keyboard.enable(timestep)


# create the Robot instance.
class Nao (Robot):
    PHALANX_MAX = 8
   
    forwards = Motion('../../motions/Forwards50.motion')
    backwards = Motion('../../motions/Backwards.motion')
    sideStepLeft = Motion('../../motions/SideStepLeft.motion')
    sideStepRight = Motion('../../motions/SideStepRight.motion')
    
    def printMessages():
        print('up for forward')
        print('down for backward')
        print('left for left')
        print('right for right')
    def startMotion(motion):
        motion.play()
        
    key = -1
    printMessages()
    
    while robot.step(timestep) != -1:
        key= keyboard.getKey()
        if key == Keyboard.LEFT:
            startMotion(sideStepLeft)
        if key == Keyboard.RIGHT:
            startMotion(sideStepRight)
        if key == Keyboard.UP:
            startMotion(forwards)
        if key == Keyboard.DOWN:
            startMotion(backwards)
      