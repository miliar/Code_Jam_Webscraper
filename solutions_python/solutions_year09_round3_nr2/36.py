#!/usr/bin/python2

import sys, os, string, re

def get_center(init_pos, velocity, time):
	center = init_pos[:]
	for i in range(3):
		center[i] += time*velocity[i]
	return center

def get_dist(a, b):
	ret = 0.0
	for i in range(3):
		ret += (a[i]-b[i])**2
	return ret**.5

in_file = sys.stdin
T = int(in_file.readline())
for case_num in range(T):
	N = int(in_file.readline().strip())

	init_pos = [0.0, 0.0, 0.0]
	velocity = [0.0, 0.0, 0.0]
	for i in range(N):
		x = map(int, in_file.readline().strip().split())
		init_pos[0] += x[0]
		init_pos[1] += x[1]
		init_pos[2] += x[2]
		velocity[0] += x[3]
		velocity[1] += x[4]
		velocity[2] += x[5]
	init_pos[0] /= N
	init_pos[1] /= N
	init_pos[2] /= N
	velocity[0] /= N
	velocity[1] /= N
	velocity[2] /= N
	
	[x0, y0, z0] = init_pos
	[dx, dy, dz] = velocity
	q = (dx**2+dy**2+dz**2)
	if q == 0:
		time = 0
	else:
		time = -(dx*x0+dy*y0+dz*z0)/(dx**2+dy**2+dz**2)
	time = max(time, 0)
	[x, y, z] = [x0+time*dx, y0+time*dy, z0+time*dz]
	dist = (x*x+y*y+z*z)**.5
	
	print 'Case #%d: %.8f %.8f' % (case_num+1, dist, time)
