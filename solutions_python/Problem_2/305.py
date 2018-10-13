import os, sys

class Time:
	def __init__(self, tstr, dep, station):	
		h, m = tstr.strip().split(":")
		self.h, self.m = int(h), int(m)
		self.dep = dep
		self.station = station
	def __repr__(self):
		a = ""
		if self.dep: a = "departing"
		else: a = "arriving"
		s = ""
		if self.station == 0:
			s = "A"
		elif self.station == 1:
			s = "B"
		else:
			raise "WTF Mate?"
		return "%d:%d = %d %s station %s" % (
			self.h, self.m, self.value(), a, s)
	def __cmp__(self, other):
		#self - other
		if (self.value() == other.value()):
			if (self.dep == False and other.dep == False):
				return 0
			elif (self.dep == True and other.dep == True):
				return 0
			elif (self.dep == True and other.dep == False):
				return 1
			elif (self.dep == False and other.dep == True):
				return -1
		else:
			return self.value() - other.value()

	def value(self):
		t = (self.h * 60) + self.m
		return t
	def add(self, mins):
		self.m += mins
	
class Case:
	def __init__(self, tat, na, nb):
		self.tat = tat
		self.times = []
		for x in na:
			a, b = x.split(' ')
			a, b = a.strip(), b.strip()
			self.times.append(Time(a, True, 0))
			t = Time(b, False, 1)	
			t.add(self.tat)
			self.times.append(t)
		for x in nb:
			a, b = x.split(' ')
			a, b = a.strip(), b.strip()
			self.times.append(Time(a, True, 1))
			t = Time(b, False, 0)
			t.add(self.tat)
			self.times.append(t)
		self.times.sort()
	def __repr__(self):
		return str(self.times)
	def solve(self):
		s = Station()
		for x in self.times:
			s.process(x)
		return s.result()
			
class Station:
	def __init__(self):
		self.waiting = [0, 0]
		self.needed = [0,0]
	def process(self, time):
		if time.dep:
			if self.waiting[time.station]:
				self.waiting[time.station] -= 1
			else: self.needed[time.station] += 1
		else:
			self.waiting[time.station] += 1
	def result(self):
		return (self.needed[0], self.needed[1])
					
				

if __name__ == "__main__":
	n = int(sys.stdin.readline())
	cases = []
	for x in range(n):
		tat = int(sys.stdin.readline())
		na, nb = [], []
		ca, cb = sys.stdin.readline().split(' ')
		ca, cb = int(ca), int(cb)
		for y in range(ca):
			na.append(sys.stdin.readline())
		for z in range(cb):
			nb.append(sys.stdin.readline())
		cases.append(Case(tat, na, nb))
	c = 1
	for x in cases:
		a, b = x.solve()
		print "Case #%d: %d %d" % (c, a, b)
		c += 1
