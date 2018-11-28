#!/usr/bin/python
import sys

finput = sys.argv[1]
fi = open(finput)
num = int(fi.readline())

class bot():
	def __init__(self, name):
		self.name = name
		self.pos = 1
		self.obj = 1
		self.inplace = False

	def get_obj(self, objs):
		self.inplace = False
		for i in objs:
			if self.name == i[0]:
				self.obj = i[1]
				if self.pos == self.obj : self.inplace = True
				return
	def move(self):
		self.inplace = False
		if not self.pos == self.obj:
			self.pos += (self.obj-self.pos)/abs(self.obj-self.pos)
		if self.pos == self.obj : 
			self.inplace = True

def process(case):
	o = bot('O')
	b = bot('B')
	o.get_obj(case)
	b.get_obj(case)
	presser = case[0][0]
	steps = 0
	while not case == []:
		presser = case[0][0]
		steps += 1
		if presser == 'O' and o.inplace:
			case = case[1:]
			o.get_obj(case)
			b.move()
		elif presser == 'B' and b.inplace:
			case = case[1:]
			b.get_obj(case)
			o.move()
		else:
			o.move()
			b.move()
	return steps

for i in range(num):
	tmp = fi.readline().strip("\n").split()
	tmp = tmp[1:]
	case = []
	for j in range(len(tmp)/2):
		case += [[tmp[2*j],int(tmp[2*j+1])]]
	steps = process(case)
	print ("Case #%i: %i") % (i+1, steps)
