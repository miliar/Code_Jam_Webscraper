import sys

T=int(sys.stdin.readline())
INF = 10000000000

def good1(cx, cy, d):
#	print cx, cy, d
	fx = cx-d
	lx = cx+d
	fy = cy-d
	ly = cy+d
	return good0(fx, lx, fy, ly, cx, cy, d)

def good2(cx, cy, d):
#	print cx, cy, d
	fx = cx-d+1
	lx = cx+d
	fy = cy-d+1
	ly = cy+d
	return good0(fx, lx, fy, ly, cx+0.5, cy+0.5, d)

def good0(fx, lx, fy, ly, cx, cy, d):
	if fx<0 or lx >= R or fy < 0 or ly >= C:
#		print "sz", fx, lx, fy, ly
		return False
	kx = 0
	ky = 0
	for x in range(fx, lx+1):
		for y in range(fy, ly+1):
			if not (x == fx and y == fy or x==lx and y==fy or x==fx and y==ly or x==lx and y==ly):
				kx += (cx-x)*W[x][y]
				ky += (cy-y)*W[x][y]
#	print kx, ky
	return kx == 0 and ky == 0


for case in range(T):
	print "Case #%d:" % (case+1),
	R, C, D = map(int, sys.stdin.readline().split(' '))
	
	W = []
	for i in range(R):
		W.append(map(int, list(sys.stdin.readline().strip())))
#	print W

	mx = 0
	for cx in range(R):
		for cy in range(C):
			for d in range(min(R,C), 0, -1):
				if mx < d*2+1 and good1(cx, cy, d):
#					print "good1", cx, cy, d
					mx = d*2+1
				if mx < d*2 and d > 1 and good2(cx, cy, d):
#					print "good2", cx, cy, d
					mx = d*2
					
	if mx == 0:
		print "IMPOSSIBLE"
	else:
		print mx
				
				