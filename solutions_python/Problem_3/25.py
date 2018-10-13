from __future__ import division
import psyco
from vector import *
import math
import random
import sys
import time
sys.stdin=file('qrcl.in')
vec = Vec2
def solve():
	case_n = input()
	for loop in xrange(case_n):
		fly, racket_r, racket_t, string_r, gap = (float(x) for x in raw_input().split())
		Gap = gap + string_r*2
		racket_ir = racket_r - racket_t - fly
		limit_area = racket_r**2*math.pi / 4 * 0.000001
		tt = time.time()
		def check(x1, y1, x2, y2):
			if x1>=x2 or y1 >= y2:
				return random.choice([-1,1])
			if x2**2+y2**2 <= racket_ir ** 2:
				return 1
			if x1**2+y1**2 >= racket_ir ** 2:
				return -1
			if ((x2-x1)*(y2-y1))<0.0001 * limit_area:
				return random.choice([-1,1])
			return 0

		def area(l):
			s = 0
			for i, p in enumerate(l):
				pp = l[i-1]
				s += pp[1] * p[0] - pp[0]*p[1]
			return abs(s)/2

		def compute_area(x1, y1, x2, y2):
			if x1 > x2:
				return 0
			c = check(x1, y1, x2, y2)
			if c == 1:
				return (x2-x1)*(y2-y1)
			elif c == -1:
				return 0
			else:
				# +-+ .
				# | |
				# +-+
				# .

				xm1 = (racket_ir**2-y1**2)**0.5
				xm2 = racket_ir**2-y2**2
				ym1 = (racket_ir**2-x1**2)**0.5
				ym2 = racket_ir**2-x2**2
				if xm1 > x2:
					if ym1 > y2:
						xm2 = xm2**0.5
						ym2 = ym2**0.5
						aa = abs(xm2*ym2-x2*y2)/2
						angle =  math.asin(2*aa/racket_ir/racket_ir)/2/math.pi
						return area([(x1,y1),(x1,y2),(xm2,y2),(x2,ym2),(x2,y1)]) + (racket_ir**2*math.pi*angle) - aa
					else:
						ym2 = ym2**0.5
						aa = abs(x2*ym1-ym2*x1)/2
						angle =  math.asin(2*aa/racket_ir/racket_ir)/2/math.pi
						return area([(x1,y1),(x1,ym1),(x2,ym2),(x2,y1)]) + (racket_ir**2*math.pi*angle) - aa
				else:
					if ym1 > y2:
						xm2 = xm2**0.5
						aa = abs(y2*xm1-xm2*y1)/2
						angle =  math.asin(2*aa/racket_ir/racket_ir)/2/math.pi
						return area([(x1,y1),(xm1,y1),(xm2,y2),(x1,y2)]) + (racket_ir**2*math.pi*angle) - aa
					else:
						aa = abs(y1*x1-xm1*ym1)/2
						angle =  math.asin(2*aa/racket_ir/racket_ir)/2/math.pi
						return (xm1-x1)*(ym1-y1)/2 + (racket_ir**2*math.pi*angle) - aa

		s = 0
		i = 0
		j = None
		incj = None
		while 1:
			x1 = i*Gap
			if x1 > racket_ir:
				break
			x2 = x1+Gap

			if j is None:
				j = 0
				incj = True
			else:
				incj = False
			while 1:
				y1 = j*Gap
				y2 = y1 + Gap
				if incj and x1**2+y1**2 > racket_ir**2:
					j+=1
					break
				if not incj and j < 0:
					break;
				cc =  compute_area(x1 + string_r + fly, y1 + string_r + fly, x2 - string_r - fly, y2 -string_r - fly)
				if not incj and x2**2+y2**2 < racket_ir**2:
					s += cc * (j+1)
					j += 1
					break
				s += cc

				if incj:
					j += 1
				else:
					j -= 1
			i += 1

		print "Case #%d: %.6f" % (loop+1, 1-s/(math.pi * racket_r ** 2 / 4))

psyco.full()
solve()

