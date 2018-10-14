from sys import stdin

def get_int_arr():
	return [int(x) for x in stdin.readline().split(' ')]

def solve():
	N = int(stdin.readline())
	A = []
	B = []

	for i in range(N):
		a, b = get_int_arr()
		A.append(a)
		B.append(b)
	
	intersect = 0
	for i in range(N):
		for j in range(i+1, N):
			y1 = A[i]
			y2 = B[i]
			z1 = A[j]
			z2 = B[j]

			if z2-z1-y2+y1 != 0:
				if (z2 < y2 and z1 > y1) or (y2 < z2 and y1 > z1):
					intersect += 1
	print intersect

T = int(stdin.readline())
for case in range(T):
	print 'Case #%d:' % (case+1),
	solve()
