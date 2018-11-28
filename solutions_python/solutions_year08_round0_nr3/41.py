#!/usr/bin/python
from math import hypot, asin, acos, sin, sqrt, pi

def side(theta, Ri):
	return (theta-sin(theta))*Ri*Ri/2.0

n = int(raw_input())
for i in xrange(1,n+1):
	f, R, t, r, g = [float(s) for s in raw_input().split()]
	Ri = R - t - f
	if Ri <= 0.0 or g-2*f <= 0.0:
		print "Case #%d: 1.000000" % (i,)
		continue
	safe = 0.0
	x = 0.0
	while r+f+x*(2*r+g) < Ri:
		y = 0.0
		while hypot(r+f+x*(2*r+g), r+f+y*(2*r+g)) < Ri:
			x1, x2 = r+f+x*(2*r+g), r+g-f+x*(2*r+g)
			y1, y2 = r+f+y*(2*r+g), r+g-f+y*(2*r+g)
			if hypot(x2, y2) <= Ri:
				safe += (g-2*f)*(g-2*f)
			elif hypot(x2, y1) <= Ri and hypot(x1, y2) <= Ri:
				angle = asin(y2 / Ri) - acos(x2 / Ri)
				xcut = x2-sqrt(Ri*Ri-y2*y2)
				ycut = y2-sqrt(Ri*Ri-x2*x2)
				safe += (g-2*f)*(g-2*f) - xcut*ycut/2.0 + side(angle, Ri)
			elif hypot(x2, y1) <= Ri:
				angle = acos(x1 / Ri) - acos(x2 / Ri)
				x1cut = sqrt(Ri*Ri-x1*x1) - y1
				x2cut = sqrt(Ri*Ri-x2*x2) - y1
				safe += (g-2*f) * (x1cut+x2cut) / 2.0 + side(angle, Ri)
			elif hypot(x1, y2) <= Ri:
				angle = asin(y2 / Ri) - asin(y1 / Ri)
				y1cut = sqrt(Ri*Ri-y1*y1) - x1
				y2cut = sqrt(Ri*Ri-y2*y2) - x1
				safe += (g-2*f) * (y1cut+y2cut) / 2.0 + side(angle, Ri)
			else:
				angle = acos(x1 / Ri) - asin(y1 / Ri)
				xcut = sqrt(Ri*Ri-y1*y1) - x1
				ycut = sqrt(Ri*Ri-x1*x1) - y1
				safe += xcut*ycut/2.0 + side(angle, Ri)
			y += 1.0
		x += 1.0
	print "Case #%d: %.6f" % (i, 1.0-safe/(pi*R*R/4.0))