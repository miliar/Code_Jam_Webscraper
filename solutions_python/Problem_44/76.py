#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

def doit():
	input = open("B.in", 'r')
	output = open("B.out", 'w')
	
	T = int( input.readline().strip() )
	
	i = 1
	
	while i <= T:
		N = int( input.readline().strip() )
		x = 0.0
		y = 0.0
		z = 0.0
		vx = 0.0
		vy = 0.0
		vz = 0.0
		
		j = 0
		
		while j < N:
			tmp = input.readline().split()
			
			x = x+float( tmp[0] )
			y = y+float( tmp[1] )
			z = z+float( tmp[2] )
			vx = vx+float( tmp[3] )
			vy = vy+float( tmp[4] )
			vz = vz+float( tmp[5] )
			
			j = j+1
		
		x = x/N
		y = y/N
		z = z/N
		vx = vx/N
		vy = vy/N
		vz = vz/N
		
		t=0.0
		#t = max(  ( x*vx + y*vy + z*vz )/( vx*vx + vy*vy + vz*vz ), 0.0  )
		
		while True:
			dm = math.sqrt(  dsq( x, y, z, vx, vy, vz, t )  )
			dmp = dsqprim( x, y, z, vx, vy, vz, t )
			
			#print dm, dmp, t
			
			if abs( dm ) <= math.pow( 10, -7 ) or abs( dmp ) <= math.pow( 10, -8 ):
				break
			else:
				t = t - dsqprim( x, y, z, vx, vy, vz, t )/dsqbis( x, y, z, vx, vy, vz, t )
				
				if t < 0:
					t = 0
					dm = math.sqrt(  dsq( x, y, z, vx, vy, vz, t )  )
					break
		
		#print dm, t
		
		output.write("Case #" + str(i) + ": " + str( dm ) + " " + str( t ) + "\n" )
		
		i = i+1
	
	output.close()
	input.close()


def dsq( x, y, z, vx, vy, vz, t ):
	return (x+vx*t)*(x+vx*t) + (y+vy*t)*(y+vy*t) + (z+vz*t)*(z+vz*t)


def dsqprim( x, y, z, vx, vy, vz, t ):
	return 2.0*(  x*vx + vx*vx*t + y*vy + vy*vy*t + z*vz + vz*vz*t )


def dsqbis( x, y, z, vx, vy, vz, t ):
	return 2.0*(  vx*vx + vy*vy + vz*vz  )


doit()
