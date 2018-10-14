#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Code to solve Google Code Jam problem "Bot Trust" of 2011/may/07"""

import sys

class Robot:
	"""The definition of a robot"""
	def __init__(self, color, position):
		self.color = color
		self.position = position
	def moveTo(self, newPosition):
		"""Moves the robot to a new position, returning the cost (in seconds) to move there"""
		cost = abs(self.position - newPosition)
		self.position = newPosition
		return cost

if __name__ == "__main__":
	with open(sys.argv[1]) as input:
		with open(sys.argv[1] + ".out", "w") as output:
			cases = int(input.readline())
			for case in xrange(1, cases + 1):
				# print "starting case {0}".format(case)	

				# prepare robots
				blue = Robot("B", 1)
				orange = Robot("O", 1)
				robots = [blue, orange]

				# test variables
				currentRobot = None		
				accumulatedCost = 0
				totalCost = 0

				testData = input.readline().split()
				buttons = int(testData[0])
				# print "{0} buttons to press".format(buttons)

				for i in xrange(1, buttons * 2, 2):
					color = testData[i]
					button = int(testData[i + 1])

					robot = [r for r in robots if r.color == color][0]
					# print "robot {0}".format(robot.color)

					if currentRobot == None  or currentRobot == robot:

						# same robot, keep addding costs
						roundCost = robot.moveTo(button)
						currentRobot = robot
					else:

						# other robot, subtract accumulated cost
						roundCost = max(robot.moveTo(button) - accumulatedCost, 0)

						accumulatedCost = 0
						currentRobot = robot

					# button press cost
					roundCost += 1

					accumulatedCost += roundCost
					totalCost += roundCost

					# print "roundCost: {0}, accumulatedCost: {1}, totalCost: {2}".format(roundCost, accumulatedCost, totalCost)

				print "Case #{0}: {1}".format(case, totalCost)
				output.write("Case #{0}: {1}\n".format(case, totalCost))
