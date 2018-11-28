import math

for tc in range(1, int(input()) + 1):
	n = int(input())
	X = 0
	Y = 0
	Z = 0
	VX = 0
	VY = 0
	VZ = 0
	for _ in range(n):
		x, y, z, vx, vy, vz = map(float, input().split())
		X += x
		Y += y
		Z += z
		VX += vx
		VY += vy
		VZ += vz
	X /= n
	Y /= n
	Z /= n
	VX /= n
	VY /= n
	VZ /= n
	
	sqr = lambda x: x*x
	A = sqr(VX) + sqr(VY) + sqr(VZ)
	B = 2*(VX*X + VY*Y + VZ*Z)
	C = sqr(X) + sqr(Y) + sqr(Z)
	
	if A == 0:
		print("Case #%d: %.8f %.8f" % (tc, math.sqrt(C), 0))
		continue
	
	tmin = -B/(2*A)
	if tmin <= 0.0:
		tmin = 0.0
	dmin = A*sqr(tmin) + B*tmin + C
	if dmin <= 0.0:
		dmin = 0.0
	
	print("Case #%d: %.8f %.8f" % (tc, math.sqrt(dmin), tmin))
	
	