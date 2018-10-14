import sys

from math import *

class point(object):
	def __init__(self, x = 0, y = 0, r = 0):
		self.x = x
		self.y = y
		self.r = r
	def __str__(self):
		return 'x=%f, y=%f, r=%f' % (self.x, self.y, self.r)

class test_case(object):
	def __init__(self, f, R, t, r, g):
		self.__f = f
		self.__R = R
		self.__t = t
		self.__r = r
		self.__g = g
		return

	def __get_cell_points(self, col, row):
		x = y = 0

		xn = self.__r + col * (2 * self.__r + self.__g) + self.__f
		yn = self.__r + row * (2 * self.__r + self.__g) + self.__f

		xf = xn + self.__g - 2 * self.__f
		yf = yn + self.__g - 2 * self.__f

		near = point(xn, yn, sqrt(pow(xn, 2) + pow(yn, 2))) 
		far = point(xf, yf, sqrt(pow(xf, 2) + pow(yf, 2)))
		upper = point(xn, yf, sqrt(pow(xn, 2) + pow(yf, 2)))
		lower = point(xf, yn, sqrt(pow(xf, 2) + pow(yn, 2)))

		return (near, far, upper, lower)

	def __get_sector_area(self, p1, p2, r):
		k1 = (p2.x - p1.x)
		k2 = (p1.y - p2.y)
		c = sqrt(pow(k1, 2) + pow(k2, 2))
		fi = acos(1 - pow(c, 2) / (2 * pow(r, 2)))
		area = (pow(r, 2) / 2) * (fi - sin(fi))
		return area 

	def __get_fly_passable_area(self):
		area = 0

		inner_radius = self.__R - self.__t - self.__f
		max_index = int(ceil(inner_radius / (self.__g + 2 * self.__r))) 

		for row in xrange(max_index):
			for col in xrange(max_index):
				(near, far, upper, lower) = self.__get_cell_points(col, 
					row)
				if far.r < inner_radius:
					qf = (self.__g - 2 * self.__f) 
					if qf > 0: area += pow(qf, 2)
				elif near.r < inner_radius:
					c1 = point()	
					c2 = point()
					if lower.r <= inner_radius and upper.r <= inner_radius:
						c1.x = sqrt(pow(inner_radius, 2) - pow(upper.y, 2))
						c1.y = upper.y
						c2.x = lower.x
						c2.y = sqrt(pow(inner_radius, 2) - pow(lower.x, 2))

						area += (c1.x - upper.x) * (c1.y - c2.y)
						area += (c2.x - c1.x) * (c2.y - lower.y)
						area += (c1.x - upper.x) * (c2.y - lower.y)
					elif lower.r >= inner_radius and upper.r <= inner_radius:
						c1.x = sqrt(pow(inner_radius, 2) - pow(upper.y, 2))
						c1.y = upper.y
						c2.x = sqrt(pow(inner_radius, 2) - pow(lower.y, 2))
						c2.y = lower.y

						area += (c1.x - upper.x) * (c1.y - c2.y)
						#area += (lower.x - c2.x) * (c1.y - c2.y)
					elif lower.r <= inner_radius and upper.r >= inner_radius:
						c1.x = upper.x
						c1.y = sqrt(pow(inner_radius, 2) - pow(upper.x, 2))
						c2.x = lower.x
						c2.y = sqrt(pow(inner_radius, 2) - pow(lower.x, 2))

						area += (c2.x - c1.x) * (c2.y - lower.y)
						#area += (c2.x - c1.x) * (upper.y - c1.y)
					else:
						c1.x = upper.x
						c1.y = sqrt(pow(inner_radius, 2) - pow(upper.x, 2))
						c2.x = sqrt(pow(inner_radius, 2) - pow(lower.y, 2))
						c2.y = lower.y
					area += (c2.x - c1.x) * (c1.y - c2.y) / 2
					area += self.__get_sector_area(c1, c2, inner_radius)
	
		return area * 4

	def run(self):
		r = 0
		full_area = pow(self.__R, 2)  * pi
		if full_area > 0:
			r = float(self.__get_fly_passable_area()) / full_area
		return (1 - r)

def process_case(index, file):
	d = []
	for s in file.readline().split():
		d.append(float(s))

	tc = test_case(d[0], d[1], d[2], d[3], d[4])
	r = tc.run()

	print 'Case #%i: %f' % (index, r)
	return

def main(argv):
	for input_file_name in argv:
		input_file = open(input_file_name, 'r')
		try:
			n = int(input_file.readline())
			for i in xrange(n):
				process_case(i + 1, input_file)
		finally:
			input_file.close()
	return

if __name__ == '__main__':
	#import pdb
	#pdb.set_trace()
	main(sys.argv[1:])
