from sympy.solvers import solve
from sympy import Symbol

class Horses(object):
	def __init__(self, d, n):
		self.d = d
		self.n = n
		self.pos = []
		self.vel = []

	def addHorse(self, pos, vel):
		self.pos.append(pos)
		self.vel.append(vel)

	def battle(self):
		p1 = self.pos[0]
		p2 = self.pos[1]
		v1 = self.vel[0]
		v2 = self.vel[1]
		d = self.d
		if v1 == v2:
			if p1 < p2:
				del self.pos[1]
				del self.vel[1]
			else:
				del self.pos[0]
				del self.vel[0]
		else:
			x = Symbol('x')
			T = solve(p1 - p2 + x * (v1 - v2), x)
			t = T[0]
			if t < 0:
				if p1 < p2:
					del self.pos[1]
					del self.vel[1]
				else:
					del self.pos[0]
					del self.vel[0]
			elif t * v1 + p1 < d:
				if p1 < p2:
					del self.pos[0]
					del self.vel[0]
				else:
					del self.pos[1]
					del self.vel[1]
			else: 
				if p1 < p2:
					del self.pos[1]
					del self.vel[1]
				else: 
					del self.pos[0]
					del self.vel[0]
		self.n -= 1

	def getSpeed(self):
		p = self.pos[0]
		v = self.vel[0]
		d = self.d
		t = (d - p) / v
		return d / t


infile = open("input_file.txt", 'r')
outfile = open("output_file.txt", 'w')

T = int(infile.readline())
for i in range(T):
	inStr = infile.readline().split()
	d = int(inStr[0])
	n = int(inStr[1])
	h = Horses(d, n)
	for j in range(n):
		inStr2 = infile.readline().split()
		pos = int(inStr2[0])
		vel = int(inStr2[1])
		h.addHorse(pos, vel)
	while h.n > 1:
		h.battle()
	outfile.write("Case #" + str(i + 1) + ": " + str(h.getSpeed()) + "\n")
