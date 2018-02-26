# -*- coding: utf-8 -*-
#/usr/bin/python
import math


# set parameters
mass = 1.0
viscosity = 0.15
spring1 = 0.5
spring3 = 0.5

#initial values
acceleration = 0.0
velocity = 1.0
position = 1.0
time = 0.0
frequency = 0.833
period = (2*math.pi)/frequency
amplitude = 0.19
samplePoints = 2000
pointsPerPeriod = 1000
dt = period/pointsPerPeriod

#initialize archive lists
positionArchive = [0] * samplePoints
velocityArchive = [0] * samplePoints

for j in range(0,pointsPerPeriod):
	positionArchive[j] = position
	velocityArchive[j] = velocity
	for i in range(0,samplePoints):
	
	    acceleration = (-viscosity * velocity + spring1 * position - spring3*position*position*position + amplitude * math.cos(
	    frequency * time))/mass
	
	    #Euler-Cromer algorithm
	    velocity += acceleration * dt
	    position += velocity * dt
	    time += dt

import matplotlib.pyplot as plt

plt.plot(positionArchive,velocityArchive, '.')

plt.show()


