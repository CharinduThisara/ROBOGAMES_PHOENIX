from controller import Robot
from controller import Receiver
import json

def moveUP(t):
    time = 0
    left.setVelocity(-3.0)
    right.setVelocity(-3.0)
    while robot.step(timestep) != -1:
        while receiver.getQueueLength() > 0:
            print(json.loads(receiver.getData().decode('utf-8')))
            time+=1
            if time > t:
                break
            receiver.nextPacket()
        if time > t:
                break   
    left.setVelocity(0.0)
    right.setVelocity(0.0)
    
    return
    
def turnLeft(t):
    time = 0
    left.setVelocity(-3.0)
    right.setVelocity(3.0)
    while robot.step(timestep) != -1:
        while receiver.getQueueLength() > 0:
            print(json.loads(receiver.getData().decode('utf-8')))
            time+=1
            if time > t:
                break
            receiver.nextPacket()
        if time > t:
                break     
    left.setVelocity(0.0)
    right.setVelocity(0.0)
    
    return
    
def turnRight(t):
    time = 0
    left.setVelocity(3.0)
    right.setVelocity(-3.0)
    while robot.step(timestep) != -1:
        while receiver.getQueueLength() > 0:
            print(json.loads(receiver.getData().decode('utf-8')))
            time+=1
            if time > t:
                break
            receiver.nextPacket()
        if time > t:
                break
        
    left.setVelocity(0.0)
    right.setVelocity(0.0)
    
    return

robot = Robot()
timestep = int(robot.getBasicTimeStep())
receiver = robot.getDevice("receiver")
receiver.enable(10)

left = robot.getDevice('left wheel motor')
right = robot.getDevice('right wheel motor')

left.setPosition(float("inf"))
right.setPosition(float("inf"))

moveUP(150)
turnLeft(23)
moveUP(100)
"""
time = 0

while robot.step(timestep) != -1:
    left.setVelocity(-3.0)
    right.setVelocity(3.0)
    while receiver.getQueueLength() > 0:
        print(json.loads(receiver.getData().decode('utf-8')))
        time+=1
        if time > 200:
            break
        receiver.nextPacket()
    if time > 200:
            break
    
left.setVelocity(0.0)
right.setVelocity(0.0)"""
