# -----------------------------------------------------------------------------------
# Title: Grav-Mag Codes
# Author: Nelson Ribeiro Filho
# Description: Source codes that will be necessary during the masters course.
# Collaborator: Rodrigo Bijani
# -----------------------------------------------------------------------------------

# Import Python libraries
import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
# Import my libraries
import auxiliars as aux

#--------------------------------------------------------------------------------------------------------------
# FUNCTIONS IMPLEMENTADED FOR GRAVITY AND MAGNETIC CALCULATIONS DUE TO A SOLID SPHERE
#
#--------------------------------------------------------------------------------------------------------------
# Function 1
def sphere_bx(x, y, z, sphere, direction):
    
    '''    
    This function is a Python implementation for a Fortran subroutine contained in Blakely (1995). 
    It computes the X component of the magnetic induction caused by a sphere with uniform  distribution of
    magnetization. The direction X represents the north and Z represents growth downward. This function 
    receives the coordinates of the points of observation (X, Y, Z - arrays), the coordinates of the center 
    of the sphere (Xe, Ye, Ze), the magnetization intensity M and the values for inclination and declination 
    (in degrees). The observation values are given in meters.
    
    Inputs: 
    x, y, z - numpy arrays - position of the observation points
    sphere[0, 1, 2] - arrays - position of the center of the sphere
    sphere[3] - float - value for the spehre radius  
    sphere[4] - flaot - magnetization intensity value
    direction - numpy array - inclination and declination values
    
    Outputs:
    Bx - induced field on X direction
     
    Ps. The value for Z can be a scalar in the case of one depth, otherwise it can be a set of points.    
    '''
    
    # Calculates some constants
    t2nt = 1.e9 # Testa to nT - conversion
    cm = 1.e-7  # Magnetization constant
    
    # Setting the directions
    A, B = direction[0], direction[1]
    
    #Setting some constants
    xe, ye, ze = sphere[0], sphere[1], sphere[2]
    radius = sphere[3]
    mag = sphere[4]
    
    # Distances in all axis directions - x, y e z
    rx = x - xe
    ry = y - ye
    rz = z - ze
    
    # Computes the distance (r) as the module of the other three components
    r2 = rx**2 + ry**2 + rz**2
        
    # Computes the magnetization values for all directions
    mx, my, mz = aux.dircos(A, B)
    
    # Auxiliars calculations
    dot = rx*mx + ry*my + rz*mz  # Scalar product
    m = (4.*np.pi*(radius**3)*mag)/3.    # Magnetic moment
    
    # Component calculation - Bx
    bx = cm*m*(3.*dot*rx - (r2*mx))/(r2**(2.5))

    # Final component calculation
    bx *= t2nt
    
    # Return the final output
    return bx

# Function 2
def sphere_by(x, y, z, sphere, direction):
    
    '''    
    This function is a Python implementation for a Fortran subroutine contained in Blakely (1995). 
    It computes the Y component of the magnetic induction caused by a sphere with uniform  distribution of
    magnetization. The direction X represents the north and Z represents growth downward. This function 
    receives the coordinates of the points of observation (X, Y, Z - arrays), the coordinates of the center 
    of the sphere (Xe, Ye, Ze), the magnetization intensity M and the values for inclination and declination 
    (in degrees). The observation values are given in meters.
    
    Inputs: 
    x, y, z - numpy arrays - position of the observation points
    sphere[0, 1, 2] - arrays - position of the center of the sphere
    sphere[3] - float - value for the spehre radius  
    sphere[4] - flaot - magnetization intensity value
    direction - numpy array - inclination, declination values
    
    Outputs:
    By - induced field on Y direction
     
    Ps. The value for Z can be a scalar in the case of one depth, otherwise it can be a set of points.    
    '''
    
    # Calculates some constants
    t2nt = 1.e9 # Testa to nT - conversion
    cm = 1.e-7  # Magnetization constant
    
    # Setting the directions
    A, B = direction[0], direction[1]
    
    #Setting some constants
    xe, ye, ze = sphere[0], sphere[1], sphere[2]
    radius = sphere[3]
    mag = sphere[4]
    
    # Distances in all axis directions - x, y e z
    rx = x - xe
    ry = y - ye
    rz = z - ze
    
    # Computes the distance (r) as the module of the other three components
    r2 = rx**2 + ry**2 + rz**2
        
    # Computes the magnetization values for all directions
    mx, my, mz = aux.dircos(A, B)
    
    # Auxiliars calculations
    dot = rx*mx + ry*my + rz*mz  # Scalar product
    m = (4.*np.pi*(radius**3)*mag)/3.    # Magnetic moment
    
    # Component calculation - By
    by = (3.*dot*ry - (r2*my))/(r2**(2.5))
    
    # Final component calculation
    by *= cm*m*t2nt
    
    # Return the final output
    return by

