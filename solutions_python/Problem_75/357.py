#!/usr/bin/env python

from collections import deque

global debug,data,C,D,N

class elist:
	def __init__(self, name):
		self.name = name
		self.matrix = [[0 for col in range(26)] for row in range(26)]

	def add(self, sp):
		global debug
		if debug: print "%s: add %s [" % (self.name, sp),

		r = ord(sp[0])-65
		c = ord(sp[1])-65

		if (self.name == "create"):
			if debug: print "%s ][ %s ] = %s" % (r,c,sp[2])
			self.matrix[r][c] = sp[2]
			self.matrix[c][r] = sp[2]
		elif (self.name == "destroy"):
			if debug: print "%s ][ %s ] = %d" % (r,c,1)
			self.matrix[r][c] = 1
			self.matrix[c][r] = 1

	def find(self, x, y):
		global debug

		r = ord(x)-65
		c = ord(y)-65

		return self.matrix[r][c]

	def find_all(self, x, inv):
		global debug

		r = ord(x)-65
		for y in inv:
			c = ord(y)-65
			if (self.matrix[r][c]):
				return True

		return False


def parse():
	global debug,data,C,D,N
	if debug: print "data =",data

	#create element pairings
	for i in range(0,int(data.popleft())):
		C.add(data.popleft())

	#destroy element pairings
	for i in range(0,int(data.popleft())):
		D.add(data.popleft())

	#invokation list
	data.popleft() #get rid of invokation list size
	N = str(data.popleft())
	if debug: print "invoke: %s" % N

def eval():
	global debug,output,C,D,N

	for e in N:
		if (len(output) == 0):
			if debug: print "add", e
			output.append(e)
		elif (C.find(e,output[len(output)-1])):
			f = output.pop()
			if debug: print "morph %s + %s = %s" % (e,f,C.find(e,f))
			output.append(C.find(e,f))
		elif (D.find_all(e,output)): #should've polymorphed into children objects and overloaded find
			if debug: print "erase output"
			output = []
		else:
			if debug: print "add", e
			output.append(e)


def main():
	global debug,data,output,C,D,N
	debug = False
	cases = int(raw_input())

	for n in range(1,cases+1):
		data = []
		output = []
		C = elist("create")
		D = elist("destroy")
		N = ""

		data = raw_input().split()
		data = deque(data)

		parse()
		eval()

		print "Case #%s: [%s]" % (n, ', '.join(str(x) for x in output))
		#for o in range(0,len(output)):
			#print output[o],
			#if (o != len(output)-1):
				#print ",",
		#print "]"

	return 0

main()
