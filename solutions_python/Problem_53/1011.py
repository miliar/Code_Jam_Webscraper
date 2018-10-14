#! /usr/bin/env python

"""
This program is part of "Google Code Jam Contest", a programming competition in which professional and student programmers are asked to solve complex algorithmic challenges in a limited amount of time.  
Visit http://code.google.com/codejam
"""

__author__ = "Rodrigo Augosto (rodrigo.augosto@gmail.com)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/05/07 14:47 $"

#############################
# Define Input/Output
#############################
file_in = open("SnapperChain/A-small.in", "r")
file_out = open("SnapperChain/A-small.out", "w")
file_buffer = []
result =[]
#############################
# Main Function
#############################
class Snapper(object):
	"A Snapper is a clever little device"
	def __init__(self, sin=None, state=None):
		self.sin = sin
		self.state = state
	def snap(self):
		self.changeState()
		self.change_out()
	def changeState(self):
		if self.sin == "yes" and self.state == "OFF":
			self.state = "ON"
		elif self.sin == "yes" and self.state == "ON":
			self.state = "OFF"
	def change_in(self, before):
		if before.sin == "yes" and before.state == "ON":
			self.sin = "yes"
		else:
			self.sin = "no"

def snapping(cases):
	light = "OFF"
	for case in range(0,int(cases)):
		snapperList = []
		snappers = file_buffer[case+1].split()[0]
		snaps = file_buffer[case+1].split()[1]

		for c in xrange(int(snappers)):
			if c == 0:
				snapperList.append(Snapper("yes", "OFF"))
			else:
				snapperList.append(Snapper("no", "OFF"))

		for s in xrange(int(snaps)):
			snapper_before = ""
			for lis in range(0, len(snapperList)):
				snapperList[lis].changeState()
				if lis > 0 :
					snapperList[lis].change_in(snapper_before)
				snapper_before = snapperList[lis]

		if snapperList[len(snapperList)-1].sin == "yes" and snapperList[len(snapperList)-1].state == "ON":
			light = "ON"
		else:
			light = "OFF"

		result.append("Case #" + str(case+1) + ": " + light + "\n")

#############################
# Reading Input
#############################
# Store file in a buffer
for line in file_in:
	file_buffer.append(line)
# Identify Cases
cases = file_buffer[0]
snapping(cases)
#############################
# Writing Output
#############################
file_out.writelines(result)
file_out.close()



