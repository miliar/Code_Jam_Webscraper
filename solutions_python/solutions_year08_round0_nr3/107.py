from __future__ import division, with_statement

# set up logging system
import logging
log_format = "%(module)s.%(name)s@%(asctime)s : %(message)s"
logging.basicConfig(
	level=logging.DEBUG,
	datefmt="%H:%M",
	format=log_format,
	)
file_handler = logging.FileHandler("output.txt")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(log_format))
logging.getLogger("").addHandler(file_handler)
logger = logging.getLogger("")

import itertools
from itertools import *

import os
import sys
import time

import socket
import re
import threading

import math
from math import *

import random

import collections
import subprocess
import heapq

def _delta_iterator(seq):
	prev = None
	for s in seq:
		if prev is not None:
			yield s - prev
		prev = s


def delta(seq):
	return list(_delta_iterator(seq))


def execute(args, blocking=True, cwd=""):
	args = map(str, args)
	c = os.path.abspath(args[0])
	if os.path.exists(c):
		args[0] = c
	if not cwd:
		cwd = os.getcwd()
	#~ print args, cwd, blocking
	p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd)
	#~ print p
	#~ print dir(p)
	if blocking:
		return p.stdout.read().strip()
	else:
		return p

def choose_object_side(object_pos, r, vehicle_pos, direction, viewer=None):
	n1, n2 = tangent_vectors(object_pos, r, vehicle_pos)
	n1 += vehicle_pos
	n2 += vehicle_pos
	if viewer:
		viewer.line(c_to_t(n1), color=(0,200,255))
		viewer.line(c_to_t(n2), color=(0,200,255))
						
	origin = vehicle_pos
	theta1 = acos(dot(origin, n1) / (magnitude(n1) * magnitude(origin)))
	theta2 = acos(dot(origin, n2) / (magnitude(n2) * magnitude(origin)))
	if theta1 < theta2:
		return n1
	else:
		return n2

def choose_object_side2(n1, n2, r, vehicle_pos, direction, viewer=None):
	n1 += vehicle_pos
	n2 += vehicle_pos
	if viewer:
		viewer.line(c_to_t(n1), color=(0,200,255))
		viewer.line(c_to_t(n2), color=(0,200,255))
						
	origin = vehicle_pos
	theta1 = acos(dot(origin, n1) / (magnitude(n1) * magnitude(origin)))
	theta2 = acos(dot(origin, n2) / (magnitude(n2) * magnitude(origin)))
	if theta1 < theta2:
		return n1
	else:
		return n2

'''	
def A_star(start, goal, successors, edge_cost, heuristic_cost_to_goal=lambda position, goal:0):
  """Very general a-star search. Start and goal are objects to be compared
  with the 'is' operator, successors is a function that, given a node, returns
  other nodes reachable therefrom, edge_cost is a function that returns the
  cost to travel between two nodes, and heuristic_cost_to_goal is an
  admissible heuristic function that gives an underestimate of the cost from a
  position to the goal."""
  import heapq
  closed = set()
  open = [(0, 0, (start,))]
  while open:
    heuristic_cost, cost_so_far, path = heapq.heappop(open)
    tail = path[-1]
    if tail in closed:
      continue
    if tail == goal:
      return path
    closed.add(tail)
    for new_tail in successors(tail):
      new_cost_so_far = cost_so_far + edge_cost(tail, new_tail)
      new_heuristic_cost = new_cost_so_far + heuristic_cost_to_goal(new_tail, goal)
      heapq.heappush(open, (new_cost_so_far, new_heuristic_cost, path+(new_tail,)))
  raise RuntimeError('No path found.')
'''

class PathFinder(object):
	def __init__(self):
		self.path

