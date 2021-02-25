import pygame
from vpython import *

# Set the canvas
scene = canvas(title='Traffic Signals', width=600, height=400, center=vector(0, 0, 0),
               background=color.cyan, autoscale=1)

# Create the roads
road = box(color=vector(0.3, 0.3, 0.3), pos=vector(0, -11, 0), axis=vector(0.01, 0, -0.1),
           length=10, height=0.5, width=50)
road1 = box(color=vector(0.3, 0.3, 0.3), pos=vector(0, -11, 0), axis=vector(0.5, 0, 0),
            length=10, height=0.5, width=50)
road2 = box(color=vector(0.3, 0.3, 0.3), pos=vector(-25, -11, 0), axis=vector(-5, 0, 0),
            length=5, height=0.5, width=100)
road3 = box(color=vector(0.3, 0.3, 0.3), pos=vector(25, -11, 0), axis=vector(5, 0, 0),
            length=5, height=0.5, width=100)
road4 = box(color=vector(0.3, 0.3, 0.3), pos=vector(1, -20, 5), axis=vector(0, 0, -0.5),
            length=10, height=0.5, width=100)
line = box(color=vector(1, 0.6, 0), pos=vector(1, -20, 5), axis=vector(0, 0, -0.5),
           length=1.2, height=0.5, width=100)
line1 = box(color=vector(1, 0.6, 0), pos=vector(25, -11, 0), axis=vector(5, 0, 0),
            length=1.2, height=0.5, width=100)
line2 = box(color=vector(1, 0.6, 0), pos=vector(-25, -11, 0), axis=vector(-5, 0, 0),
            length=1.2, height=0.5, width=100)
crossWalk1 = box(color=vector(1, 1, 1), pos=vector(0, -8, 0), axis=vector(0.5, 0, 0),
                 length=7, height=0.01, width=3)
crossWalk2 = box(color=vector(1, 1, 1), pos=vector(0, -10, 8), axis=vector(0.5, 0, 0),
                 length=9, height=0.01, width=3)
crossWalk3 = box(color=vector(1, 1, 1), pos=vector(5, -9, 4), axis=vector(0, 0, -2),
                 length=9, height=0.01, width=3)
crossWalk4 = box(color=vector(1, 1, 1), pos=vector(-5, -9, 4), axis=vector(0, 0, -2),
                 length=9, height=0.01, width=3)

# Set the values of signals when they are off or on
greenOff = vector(0, 0.5, 0)
greenOn = vector(0, 1, 0)
yellowOff = vector(0.6, 0.6, 0)
yellowOn = vector(1.5, 1, 0)
redOff = vector(0.5, 0, 0)
redOn = vector(1.5, 0, 0)

# Create the parts of Traffic Light
frame = box(color=vector(0.3, 0.3, 0.3), pos=vector(-5, 4, 0), length=4, height=10, width=4, opacity=1)
cover = box(color=vector(0.4, 0.4, 0.4), pos=vector(-4.9, 9, 2), length=4.5, height=0.4, width=4, opacity=1)
cover1 = box(color=vector(0.4, 0.4, 0.4), pos=vector(-7, 4, 3), length=0.4, height=10, width=2, opacity=1)
cover2 = box(color=vector(0.4, 0.4, 0.4), pos=vector(-2.8, 4, 2), length=0.4, height=10, width=4, opacity=1)
pole = cylinder(color=vector(0.5, 0.5, 0.5), pos=vector(-5, -9, 0), axis=vector(0, 15, 0), radius=1)
redLight = sphere(color=redOff, pos=vector(-5, 7, 2), radius=1.4, emissive=0.5)
yellowLight = sphere(color=yellowOff, pos=vector(-5, 4, 2), radius=1.4, emissive=0.5)
greenLight = sphere(color=greenOff, pos=vector(-5, 1, 2), radius=1.4, emissive=0.5)

pygame.init()
pygame.mixer.music.load('churchBell.mp3')  # load a sound for red and yellow signal
run = False  # Initialize a boolean value for the run/pause button


def run_button():  # Set up the control button
    global run
    if run:
        b.text = 'Run'
        pygame.mixer.music.stop()
    else:
        b.text = 'Pause'
        pygame.mixer.music.play()
    run = not run


b = button(bind=run_button, text='Run')  # Add a control button


frameRate = 20
signalTime = 0
while True:  # Set the running loop between the three lights
    if run:
        signalTime += 1
        if signalTime <= 70:
            redLight.color = redOn
            yellowLight.color = yellowOff
            greenLight.color = greenOff
            pygame.mixer.music.unpause()

        elif signalTime <= 100:
            redLight.color = redOff
            yellowLight.color = yellowOn
            greenLight.color = greenOff
            pygame.mixer.music.unpause()

        elif signalTime <= 170:
            pygame.mixer.music.pause()
            redLight.color = redOff
            yellowLight.color = yellowOff
            greenLight.color = greenOn

        elif signalTime <= 200:
            redLight.color = redOff
            yellowLight.color = yellowOn
            greenLight.color = greenOff
            pygame.mixer.music.unpause()

        elif signalTime > 200:
            signalTime = 0
            pygame.mixer.music.pause()

        rate(frameRate)  # set the animation rate
