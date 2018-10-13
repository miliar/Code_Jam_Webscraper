import math

def test(r, t):
	root = math.sqrt(t)
	floor = int(math.floor(root))
	if (floor - r - 1) % 2 == 1:
		floor -= 1
	p = max(floor, r+1)
	while (p+r)*(p-r+1) <=2*t:
		p += 2
	return (p - r - 1) / 2	

def main():
	f = open("./A-small-attempt0.in")
	n = int(f.readline())
	for i in range(1, n+1):
		line = f.readline().split()
		r, t = int(line[0]), int(line[1])
		print "Case #%d: %d" % (i, test(r,t))

main()