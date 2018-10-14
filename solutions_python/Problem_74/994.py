#!/usr/bin/python
# coding: UTF-8

import sys

class robot():
	def __init__(self,color,case):
		self.color = color
		self.place = 1
		self.flag = False
		self.case = case

def ifB():
	#print '\t\t',
	pass

def move(robot):
	if robot.color == 'B': ifB()
	#print robot.color + ' move ' + str(robot.place) + ' to ',
	robot.place += 1
	#print str(robot.place)

def back(robot):
	if robot.color == 'B': ifB()
	#print robot.color + ' move ' + str(robot.place) + ' to ',
	robot.place -= 1
	#print str(robot.place)

def push(robot):
	if robot.color == 'B': ifB()
	#print robot.color + ' push ' + str(robot.place)

def stay(robot):
	if robot.color == 'B': ifB()
	#print robot.color + ' stay ' + str(robot.place)

def Main(robot,n):
	if not robot.case[0][0] == n:
		sys.stderr.write('Error:\n')
		quit()
	P = robot.case[0][1]
	add_time = 0
	while robot.place != P:
		if robot.place < P: move(robot)
		elif robot.place > P: back(robot)
		add_time += 1
	push(robot)
	add_time += 1
	robot.case.pop(0)
	return add_time

def Sub(robot,n,add_time):
	add = 0
	if robot.case:
		while robot.place != robot.case[0][1]:
			if robot.place < robot.case[0][1]: move(robot)
			elif robot.place > robot.case[0][1]: back(robot)
			add += 1
			if add == add_time:
				break
	while add < add_time:
		stay(robot)
		add += 1

f = open(sys.argv[1])
lines = f.readlines()
f.close()

cases = []
for l in lines[1:]:
	ll = l[:-1].split()
	case = [ (n,ll[2*n+1],int(ll[2*n+2])) for n in range(len(ll)/2)]
	cases.append(case)

case = 1
for c in cases:
	s = 'Case #' + str(case) + ': '
	time = 0
	colorOrder = [ button[1] for button in c]
	Ocase = [ (button[0], button[2]) for button in c if button[1] == 'O']
	Bcase = [ (button[0], button[2]) for button in c if button[1] == 'B']
	O = robot('O',Ocase)
	B = robot('B',Bcase)

	for n in range(len(colorOrder)):
		clr = colorOrder[n]
		#print '\t***   ' + clr + '   ***'
		if clr == 'O':
			add_time = Main(O,n)
			Sub(B,n,add_time)
			time += add_time
		elif clr == 'B':
			add_time = Main(B,n)
			Sub(O,n,add_time)
			time += add_time

	s += str(time)
	print s
	case += 1
