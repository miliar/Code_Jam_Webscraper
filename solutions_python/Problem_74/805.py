#!/usr/bin/env python

from __future__ import print_function
import sys

class Robot:
	def __init__(self):
		self.goals = list()
		self.pos   = 1
	
	def has_goal(self):
		return len(self.goals) > 0
	
	def step(self, turn):
		# press the button if it's our turn
		if self.has_goal() and self.pos == int(self.goals[0]) and turn:
			del self.goals[0]
			return True
		# move towards the next goal
		elif self.has_goal() and self.pos < int(self.goals[0]):
			self.pos += 1
		elif self.has_goal() and self.pos > int(self.goals[0]):
			self.pos -= 1
		return False

def tokenize(f, delim = [ ' ', '\n' ]):
	token = list()

	while True:
		ch = f.read(1)
		if ch == '':
			yield ''.join(token)
			raise StopIteration
			token = list()
		elif ch in delim:
			yield ''.join(token)
			token = list()
		else:
			token.append(ch)


tokens = tokenize(sys.stdin)
T      = int(tokens.next())

for t in xrange(0, T):
	robots = dict()
	actors = list()

	# build a list of goals for each robot
	N = int(tokens.next())
	for n in xrange(0, N):
		robot, button = tokens.next(), tokens.next()

		if robot not in robots:
			robots[robot] = Robot()

		robots[robot].goals.append(button)
		actors.append(robot)

	# simulate optimal movement
	time = 0
	while len(actors) > 0:
		actor_turn = actors[0]
		for actor, robot in robots.items():
			pressed = robot.step(actor == actor_turn)
			if pressed:
				del actors[0]
		time += 1

	print('Case #{0}: {1}'.format(t + 1, time))