# Function 3
def sphere_bz(x, y, z, sphere, direction):
    
    '''    
    This function is a Python implementation for a Fortran subroutine contained in Blakely (1995). 
    It computes the Z component of the magnetic induction caused by a sphere with uniform  distribution of
    magnetization. The direction X represents the north and Z represents growth downward. This function 
    receives the coordinates of the points of observation (X, Y, Z - arrays), the coordinates of the center 
    of the sphere (Xe, Ye, Ze), the magnetization intensity M and the values for inclination and declination 
    (in degrees). The observation values are given in meters.
    
    Inputs: 
    x, y, z - numpy arrays - position of the observation points
    sphere[0, 1, 2] - arrays - position of the center of the sphere
    sphere[3] - float - value for the spehre radius  
    sphere[4] - flaot - magnetization intensity value
    direction - numpy array - inclination and declination values
    
    Outputs:
    Bz - induced field on Z direction
     
    Ps. The value for Z can be a scalar in the case of one depth, otherwise it can be a set of points.
    '''
    
    # Calculates some constants
    t2nt = 1.e9 # Testa to nT - conversion
    cm = 1.e-7  # Magnetization constant
    
    # Setting the directions
    A, B = direction[0], direction[1]
    
    #Setting some constants
    xe, ye, ze = sphere[0], sphere[1], sphere[2]
    radius = sphere[3]
    mag = sphere[4]
    
    # Distances in all axis directions - x, y e z
    rx = x - xe
    ry = y - ye
    rz = z - ze
    
    # Computes the distance (r) as the module of the other three components
    r2 = rx**2 + ry**2 + rz**2
    
    # Computes the magnetization values for all directions
    mx, my, mz = aux.dircos(A, B)
    
    # Auxiliars calculations
    dot = (rx*mx) + (ry*my) + (rz*mz)  # Scalar product
    m = (4.*np.pi*(radius**3)*mag)/3.    # Magnetic moment
    
    # Component calculation - Bz
    bz = (3.*dot*rz - (r2*mz))/(r2**(2.5))

    # Final component calculation
    bz *= cm*m*t2nt
    
    # Return the final output
    return bz

#--------------------------------------------------------------------------------------------------------------
# Function 4
def sphere_tf(x, y, z, sphere, direction, field):
    
    '''    
    This function computes the total field anomaly produced due to a solid sphere, which has its center 
    located in xe, ye and ze, radius equals to r and also the magnetic property (magnetic intensity). 
    This function receives the coordinates of the points of observation (X, Y, Z - arrays), the elements 
    of the sphere, the values for inclination, declination and azimuth (in one array only!) and the elements 
    of the field (intensity, inclination, declination and azimuth - IN THAT ORDER!). The observation values 
    are given in meters.
    
    Inputs: 
    x, y, z - numpy arrays - position of the observation points
    sphere[0, 1, 2] - arrays - position of the center of the sphere
    sphere[3] - float - value for the spehre radius  
    sphere[4] - float - magnetization intensity value
    direction - numpy array - inclination and declination values
    field - numpy array - values for the field and its orientations
    
    Outputs:
    totalfield - numpy array - calculated total field anomaly
    
    Ps. The value for Z can be a scalar in the case of one depth, otherwise it can be a set of points.    
    '''
       
    # Setting contants
    F, inc, dec = field[0], field[1], field[2]
    
    # Compute de regional field    
    reg = aux.regional(field)
    
    # Computing the components and the regional field
    bx = sphere_bx(x, y, z, sphere, direction) + reg[0]
    by = sphere_by(x, y, z, sphere, direction) + reg[1]
    bz = sphere_bz(x, y, z, sphere, direction) + reg[2]
    
    # Final value for the total field anomaly
    tf = np.sqrt(bx**2 + by**2 + bz**2) - F
    
    # Return the final output
    return tf

