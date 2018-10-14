import math

def getClosest(n, fireflies):
	x, y, z = float(0), float(0), float(0)
	vx, vy, vz = float(0), float(0), float(0)

	for i in range(n):
		infos = fireflies[i].split(' ')
		x += float(infos[0])
		y += float(infos[1])
		z += float(infos[2])
		vx += float(infos[3])
		vy += float(infos[4])
		vz += float(infos[5])

	x = x / n
	y = y / n
	z = z / n
	vx = vx / n
	vy = vy / n
	vz = vz / n

	if vx == 0 and vy == 0 and vz == 0:
		tmin = 0
	else:
		tmin = (x*vx + y*vy + z*vz) / (vx*vx + vy*vy + vz*vz)
		tmin = tmin * (-1)

	if tmin <= 0:
		tmin = 0
		dmin = math.sqrt(x*x + y*y + z*z)
	else:
		dmin = math.sqrt( (vx*tmin+x)**2 + (vy*tmin+y)**2 + (vz*tmin+z)**2 )

	return (dmin, tmin)

import sys

fileNamePrefix = sys.argv[1]
fileNameIn = fileNamePrefix + ".in"
fileNameOut = fileNamePrefix + ".out"

fileIn = open(fileNameIn, 'r')
lines = fileIn.readlines()

testcnt = int(lines[0])
idx = 1

fileOut = open(fileNameOut, 'w')

for test in range(testcnt):
	n = int(lines[idx])
	idx += 1

	res = getClosest(n, lines[idx:idx+n])
	idx += n
	fileOut.write("Case #{0}: {1:.8f} {2:.8f}\n".format(test + 1, res[0], res[1]))
