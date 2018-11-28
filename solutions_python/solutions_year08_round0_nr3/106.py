import math

inp = file("C-small-attempt0.in")
#inp = file("C-large.in")
result = file("C-small-attempt0.out", "w")
#result = file("C-large.out", "w")

def sgn(x):
	if x < 0:
		return -1
	else:
		return 1

def CircleLineIntersect(x1, y1, x2, y2, r):
	dx = x2 - x1
	dy = y2 - y1
	dr = math.sqrt(dx * dx + dy * dy)
	d = x1 * y2 - x2 * y1
	disc = r * r * dr * dr - d * d
	
	if disc <= 0:
		return None	
		
	diff_x = sgn(dy) * dx * math.sqrt(disc)
	diff_y = abs(dy) * math.sqrt(disc)
	
	return (
		((d * dy + diff_x) / (dr * dr), (-d * dx + diff_y) / (dr * dr)),
		((d * dy - diff_x) / (dr * dr), (-d * dx - diff_y) / (dr * dr))
		)
	
def CircleSquareIntersect(x1, y1, x2, y2, r):
	r1 = math.sqrt(x1 * x1 + y1 * y1)
	r2 = math.sqrt(x2 * x2 + y2 * y2)
	
	if r1 >= r:
		return 0
	
	if r2 <= r:
		return (x2 - x1) * (y2 - y1)

	poly = [(x1, y1)]
	i1 = None
	i2 = None
	
	p = CircleLineIntersect(x1, y1, x1, y2, r)
	
	if p and p[0][1] >= y1 and p[0][1] <= y2:
		i1 = p[0]
		poly.append(i1)
	elif p and p[1][1] >= y1 and p[1][1] <= y2:
		i1 = p[1]
		poly.append(i1)
	else:
		poly.append((x1, y2))
		
	p = CircleLineIntersect(x1, y2, x2, y2, r)

	if p and p[0][0] >= x1 and p[0][0] <= x2:
		i1 = p[0]
		poly.append(i1)
	elif p and p[1][0] >= x1 and p[1][0] <= x2:
		i1 = p[1]
		poly.append(i1)

	p = CircleLineIntersect(x2, y2, x2, y1, r)
	
	if p and p[0][1] >= y1 and p[0][1] <= y2:
		i2 = p[0]
		poly.append(p[0])
	elif p and p[1][1] >= y1 and p[1][1] >= y2:
		i2 = p[0]
		poly.append(p[1])
		
	if i2:	
		poly.append((x2, y1))
	
	p = CircleLineIntersect(x2, y1, x1, y1, r)
	
	if p and p[0][0] >= x1 and p[0][0] <= x2:
		i2 = p[0]
		poly.append(p[0])
	elif p and p[1][0] >= x1 and p[1][0] <= x2:
		i2 = p[1]
		poly.append(p[1])
		
	#print poly

	a = 0
	for i in range(len(poly)):
		p1 = poly[i]
		if i < len(poly) - 1:
			p2 = poly[i + 1]
		else:
			p2 = poly[0]
			
		det = p1[1] * p2[0] - p2[1] * p1[0]
		
		a += det
		
	a *= 0.5

	# area of curved addition
	angle1 = math.acos(i1[0] / r)	
	angle2 = math.acos(i2[0] / r)
	
	angle = angle1 - angle2
	
	circle_area = math.pi * r * r
	slice_area = (angle / (math.pi * 2)) * circle_area
	
	x1 = 0
	y1 = 0
	x2 = i1[0]
	y2 = i1[1]
	x3 = i2[0]
	y3 = i2[1]
	#print "tri", x1, y1, x2, y2, x3, y3
	triangle_area = x2 * y1 - y2 * x1 + x3 * y2 - y3 * x2 + x1 * y3 - y1 * x3
	triangle_area *= 0.5
	
	#print triangle_area

	a += slice_area - triangle_area
	
	return a


		
def calc(f, bigR, t, r, g):
	area = 0
	
	x = r + f
	while x < bigR:
		y = r + f
		
		while y < bigR:
			x1 = x
			y1 = y
			x2 = x + (g - 2.0 * f)
			y2 = y + (g - 2.0 * f)
			
			a = CircleSquareIntersect(x1, y1, x2, y2, bigR - t - f)
			area += a
			#print x1, y1, x2, y2, a
			
			y += g + 2 * r
			
		x += g + 2 * r		


	return 1.0 - area / (bigR * bigR * math.pi * 0.25)
	
	
cases = int(inp.readline())
for case in range(cases):
	line = inp.readline()
	line = line.strip()
	values = line.split()
	
	f = float(values[0])
	bigR = float(values[1])
	t = float(values[2])
	r = float(values[3])
	g = float(values[4])
	
	r = calc(f, bigR, t, r, g)
	result.write("Case #" + str(case + 1) + ": " + str(r) + "\n")