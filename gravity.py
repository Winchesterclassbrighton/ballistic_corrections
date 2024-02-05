import numpy as np
import math as mt


re = 6.3781*mt.pow(10.0, 6.0)  # meters,   radius of the earth
me = 5.97219*mt.pow(10.0, 24.0)  # kilograms,   mass of the earth
G = 6.67430*mt.pow(10.0, -11.0)  # Newtons*meters^2*kilograms^-2


def gps3c2pos(altitude, latitude, longitutde):
    return np.arrray([(altitude+re)*mt.cos(latitude)*mt.cos(longitude), (altitude+re)*mt.cos(latitude)*mt.sin(longitude), (altitude+re)*mt.sin(latitude)])
    

class BallisticProjectile:
    def __init__(self, mass, position, velocity, time):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.time = time
        self.acceleration = self.accelration_high_altitude_gravity()

    def accelration_high_altitude_gravity(self):
        return (-mt.pow(self.position.dot(self.position), -1.5)*me*G)*self.position

    def drag(self, air_density, coefficient_of_drag, cross_section):
        return -0.5*air_density*coefficient_of_drag*cross_section*mt.pow((self.velocity.dot(self.velocity)), 0.5)*self.velocity

    def time_evolve(self, nt, dt):
        for i in range(0, nt):
            self.acceleration = self.accelration_high_altitude_gravity()
            self.acceleration = self.acceleration + self.dar
            self.position = self.position + dt*self.velocity
            self.velocity = self.velocity + self.drag()
            t = t + dt
        
