import math

f = open('D-small-attempt0.in', 'r')

dist = lambda x1, y1, x2, y2: math.sqrt((x2-x1)**2 + (y2-y1)**2)

def testcase(ncase):
	n = int(f.readline())
	pl = []
	for i in range(n):
		(x, y, r) = map(int, f.readline().split())
		pl.append((x, y, r))
	if n == 1:
		R = pl[0][2]
	elif n == 2:
		R = max(pl[0][2], pl[1][2])
	elif n == 3:
		R = min([max((pl[0][2]+dist(pl[0][0],pl[0][1],pl[1][0],pl[1][1])+pl[1][2])/2.0, pl[2][2]),
			max((pl[0][2]+dist(pl[0][0],pl[0][1],pl[2][0],pl[2][1])+pl[2][2])/2.0, pl[1][2]),
			max((pl[2][2]+dist(pl[2][0],pl[2][1],pl[1][0],pl[1][1])+pl[1][2])/2.0, pl[0][2])])
	else:
		print 'Invalid test case'
		return
	print 'Case #%d: %.5f' % (ncase, R)


nc = int(f.readline())
for i in range(1, nc+1):
	testcase(i)