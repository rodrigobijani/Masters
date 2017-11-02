# -----------------------------------------------------------------------------------
# Title: Grav-Mag Codes
# Author: Nelson Ribeiro Filho
# Description: Source codes that will be necessary during the masters course.
# Collaborator: Rodrigo Bijani
# -----------------------------------------------------------------------------------

import numpy as np # Numpy library

def deg_rad(angle):
    
    '''
    This function converts an angle value in degrees to an another value in radian.
    
    Input:
    angle - float - angle in degrees
    
    Output:
    argument - float - angle in radian    
    '''
    
    # Condition for the calculation
    if angle > 360.:
        r = angle//360
        angle = angle - r*360
    
    # Angle conversion
    argument = (angle/180.)*np.pi
    
    # Return the final output
    return argument

def rad_deg(argument):
    
    '''
    This function converts an angle value in radian to an another value in degrees.
    
    Input:
    argument - float - angle in radian
        
    Output:
    angle - float - angle in degrees    
    '''
    
    # Check the input value for an angle
    assert type(argument) is float, 'Angle value must be decimal!'
    # Angle conversion
    angle = (argument/np.pi)*180.
    # Return the final output
    return angle

def dir_cossine(theta_inc, theta_dec, theta_azi):
    
    '''
    This function calculates the cossines projected values on directions using inclination and declination values. Here, we do not considerate an azimuth as a zero value, but as a input value.
    
    Inputs:
    theta_inc - inclination angle
    theta_dec - declination angle
    theta_azi - azimuth angle
    
    Outputs:
    dirA - projected cossine A
    dirB - projected cossine B
    dirC - projected cossine C    
    '''
    
    # Use the function to convert some values
    incl = deg_rad(theta_inc)
    decl = deg_rad(theta_dec)
    azim = deg_rad(theta_azi)
    
    # Calculates the projected cossine values
    dirA = np.cos(incl)*np.cos(decl - azim)
    dirB = np.cos(incl)*np.sin(decl - azim)
    dirC = np.sin(incl)
    
    # Return the final output
    return dirA, dirB, dirC

def regional(field_values):
    
    '''
    This fucntion computes the projected components of the regional magnetic field in all directions X, Y and Z. This calculation is done by using a cossine projected function, which recieves the values for an inclination, declination and also and azimuth value. It returns all three components for a magnetic field (Fx, Fy e Fz), using a value for the regional field (F) as a reference for the calculation.
    
    Inputs: 
    valF - float - regional magnetic field value
    incF - float - magnetic field inclination value
    decF - float - magnetic field declination value
    aziF - float - magnetic field azimuth value
    
    Outputs:
    vecF - numpy array - F componentes along X, Y e Z axis
        
    Ps. All inputs can be arrays when they are used for a set of values.    
    '''
    
    assert field_values[0] != 0., 'Value of the regional magnetic field must be nonzero!'
        
    # Computes the projected cossine
    X, Y, Z = dir_cossine(field_values[1], field_values[2], field_values[3])
    # Compute all components
    Fx = field_values[0]*X
    Fy = field_values[0]*Y
    Fz = field_values[0]*Z
    # Set the F values as an array
    vecF =[Fx, Fy, Fz]
    # Return the final output
    return vecF

