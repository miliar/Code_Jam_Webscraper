v = [[int(n) for n in line.strip().split()] for line in open('b.in','r').readlines()]

nt = v[0][0]
v = v[1:]

#print(v)

out = open('b.out', 'w')

X, Y, Z, VX, VY, VZ = [0] * 6

def proc(t):
	global X, Y, Z, VX, VY, VZ
	return ((X + VX * t) ** 2 + (Y + VY * t) ** 2 + (Z + VZ * t) ** 2) ** 0.5

case = 0
while case < nt:
	case += 1
	N = v[0][0]
	fs = v[1:1 + N]
	v = v[1 + N:]
#	print(N, fs)
	X, Y, Z, VX, VY, VZ = [0] * 6
	for f in fs:
		X += f[0]
		Y += f[1]
		Z += f[2]
		VX += f[3]
		VY += f[4]
		VZ += f[5]
	a = VX * VX + VY * VY + VZ * VZ
	b = X * VX + Y * VY + Z * VZ
	c = X * X + Y * Y + Z * Z
	D = b * b - a * c
	if a != 0:
		if D <= 0:
			x = -b / a
			if x < 0: x = 0.0
		else:
			x = (-b + D ** 0.5) / a
			if x < 0: x = 0.0
	else:
		if b != 0:
			x = - c / (2 * b)
		else: x = 0.0
		if x < 0: x = 0.0
	print("Case #%d: %.8f %.8f" % (case, proc(x) / N, x), file = out)

'''
	t = 0.0
	while t < 7:
#		print(X, Y, Z, VX, VY, VZ)
		t += 1
'''
