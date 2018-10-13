#!/usr/bin/env python

#import numpy as np
import sys, os
import math
import itertools


class Robot(object):
	pos = 1
	def __init__(self, color, iterable):
		self.it = itertools.ifilter(lambda x: x[0] == color, iterable)
		self.color = color
		try:
			self.next_pos = self.it.next()[1]
		except StopIteration:
			self.next_pos = None
			
	def next(self):
		try:
			self.next_pos = self.it.next()[1]
		except StopIteration:
			self.next_pos = None
				
	
	def update(self, dest):
#		print self.color, "is at", self.pos, "dest", dest
		if self.pos < dest:
			self.pos += 1
		elif self.pos > dest:
			self.pos -= 1

		
def solve(line):
	N = int(line.pop(0))
		
	button_sequence = []
		
	for n in range(0, N*2, 2):
		button_sequence.append( (line[n], int(line[n+1])) )
	
#	print "button_sequence", button_sequence

	time = 0
	O = Robot('O', button_sequence)
	B = Robot('B', button_sequence)
	
	for button in button_sequence:
		this, other = (O, B) if button[0] == 'O' else (B, O)
		
#		print "objective:", button
		while button[0] != this.pos:
			time += 1
#			print "time", time
#			print 'othernext:', othernext
			if other.next_pos != None:
#				print other.color, "'s next_pos", other.next_pos
				other.update(other.next_pos)
			
			if this.pos == button[1]:
				this.next()
				break
			assert button[0] == this.color
			this.update(button[1])
		 
	return time



def main():
	rl = sys.stdin.readline
	T = int(rl())
				
	for t in xrange(T):
		print "Case #%i: %i" % (t+1, solve(rl().split()))
					
			
		
		
main()