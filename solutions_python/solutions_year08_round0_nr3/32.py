#!/usr/bin/env python2.5

import math
import sys

import psyco
psyco.full()
        
def input_text():
    return sys.stdin.readline().strip()

def input_int():
    return int( input_text() )

def input_int_list():
    return ( int( x ) for x in input_text().split() )

def input_float_list():
    return ( float( x ) for x in input_text().split() )

def integrate_disk( x1, x2, r ):
    u1 = math.asin( x1/r )
    u2 = math.asin( x2/r )
    return r**2*( u2 - u1 + math.sin( u2 )*math.cos( u2 ) - math.sin( u1 )*math.cos( u1 ) )/2

    
N = input_int()

for k in range( N ):
    f, R, t, r, g = input_float_list()

    racquet_total_area = math.pi*R**2
    max_grid_radius = max( 0, R - t - f )
    max_grid_radius_squared = max_grid_radius**2
    grid_interval = g + 2*r
    safe_gap_width =  max( 0, g - 2*f )

    safe_area = 0

    x1 = r + f
    while x1 < max_grid_radius:
        x1_squared = x1**2
        x2 = x1 + safe_gap_width
        x2_squared = x2**2
        y1 = r + f
        y1_squared = y1**2
        while x1_squared + y1_squared < max_grid_radius_squared:
            y2 = y1 + safe_gap_width
            y2_squared = y2**2
            if x2_squared + y2_squared <= max_grid_radius_squared:
                safe_area += safe_gap_width**2
            elif x1_squared + y2_squared <= max_grid_radius_squared:
                xi = math.sqrt( max_grid_radius_squared - y2_squared )
                safe_area += safe_gap_width*( xi - x1 )
                if x2_squared + y1_squared <= max_grid_radius_squared:
                    safe_area += integrate_disk( xi, x2, max_grid_radius ) - ( x2 - xi )*y1
                else:
                    xi2 = math.sqrt( max_grid_radius_squared - y1_squared )
                    safe_area += integrate_disk( xi, xi2, max_grid_radius ) - ( xi2 - xi )*y1
            else:
                yi = math.sqrt( max_grid_radius_squared - x1_squared )
                if x2_squared + y1_squared <= max_grid_radius_squared:
                    safe_area += integrate_disk( x1, x2, max_grid_radius ) - safe_gap_width*y1
                else:
                    xi2 = math.sqrt( max_grid_radius_squared - y1_squared )
                    safe_area += integrate_disk( x1, xi2, max_grid_radius ) - ( xi2 - x1 )*y1
            y1 += grid_interval
            y1_squared = y1**2
        x1 += grid_interval

    P = 1 - 4*safe_area/racquet_total_area
    
    print 'Case #%i: %f' % ( k + 1, P )
