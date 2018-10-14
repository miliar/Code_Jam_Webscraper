#!/usr/bin/python

import sys

class Snapper:
	def __init__(self):
		self.on = False
		self.powered = False

	def inputPowerChanged(self, newState):
		self.powered = newState

	def snap(self):
		if self.powered:
			self.on = not self.on

class SnapperSolver:
	def __init__(self):
		self.testCases = []
		self.results = []


	def readInput(self, filename):
		input = file(filename, "r")
		testNum = int(input.readline())
		for i in xrange(testNum):
			line = input.readline()
			lineItems = line.split(' ')
			self.testCases.append((int(lineItems[0]), int(lineItems[1])))
		input.close()

	def solveCase(self, snappers, snaps):
		if snaps == 0:
			return False

		# generate snapper chain
		self.snappers = []
		for i in xrange(snappers):
			self.snappers.append(Snapper())
		self.snappers[0].inputPowerChanged(True)

		# simulate snaps
		for i in xrange(snaps):
                        previousGivesPower = True
			for snapper in self.snappers:
				snapper.snap()
				snapper.inputPowerChanged(previousGivesPower)
				previousGivesPower = snapper.on and snapper.powered

                return previousGivesPower

	def solveCases(self):
		for N, K in self.testCases:
			self.results.append(self.solveCase(N, K))

	def printOutput(self):
		resultCounter = 1
		for result in self.results:
			print "Case #%d:" % resultCounter,
			if result:
				print "ON"
			else:
				print "OFF"
			resultCounter += 1


if __name__ == '__main__':
	solver = SnapperSolver()
	solver.readInput(sys.argv[1])
	solver.solveCases()
	solver.printOutput()
