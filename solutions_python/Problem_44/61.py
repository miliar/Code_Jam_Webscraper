import math

T = int(raw_input())
for T_count in range(T):
	N = int(raw_input())
	x, y, z, vx, vy, vz = 0, 0, 0, 0, 0, 0
	for N_count in range(N):
		line = raw_input().strip().split()
		x = x + int(line[0])
		y = y + int(line[1])
		z = z + int(line[2])
		vx = vx + int(line[3])
		vy = vy + int(line[4])
		vz = vz + int(line[5])
	x = float(x) / float(N)
	y = float(y) / float(N)
	z = float(z) / float(N)
	vx = float(vx) / float(N)
	vy = float(vy) / float(N)
	vz = float(vz) / float(N)
	try:
		t = -(x*vx + y*vy + z*vz) / ((vx**2) + (vy**2) + (vz**2))
	except:
		t = 0
	if t < 0:
		t = 0
	d = math.sqrt(((x + t*vx)**2) + ((y + t*vy)**2) + ((z + t*vz)**2))
	print 'Case #%d: %.8f %.8f' % (T_count + 1, d, t)