def sphere_tfa(x, y, z, sphere, direction, field):
    
    '''    
    This function computes the total field anomaly produced due to a solid sphere, which has its center 
    located in xe, ye and ze, radius equals to r and also the magnetic property (magnetic intensity). 
    This function receives the coordinates of the points of observation (X, Y, Z - arrays), the elements 
    of the sphere, the values for inclination, declination and azimuth (in one array only!) and the elements 
    of the field (intensity, inclination, declination and azimuth - IN THAT ORDER!). The observation values 
    are given in meters.
    
    Inputs: 
    x, y, z - numpy arrays - position of the observation points
    sphere[0, 1, 2] - arrays - position of the center of the sphere
    sphere[3] - float - value for the spehre radius  
    sphere[4] - flaot - magnetization intensity value
    direction - numpy array - inclination and declination values
    field - numpy array - inclination and declination values for the field
    
    Outputs:
    tf_aprox - numpy array - approximated total field anomaly
    
    Ps. The value for Z can be a scalar in the case of one depth, otherwise it can be a set of points.    
    '''
    
    # Setting some values
    f, inc, dec = field[0], field[1], field[2]
    
    # Compute de regional field    
    fx, fy, fz = aux.dircos(inc, dec)
    
    # Computing the components and the regional field
    bx = sphere_bx(x, y, z, sphere, direction)
    by = sphere_by(x, y, z, sphere, direction)
    bz = sphere_bz(x, y, z, sphere, direction)
    
    # Final value for the total field anomaly
    tf_aprox = fx*bx + fy*by + fz*bz
    
    # Return the final output
    return tf_aprox

#--------------------------------------------------------------------------------------------------------------
# Function 5
def sphere_gz(x, y, sphere):
    
    '''    
    This function calculates the gravity contribution due to a solid sphere. This is a Python implementation 
    for the subroutine presented in Blakely (1995). On this function, there are received the value of the 
    initial and final observation points (X and Y) and the properties of the sphere. The inputs sphere is 
    allocated as: sphere[size = 5] = sphere[x center, y center, z center, radius , density]
    
    Inputs:
    sphere - numpy array - elements of the sphere
        sphere[0, 1, 2] - positions of the sphere center at x, y and z directions
        sphere[3] - radius
        sphere[4] - density value
    Output:
    gz - numpy array - vertical component for the gravity signal due to a solid sphere    
    '''
    
    # Definition for some constants
    G = 6.673e-11
    si2mGal = 10.e5
    
    # Compute the constant which is result due to the product
    C = (4./3)*np.pi*G*si2mGal*sphere[4]*(sphere[3]**3)
    
    # Compute the vertical component 
    gz = C*sphere[2]/(((x - sphere[0])**2 + 
                       (y - sphere[1])**2 + 
                       (sphere[2]**2))**(3./2))
    
    # Return the final output
    return gz

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
# FUNCTIONS IMPLEMENTADED FOR GRAVITY AND MAGNETIC CALCULATIONS DUE TO A RECTANGULAR PRISM
#
#--------------------------------------------------------------------------------------------------------------
# Function 1
def prism_tf(x, y, z, prism, directions, field):
    
    '''
    This function calculates the total field anomaly produced by a rectangular prism located under surface; 
    it is a Python implementation for the Subroutin MBox which is contained on Blakely (1995). It recieves: 
    the coordinates of the positions in all directions, the elements of the prims, the angle directions and 
    the elements of the field. That function also uses the auxilary function DIR_COSSINE to calculate the 
    projections due to the field F and the source S.
    
    Inputs:
    x, y - numpy arrays - observation points in x and y directions
    z - numpy array/float - height for the observation
    prism - numpy array - all elements for the prims
        prism[0, 1] - initial and final coordinates at X (dimension at X axis!)
        prism[2, 3] - initial and final coordinates at Y (dimension at Y axis!)
        prism[4, 5] - initial and final coordinates at Z (dimension at Z axis!)
        prism[6] - magnetic intensity
    directions - numpy array - elements for source directions
        directions[0] - float - source inclination
        directions[1] - float - source declination
    field - numpy array - elementes for regional field
        field[0] - float - magnetic field inclination
        field[1] - float - magnetic field declination
        
    Output:
    tfa - numpy array - calculated total field anomaly
    
    X and Y represents North and East; Z is positive downward.
    Ps. Z can be a array with all elements for toppography or a float point as a flight height.
    '''    
    
    # Stablish some constants
    t2nt = 1.e9 # Testa to nT - conversion
    cm = 1.e-7  # Magnetization constant

    # Setting some values
    D1 = directions[0]
    D2 = directions[1]
    F1 = field[0]
    F2 = field[1] 
    
    # Calculate the directions for the source magnetization and for the field
    Ma, Mb, Mc = aux.dircos(D1, D2) # s -> source
    Fa, Fb, Fc = aux.dircos(F1, F2) # f -> field

    # Aranges all values as a vector
    MF = [Ma*Fb + Mb*Fa, 
          Ma*Fc + Mc*Fa, 
          Mb*Fc + Mc*Fb, 
          Ma*Fa, 
          Mb*Fb, 
          Mc*Fc]
    
    # Limits for initial and final position along the directions
    A = [prism[0] - x, prism[1] - x]
    B = [prism[2] - y, prism[3] - y]
    H = [prism[5] - z, prism[4] - z]
    
    # Create the zero array to allocate the total field result
    tfa = np.zeros_like(x)
    
    # Loop for controling the signal of the function    
    mag = prism[6]
    for k in range(2):
        mag *= -1
        H2 = H[k]**2
        for j in range(2):
            Y2 = B[j]**2
            for i in range(2):
                X2 = A[i]**2
                AxB = A[i]*B[j]
                R2 = X2 + Y2 + H2
                R = np.sqrt(R2)
                HxR = H[k]*R
                tfa += ((-1.)**(i + j))*mag*(0.5*(MF[2])*np.log((R - A[i])/(R + A[i])) + 0.5*(MF[1])*
                                             np.log((R - B[j])/(R + B[j])) - (MF[0])*np.log(R + H[k]) -
                                             (MF[3])*np.arctan2(AxB, X2 + HxR + H2) -
                                             (MF[4])*np.arctan2(AxB, R2 + HxR - X2) +
                                             (MF[5])*np.arctan2(AxB, HxR))        
        
        tfa *= t2nt*cm
    
    # Return the final output
    return tfa

