#roller coaster

f = open("C-small-attempt0.in","r")
w = open("roll_out.txt","w")
N = int(f.readline())
for c in range(1, N+1):
	x = map(int, f.readline().split())
	R = x[0]
	k = x[1]
	g = map(int, f.readline().split())
	p = 0 #cost
	for j in range(0, R):
		n = 0
		for m in range(0,len(g)):
			if n + g[m] > k:
				g = g[m:] + g[0:m]
				break
			n += g[m]
		p += n
	w.write("Case #%d: %d\n" % (c,p))
f.close()
w.close()