class PathFinding(object):
	def __init__(self, world, size=50, viewer=None):
		self.size = size
		self.objects_seen = []
		self.world = world
		self.viewer = viewer
		self.states = [[0 for x in range(self.size)] for y in range(self.size)]
		
	def world_to_index(self, w):
		#w = -dx/2 + sx*index[0], -dy/2 + sy*index[1]	
		w = c_to_t(w)
		dx, dy = self.world['dx'], self.world['dy']
		sx, sy = dx / self.size, dy / self.size
		w = w[0] + dx/2, w[1] + dy/2
		return int(w[0] / sx), int(self.size - w[1] / sy)

	def index_to_world(self, index):
		dx, dy = self.world['dx'], self.world['dy']	
		sx, sy = dx / self.size, dy / self.size	
		return -dx/2 + sx*index[0] + sx/2, -dy/2 + sy*(self.size-index[1]) - sy/2

	def draw_grid(self, viewer, size):
		for y in range(self.size):
			for x in range(self.size):
				self.viewer.grid_square((x, y), self.size, permanent=1, style=1)
 

	def update_grid(self, state):
		if self.viewer: 
			self.viewer.draw_grid(self.size)
		for o in state["items"]:
			if o not in self.objects_seen:
				if o["object_kind"] in ['h']: 
					continue
				self.objects_seen.append(o)
				if self.viewer:
					r = o["object_r"]
					if r < 1: 
						continue
					d1 = self.world_to_index(o["object_pos"] - complex(r, r))
					d2 = self.world_to_index(o["object_pos"] + complex(r, r))
					p1 = min(d1[0], d2[0]), min(d1[1], d2[1])
					p2 = max(d1[0], d2[0]), max(d1[1], d2[1])					
					for x in range(p1[0], p2[0]+1):
						for y in range(p1[1], p2[1]+1):
							self.viewer.grid_square((x, y), self.size, fill=-1)
							if x >= 0 and y >= 0 and x < self.size and y < self.size:
								self.states[x][y] = 1
								for index in self.successors((x,y)):
									self.viewer.grid_square(index, self.size, color=(0,255,0), fill=-1)								
								
		start = self.world_to_index(state["vehicle_pos"])
		goal = self.world_to_index(complex(0,0))
		path = self.find_route(start, goal)
		for node in path:
			self.viewer.grid_square(node, self.size, permanent=0, color=(255,255,0), fill=-1)
		return path[1]

	def successors(self, index):		
		index = c_to_t(index)
		for x in range(index[0]-1,index[0]+2):			
			if x >= 0 and x < self.size:			
				for y in range(index[1]-1,index[1]+2):
					if x == index[0] and y == index[1]:
						continue
					if y >= 0 and y < self.size:
						if not self.states[x][y]:
							yield (x, y)
		
	def edge_cost(self, a, b):
		return 1
		
	def heuristic_cost_to_goal(self, point, goal):
		return distance(complex(*point), complex(0,0))
		
	def find_route(self, start, goal):
		"""Very general a-star search. Start and goal are objects to be compared
		with the 'is' operator, successors is a function that, given a node, returns
		other nodes reachable therefrom, edge_cost is a function that returns the
		cost to travel between two nodes, and heuristic_cost_to_goal is an
		admissible heuristic function that gives an underestimate of the cost from a
		position to the goal."""	
		closed = set()
		opened = [(0, 0, (start,))]
		while opened:
			heuristic_cost, cost_so_far, path = heapq.heappop(opened)
			tail = path[-1]
			if tail in closed:
				continue
			if tail == goal:
				return path
			closed.add(tail)
			for new_tail in self.successors(tail):
				new_cost_so_far = cost_so_far + self.edge_cost(tail, new_tail)
				new_heuristic_cost = new_cost_so_far + self.heuristic_cost_to_goal(new_tail, goal)
				heapq.heappush(opened, (new_cost_so_far, new_heuristic_cost, path+(new_tail,)))
		return[(0,0)]

def sgn(i):
	if i > 0:
		return 1
	return -1
	
	
def line_through_circle(line, circle, line_is_finite=1):
	x1, y1, x2, y2 = line
	a, b, r = circle
	x1 -= a
	y1 -= b
	x2 -= a
	y2 -= b
	dx = x2 - x1
	dy = y2 - y1
	dr = math.sqrt(dx**2 + dy**2)
	D = x1*y2 - x2*y1	
	dis = r**2 * dr**2 - D**2	
	if dis < 0:
		return False
	if line_is_finite:
		s_x1 = (D * dy + sgn(dy)*dx*math.sqrt(dis) )/(dr**2)
		s_x2 = (D * dy - sgn(dy)*dx*math.sqrt(dis) )/(dr**2)		
		s_y1 = (-D * dx + abs(dy)*math.sqrt(dis) )/(dr**2)
		s_y2 = (-D * dx - abs(dy)*math.sqrt(dis) )/(dr**2)	
		if max(s_x1, s_x2) < max(x1, x2) and max(s_y1, s_y2) < max(y1, y2):
			if min(s_x1, s_x2) > min(x1, x2) and min(s_y1, s_y2) > min(y1, y2):
				return True
		return False			
	return True


def tangent_vectors(to_object, radius, from_position):
	assert distance(to_object, from_position) > radius
	r = radius
	x, y = from_position.real, from_position.imag
	cx, cy = to_object.real, to_object.imag
	bigtheta = math.atan2(cy-y, cx-x)
	theta = math.asin(r/distance(to_object, from_position))
	l = math.sqrt(distance(to_object, from_position)**2 - r**2)
	diffangle1 = bigtheta - theta									
	tangent1 = complex(x+l*math.cos(diffangle1), (y+l*math.sin(diffangle1))) - from_position
	diffangle2 = bigtheta + theta									
	tangent2 = complex(x+l*math.cos(diffangle2), (y+l*math.sin(diffangle2))) - from_position
	return tangent1, tangent2

	
def angle_between(complex1, complex2):
	return acos(dot(complex1, complex2) / (magnitude(complex1) * magnitude(complex2)))