#--------------------------------------------------------------------------------------------------------------
def potential(xo, yo, zo, prism):
    
    '''
    This function calculates the gravitational potential due to a rectangular prism. It is calculated solving a numerical integral approximated by using the gravity field G(x,y,z), once G can be written as minus the gradient of the gravitational potential. This function recieves all obsevation points for an array or a grid and also the value for height of the observation, which can be a simple float number (as a level value) or a 1D array. It recieves the values for the prism dimension in X, Y and Z directions.
    
    Inputs:
    x, y - numpy arrays - observation points in x and y directions
    z - numpy array/float - height for the observation
    prism - numpy array - all elements for the prims
        prism[0, 1] - initial and final coordinates at X (dimension at X axis!)
        prism[2, 3] - initial and final coordinates at Y (dimension at Y axis!)
        prism[4, 5] - initial and final coordinates at Z (dimension at Z axis!)
        prism[6] - density value
        
    Output:
    potential - numpy array - gravitational potential due to a solid prism
    
    '''
       
    # Definitions for all distances
    x = [prism[1] - xo, prism[0] - xo]
    y = [prism[3] - yo, prism[2] - yo]
    z = [prism[5] - zo, prism[4] - zo]
    
    # Definition for density
    rho = prism[6]
    
    # Definition - some constants
    G = 6.673e-11
    si2mGal = 100000.
    
    # Creating the zeros vector to allocate the result
    potential = numpy.zeros_like(xp)
    
    # Solving the integral as a numerical approximation
    for k in range(2):
        for j in range(2):
            for i in range(2):
                r = sqrt(x[i]**2 + y[j]**2 + z[k]**2)
                result = (x[i]*y[j]*np.log(z[k] + r)
                          + y[j]*z[k]*np.log(x[i] + r)
                          + x[i]*z[k]*np.log(y[j] + r)
                          - 0.5*x[i]**2 *
                          np.arctan2(z[k]*y[j], x[i]*r)
                          - 0.5*y[j]**2 *
                          np.arctan2(z[k]*x[i], y[j]*r)
                          - 0.5*z[k]**2*np.arctan2(x[i]*y[j], z[k]*r))
                potential += ((-1.)**(i + j + k))*result*rho
    
    # Multiplying the values for 
    potential *= G
        
    # Return the final output
    return potential

def prism_gx(xo, yo, zo, prism):
    
    '''
    This function is a Python implementation for the X horizontal component for the gravity field due to a rectangular prism, which has initial and final positions equals to xi and xf, yi and yf, for the X and Y directions. This function also recieve the obsevation points for an array or a grid and also the value for height of the observation, which can be a simple float number (as a level value) or a 1D array.
    
    Inputs:
    x, y - numpy arrays - observation points in x and y directions
    z - numpy array/float - height for the observation
    prism - numpy array - all elements for the prims
        prism[0, 1] - initial and final coordinates at X (dimension at X axis!)
        prism[2, 3] - initial and final coordinates at Y (dimension at Y axis!)
        prism[4, 5] - initial and final coordinates at Z (dimension at Z axis!)
        prism[6] - density value
        
    Output:
    gx - numpy array - vertical component for the gravity atraction
    
    '''
    
    # Definitions for all distances
    x = [prism[1] - xo, prism[0] - xo]
    y = [prism[3] - yo, prism[2] - yo]
    z = [prism[5] - zo, prism[4] - zo]
    
    # Definition for density
    rho = prism[6]
    
    # Definition - some constants
    G = 6.673e-11
    si2mGal = 100000.
    
    # Numpy zeros array to update the result
    gx = np.zeros_like(xo)
    
    # Compute the value for Gz
    for k in range(2):
        for j in range(2):
            for i in range(2):
                r = np.sqrt(x[i]**2 + y[j]**2 + z[k]**2)
                result = -(y[j]*np.log(z[k] + r) + z[k]*np.log(y[j] + r) - x[i]*np.arctan2(z[k]*y[j], x[i]*r))
                gx += ((-1.)**(i + j + k))*result*rho
                
    # Multiplication for all constants and conversion to mGal
    gx *= G*si2mGal
    
    # Return the final output
    return gz

