import sys
import time

def readnlines(file, n):
	ret = []
	for i in range(n):
		ret.append(file.readline().rstrip("\n\r"))
	return ret

def tomins(s):
	min, sec = time.strptime(s.rstrip(), "%M:%S")[4:6]
	return min*60 + sec

def case(file, n):
	A = []
	B = []
	turnaround = int(file.readline())
	na, nb = [int(i) for i in file.readline().split(" ")]

	maxa = 0; cura = 0; maxb = 0; curb = 0

	for i in range(na):
		a, b = file.readline().split(" ")
		A.append((tomins(a), 1))
		B.append((tomins(b) + turnaround, -1))
	for i in range(nb):
		b, a = file.readline().split(" ")
		A.append((tomins(a) + turnaround, -1))
		B.append((tomins(b), 1))
	
	A.sort()
	B.sort()
	for _, i in A:
		cura += i
		if maxa < cura: maxa = cura
	for _, i in B:
		curb += i
		if maxb < curb: maxb = curb

	print "Case #%d: %d %d" % (n, maxa, maxb)

f = file(sys.argv[1])
for i in range(int(f.readline())):
	case(f, i+1)
