from math import atan2, sin, pi

def incircle(x, y, r):
	return x * x + y * y <= r * r

def findx(x, r):
	return (r * r - x * x) ** .5
	
def area(x, y, a, r):
	ina = incircle(x, y, r)
	inb = incircle(x, y + a, r)
	inc = incircle(x + a, y + a, r)
	ind = incircle(x + a, y, r)
	if not ina: return 0
	if inc: return a * a
	if not inb and not ind:
		x1 = x
		y1 = findx(x, r)
		x2 = findx(y, r)
		y2 = y
		al = atan2(y1, x1) - atan2(y2, x2)
		if (al < 0): raise ValueError
		s = r * r * (al - sin(al)) / 2
		return s + (x2 - x1) * (y1 - y2) / 2
	if inb and not ind:
		x1 = findx(y + a, r)
		y1 = y + a
		x2 = findx(y, r)
		y2 = y
		al = atan2(y1, x1) - atan2(y2, x2)
		if (al < 0): raise ValueError
		s = r * r * (al - sin(al)) / 2
		return s + a * (x1 - x + x2 - x) / 2
	if not inb and ind:
		x1 = x
		y1 = findx(x1, r)
		x2 = x + a
		y2 = findx(x2, r)
		al = atan2(y1, x1) - atan2(y2, x2)
		if (al < 0): raise ValueError
		s = r * r * (al - sin(al)) / 2
		return s + a * (y1 - y + y2 - y) / 2
	if inb and ind:
		y1 = y + a
		x1 = findx(y1, r)
		x2 = x + a
		y2 = findx(x2, r)
		al = atan2(y1, x1) - atan2(y2, x2)
		if (al < 0): raise ValueError
		s = r * r * (al - sin(al)) / 2
		return a * a - (x + a - x1) * (y + a - y2) / 2 + s
	raise ValueError

if __name__ == "__main__":
	N = int(raw_input())
	for test in range(N):
		(f, R, t, r, g) = map(float, raw_input().split())
		a = g - f - f
		inr = R - t - f
		if (a <= 0 or inr <= 0):
			print "Case #%d: %.6f" % (test + 1, 1)
			continue
		gap = (g + r + r)
		c = int(R / gap) + 2
		res = 0
		for i in range(c):
			for j in range(c):
				x = r + gap * i
				y = r + gap * j
				ar = area(x + f, y + f, a, inr)
				if ar < 0: raise ValueError
				if ar > a * a: raise ValueError
				res += ar
		res *= 4
		res /= pi * R * R
		print "Case #%d: %.6f" % (test + 1, 1 - res)