def prism_gy(xo, yo, zo, prism):
    
    '''
    This function is a Python implementation for the Y horizontal  component for the gravity field due to a rectangular prism, which has initial and final positions equals to xi and xf, yi and yf, for the X and Y directions. This function also recieve the obsevation points for an array or a grid and also the value for height of the observation, which can be a simple float number (as a level value) or a 1D array.
    
    Inputs:
    x, y - numpy arrays - observation points in x and y directions
    z - numpy array/float - height for the observation
    prism - numpy array - all elements for the prims
        prism[0, 1] - initial and final coordinates at X (dimension at X axis!)
        prism[2, 3] - initial and final coordinates at Y (dimension at Y axis!)
        prism[4, 5] - initial and final coordinates at Z (dimension at Z axis!)
        prism[6] - density value
        
    Output:
    gy - numpy array - vertical component for the gravity atraction
    
    '''
    
    # Definitions for all distances
    x = [prism[1] - xo, prism[0] - xo]
    y = [prism[3] - yo, prism[2] - yo]
    z = [prism[5] - zo, prism[4] - zo]
    
    # Definition for density
    rho = prism[6]
    
    # Definition - some constants
    G = 6.673e-11
    si2mGal = 100000.
    
    # Numpy zeros array to update the result
    gy = np.zeros_like(xo)
    
    # Compute the value for Gz
    for k in range(2):
        for j in range(2):
            for i in range(2):
                r = np.sqrt(x[i]**2 + y[j]**2 + z[k]**2)
                result = -(x[i]*np.log(y[j] + r) + y[j]*np.log(x[i] + r) - z[k]*np.arctan2(x[i]*y[j], z[k]*r))
                gz += ((-1.)**(i + j + k))*result*rho
                
    # Multiplication for all constants and conversion to mGal
    gy *= G*si2mGal
    
    # Return the final output
    return gy

def prism_gz(xo, yo, zo, prism):
    
    '''
    This function is a Python implementation for the vertical component for the gravity field due to a rectangular prism, which has initial and final positions equals to xi and xf, yi and yf, for the X and Y directions. This function also recieve the obsevation points for an array or a grid and also the value for height of the observation, which can be a simple float number (as a level value) or a 1D array.
    
    Inputs:
    x, y - numpy arrays - observation points in x and y directions
    z - numpy array/float - height for the observation
    prism - numpy array - all elements for the prims
        prism[0, 1] - initial and final coordinates at X (dimension at X axis!)
        prism[2, 3] - initial and final coordinates at Y (dimension at Y axis!)
        prism[4, 5] - initial and final coordinates at Z (dimension at Z axis!)
        prism[6] - density value
        
    Output:
    gz - numpy array - vertical component for the gravity atraction
    
    '''
    
    # Definitions for all distances
    x = [prism[1] - xo, prism[0] - xo]
    y = [prism[3] - yo, prism[2] - yo]
    z = [prism[5] - zo, prism[4] - zo]
    
    # Definition for density
    rho = prism[6]
    
    # Definition - some constants
    G = 6.673e-11
    si2mGal = 10.e5
    
    # Numpy zeros array to update the result
    gz = np.zeros_like(xo)
    
    # Compute the value for Gz
    for k in range(2):
        for j in range(2):
            for i in range(2):
                r = np.sqrt(x[i]**2 + y[j]**2 + z[k]**2)
                result = -(x[i]*np.log(y[j] + r) + y[j]*np.log(x[i] + r) - z[k]*np.arctan2(x[i]*y[j], z[k]*r))
                gz += ((-1.)**(i + j + k))*result*rho
                
    # Multiplication for all constants and conversion to mGal
    gz *= G*si2mGal
    
    # Return the final output
    return gz
