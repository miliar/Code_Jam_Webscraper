

f = open("B-small-attempt0.in")
cases = int(f.readline())
for j in range(cases):
	data = list(map(float,f.readline().split(" ")))
	C = data[0]
	F = data[1]
	X = data[2]

	totalSec = 0
	fabs = 1
	totalWithoutFabs = X/2.0
	minim = totalWithoutFabs
	k=0

	while 1:
		fabTime = 0
		for i in range(1,fabs+1):
			fabTime += C/(2.0 + (i-1)*F)
		totalWithFabs = X/(2.0 + (fabs)*F)
		total = fabTime+totalWithFabs
		fabs += 1
		if total < minim:
			minim = total
		if total > totalWithoutFabs or total > minim:
			break
		k += 1

	print "Case #" + str(j+1) + ": " + str(minim)