def objects_overlap(object1, object2, position):
	t1, t2 = tangent_vectors(object1['object_pos'], object1['object_r'], position)
	t3, t4 = tangent_vectors(object2['object_pos'], object2['object_r'], position)
	# sector (t1, t2 ) contains t3 or t4
	theta = angle_between(t1, t2)	
	theta1 = angle_between(t1, t3)
	theta2 = angle_between(t2, t3)
	theta3 = angle_between(t1, t4)
	theta4 = angle_between(t2, t4)	
	d = 1E-3	
	t3_in_sector = abs((theta1 + theta2) - theta) < d
	t4_in_sector = abs((theta3 + theta4) - theta) < d
	if t3_in_sector or t4_in_sector:
		return True
	# sector (t3, t4 ) contains t1 or t2
	theta = angle_between(t3, t4)	
	theta1 = angle_between(t3, t1)
	theta2 = angle_between(t4, t1)
	theta3 = angle_between(t3, t2)
	theta4 = angle_between(t4, t2)	
	t1_in_sector = abs((theta1 + theta2) - theta) < d
	t2_in_sector = abs((theta3 + theta4) - theta) < d
	if t1_in_sector or t2_in_sector:
		return True
	return False


def object_within_tangents(t1, t2, object2, position):
	t3, t4 = tangent_vectors(object2['object_pos'], object2['object_r'], position)
	# sector (t1, t2 ) contains t3 or t4
	theta = angle_between(t1, t2)	
	theta1 = angle_between(t1, t3)
	theta2 = angle_between(t2, t3)
	theta3 = angle_between(t1, t4)
	theta4 = angle_between(t2, t4)	
	d = 1E-3	
	t3_in_sector = abs((theta1 + theta2) - theta) < d
	t4_in_sector = abs((theta3 + theta4) - theta) < d
	if t3_in_sector and t4_in_sector:
		return (t1, t2)
	if t3_in_sector: # t4 replaces t2
		return (t1, t4)
	if t4_in_sector: # t3 replaces t1
		return (t3, t2)
	# sector (t3, t4 ) contains t1 or t2
	theta = angle_between(t3, t4)	
	theta1 = angle_between(t3, t1)
	theta2 = angle_between(t4, t1)
	theta3 = angle_between(t3, t2)
	theta4 = angle_between(t4, t2)	
	t1_in_sector = abs((theta1 + theta2) - theta) < d
	t2_in_sector = abs((theta3 + theta4) - theta) < d
	if t1_in_sector and t2_in_sector:
		return (t3, t4)
	return tuple()


def objects_within_range(position, radius, state):	
	return [m for m in state["items"] if distance(position, m["object_pos"]) <= radius]	

	
def covered_objects(seed, vehicle_position, state, search_radius=-1):	
	""" Takes seed object and return all objects that forms overlapping structure"""
	start, end = tangent_vectors(seed['object_pos'], seed['object_r'], vehicle_position)
	objects = []
	for o in state["items"]:
		if o != seed:
			new_bounds = object_within_tangents(start, end, o, vehicle_position)			
			if new_bounds:
				start, end = new_bounds	
				objects.append(o)	
	return objects, start, end


def nearest_object(state, object_kind=None):
	position = state["vehicle_pos"]
	min_d = 1E6
	nearest = None
	if object_kind:
		objects = find_objects(object_kind, state)
	else:
		objects = state["items"]		
	for m in objects:
		target = m["object_pos"]
		d = distance(target, position)
		if d < min_d:
			nearest = m
			min_d = d	
	return nearest


def find_objects(object_kind, state):
	return [m for m in state["items"] if m["object_kind"] == object_kind]	


def objects_at_back(position, direction, state):
	return [m for m in state["items"] if angle_between(complex(cos(direction), sin(direction)), m["object_pos"] - position) < pi/2]	


def collision(p0, v0, p1, v1, near_future_t=2, same_time=1):
	t = - (p1 - p0) / (v1 - v0) if magnitude(v1 - v0) != 0 else 0+0j
	t_intersect = min(t.real, t.imag)
	d_intersect = t_intersect * v0
	p_intersect = p0 + d_intersect
	#~ print abs(t.imag - t.real), t
	will_collide = abs(t.imag - t.real) < same_time and 0 < t.imag and 0 < t.real
	#~ if will_collide:
		#~ print max(t.real, t.imag)
	soon = will_collide and max(t.real, t.imag) < near_future_t
	return dict(p=p_intersect, will_collide=will_collide, soon=soon, t=t_intersect)

def dot(complex1, complex2):
	return complex1.real * complex2.real + complex1.imag * complex2.imag

def polar_to_complex(mag, theta):
	return mag * (cos(theta) + 1j*sin(theta))

def c_unit(complex_num):
	return complex_num / magnitude(complex_num)

def c_to_t(complex_num):
	if isinstance(complex_num, complex):
		return complex_num.real, complex_num.imag
	else:
		return complex_num


def magnitude(complex_num):
	return sqrt(complex_num.real ** 2 + complex_num.imag ** 2)


def angle(complex_num):
	return math.atan2(complex_num.imag, complex_num.real)


def format_complex(complex_num):
	return "(%.2f, %.2f)" % (complex_num.real, complex_num.imag)


def distance(complex1, complex2):
	return magnitude(complex1 - complex2)

class BaseRover(object):
	pass

def main():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	main()