def sphere_bxyz(x, y, z, sphere, direction):
    
    '''    
    This function is a Python implementation for a Fortran subroutine contained in Blakely (1995). It computes the components of the magnetic induction (Bx, By, Bz) caused by a sphere with uniform distribution of magnetization. The direction X represents the north and Z represents growth downward. This function receives the coordinates of the points of observation (X, Y, Z - arrays), the coordinates of the center of the sphere (Xe, Ye, Ze), the magnetization intensity M and the values for inclination and declination (in degrees). The observation values are given in meters.
    
    Inputs: 
    x, y, z - numpy arrays - position of the observation points
    sphere[0, 1, 2] - arrays - position of the center of the sphere
    sphere[3] - float - value for the spehre radius  
    sphere[4] - flaot - magnetization intensity value
    direction - numpy array - inclination, declination and azimuth values
    
    Outputs:
    Bx - induced field on X direction
    By - induced field on Y direction
    Bz - induced field on Z direction
    
    Ps. The value for Z can be a scalar in the case of one depth, otherwise it can be a set of points.    
    '''
    #assert x.size == y.size 
    #assert x.shape[0] == x.shape[1]
    
    #sphere[0] = xe
    #sphere[1] = ye
    #sphere[2] = ze
    #sphere[3] = radius
    #sphere[4] = mag
    
    #direction[0] = inc
    #direction[1] = dec
    #direction[2] = az
    
    # Calculates some constants
    t2nt = 1.e9 # Testa to nT - conversion
    cm = 1.e-7  # Magnetization constant
    
    # Distances in all axis directions - x, y e z
    rx = x - sphere[0]
    ry = y - sphere[1]
    rz = z - sphere[2]
    # Computes the distance (r) as the module of the other three components
    r = np.sqrt((rx**2)+(ry**2)+(rz**2))
    # Computes the magnetization values for all directions
    mx, my, mz = dir_cossine(direction[0], direction[1], direction[2])
    
    # Auxiliars calculations
    dot = (rx*mx) + (ry*my) + (rz*mz)  # Scalar product
    m = (4.*np.pi*(sphere[3]**3)*sphere[4])/3.    # Magnetic moment
    
    # Components calculation - Bx, By e Bz
    Bx = cm*m*(3.*dot*rx-(r**2*mx))/r**5
    By = cm*m*(3.*dot*ry-(r**2*my))/r**5
    Bz = cm*m*(3.*dot*rz-(r**2*mz))/r**5
    # Final components calculation
    Bx *= t2nt
    By *= t2nt
    Bz *= t2nt
    
    # Return the final output
    return Bx, By, Bz

def sphere_tfa(xobs, yobs, zobs, sphere, direction, field):
    
    '''    
    This function computes the total field anomaly produced due to a solid sphere, which has its center located in xe, ye and ze, radius equals to r and also the magnetic property (magnetic intensity). This function receives the coordinates of the points of observation (X, Y, Z - arrays), the elements of the sphere, the values for inclination, declination and azimuth (in one array only!) and the elements of the field (intensity, inclination, declination and azimuth - IN THAT ORDER!). The observation values are given in meters.
    
    Inputs: 
    Inputs: 
    x, y, z - numpy arrays - position of the observation points
    sphere[0, 1, 2] - arrays - position of the center of the sphere
    sphere[3] - float - value for the spehre radius  
    sphere[4] - flaot - magnetization intensity value
    direction - numpy array - inclination, declination and azimuth values
    field - numpy array - values for the field and its orientations
    
    Outputs:
    totalfield - numpy array - calculated total field anomaly
    
    Ps. The value for Z can be a scalar in the case of one depth, otherwise it can be a set of points.    
    '''
    
    Bx, By, Bz = sphere_bxyz(xobs, yobs, zobs, sphere, direction)
    
    # Compute de regional field    
    reg_calc = regional(field)
    # Computing the components and the regional field
    Bx = Bx + reg_calc[0]
    By = By + reg_calc[1]
    Bz = Bz + reg_calc[2]
    
    # Final value for the total field anomaly
    totalfield = np.sqrt(((Bx**2)+(By**2)+(Bz**2))) - field[0]
    
    # Return the final output
    return totalfield

def sphere_gz(xobs, yobs, sphere):
    
    '''    
    This function calculates the gravity contribution due to a solid sphere. This is a Python implementation for the subroutine presented in Blakely (1995). On this function, there are received the value of the initial and final observation points (X and Y) and the properties of the sphere. The inputs sphere is allocated as: sphere[size = 5] = sphere[x center, y center, z center, radius , density]
    
    Inputs:
    sphere - numpy array - elements of the sphere
    
    Output:
    gz - numpy array - vertical component for the gravity signal due to a solid sphere    
    '''
    
    # Definition for some constants
    gamma = 6.67e-6
    dmy = 1e-5 # Dummy value
    
    # Compute the constant which is result due to the product
    C = (4./3)*np.pi*gamma*sphere[4]*(sphere[3]**3)
    
    # Compute the vertical component 
    gz = C*sphere[2]/(((xobs + dmy - sphere[0])**2 + (yobs + dmy - sphere[1])**2 + (sphere[2]**2))**(3./2))
    
    # Return the final output
    return gz