import sys, math
from decimal import Decimal
debug = sys.stdout

sys.stdin  = open('B-small.in')
sys.stdout = open('B.out', 'w')

class LineSegment(object):
	def __init__(self, (t1, x1), (t2, x2)):
		self.t1 = Decimal(t1)
		self.t2 = Decimal(t2)
		self.x1 = Decimal(x1)
		self.x2 = Decimal(x2)
		self.v = (self.x2 - self.x1) / (self.t2 - self.t1)

	def contains(self, t):
		return self.t1 <= t < self.t2

	def xAt(self, t):
		return self.x1 + self.v * (t - self.t1)

	def tAt(self, x):
		return self.t1 + (x - self.x1) / self.v

	def __repr__(self):
		return "<Line from %s to %s>" % ((self.t1, self.x1), (self.t2, self.x2))

class ParabolaSection(object):
	def __init__(self, (t, x), v, a):
		self.t0 = Decimal(t)
		self.x0 = Decimal(x)
		self.v0 = Decimal(v)
		self.a =  Decimal(a)

	def vAt(self, t):
		return self.v0 + (t - self.t0) * self.a

	def xAt(self, t):
		dt = t - self.t0
		return self.x0 + self.v0*dt + 0.5*self.a*dt*dt

	def tAt(self, x):
		#px0 + pv0*t + 0.5*pa*t^2 == x
		a = self.a / 2
		b = self.v0
		c = self.x0 - x

		dt = (-b + (b*b - 4*a*c).sqrt()) / (2 * a)

		return self.t0 + dt


	def intersectionWith(self, l):
		lt = l.t1 - self.t0
		#px0 + pv0*t + 0.5*pa*t^2 == lx1 + lv(t - lt)
		#px0 + pv0*t + 0.5*pa*t^2 == lv * t + lx1 - lt * lv
		#(0.5*pa)t^2 + (pv0 - lv)t + (px0 - lx1 + lt * lv) == 0
		a = self.a / 2
		b = self.v0 - l.v
		c = self.x0 - l.x1 + lt * l.v

		dt = (-b + (b*b - 4*a*c).sqrt()) / (2 * a)
		t = self.t0 + dt

		return t if l.contains(t) else None

	def __repr__(self):
		return "<Parabola from %s, v=%f, a=%f>" % ((self.t0, self.x0), self.v0, self.a)

def solve(segments, a, d):
	car = ParabolaSection((0, 0), 0, a)

	for segment in segments:
		t = car.tAt(segment.x2)
		newT = segment.t2 - t

		if newT > car.t0:
			car.t0 = newT

	return car.tAt(d)
	"""
	for segment in segments:
		i = car.intersectionWith(segment)
		if i:
			car.v0 = segment.v
			car.t0 = segment.t2
			car.x0 = segment.x2
			#print >>debug, "Hit", segment
			#print >>debug, "Now at", car
			onLine = True
		else:
			onLine = False

	if onLine:
		return car.t0
	else:
		return car.tAt(d)"""

def segmentize(points, d):
	segments = [];
	for i in xrange(len(points) - 1):
		seg = LineSegment(points[i], points[i+1])
		t = seg.tAt(d)
		if t >= seg.t2:
			segments.append(seg)
		else:
			seg.x2 = d
			seg.t2 = t
			segments.append(seg)
			break


	return segments

for i in xrange(input()):
	d, n, a = raw_input().split(' ')
	d, n, a = Decimal(d), int(n), int(a)

	othercar = []
	for j in xrange(n):
		p = map(float, raw_input().split(' '))
		othercar.append(tuple(p))


	othercar = segmentize(othercar, d);

	#for x in range

	accelerations = map(float, raw_input().split(' '))

	print 'Case #%d:' % (i+1)
	for a in accelerations:
		print >>debug
		print >>debug, a, d
		print solve(othercar, a, d)