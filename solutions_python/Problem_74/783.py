#!/usr/bin/env python 
import sys

class robot:
	def __init__(self, seq, name):
		self.seq = seq
		self.name = name
		self.cur = 0
		self.next = 0
		self.pos = 1

	def seek(self, cur, len):
		#print "cur is %s, %s's cur is %s" %(cur, self.name, self.cur) 
		if self.cur < cur or (self.cur == cur and self.seq[cur] != self.name):
			self.cur = self.cur + 2
			while self.cur < 2*len and self.seq[self.cur] != self.name :
				self.cur = self.cur + 2
			#print "%s is seeking next botton" %self.name
		if self.cur < 2 * len:
			self.next = int(self.seq[self.cur+1])
		#print "cur is %s, %s's cur is %s" %(cur, self.name, self.cur) 
			
	def move(self):
		if self.pos < self.next:
			self.pos = self.pos + 1
			#print "%s move to %s" %(self.name, self.pos)
		elif self.pos > self.next: 
			self.pos = self.pos - 1
			#print "%s move to %s" %(self.name, self.pos)
		#else:
			#print "%s stay at bottom %s" %(self.name, self.pos)

def getMinStep(seq, len):
	
	pressed = 0
	nstep = 0
	b = robot(seq, 'B')
	o = robot(seq, 'O')
	cur = 0

	while pressed < len:
		o.seek(cur, len)
		b.seek(cur, len)
		nstep = nstep + 1
		#print "step %s:" %nstep
		if cur == o.cur:
			if o.pos == o.next:
				cur = cur + 2
				pressed = pressed + 1
				#print "O press button %s" %o.pos
			else:
				o.move()
			b.move()
		else: # cur = b.cur
			if b.pos == b.next:
				cur = cur + 2 
				pressed = pressed + 1
				#print "B press button %s" %b.pos
			else:
				b.move()
			o.move()

	return nstep

if __name__ == '__main__':
	f = open('A-large.in')
	data = f.read().split()
	T = int(data[0])
	data = data[1:]
	for i in range(T):
		len = int(data[0])
		seq = data[1:1+len*2]
		data = data[1+len*2:]
		step = getMinStep(seq, len)
		print "Case #%s: %s" %(i+1, step)
		#print "******************************************************"
