import time, sys
f = open("input.txt", "r")
u = open("output.txt", "w")

def rotate(a, b):
	x = a
	a = str(a)
	cnt = 0
	while 1:
		a = a[1:] + a[0]
		if int(a) > x and int(a) <= b:
			cnt += 1
		if str(x) == a:
			break
	return cnt

def solve(a, b):
	s = 0
	for i in range(a, b+1):
		s += rotate(i, b)
	return s

n = int(f.readline())
for I in range(n):
	print>>u, "Case #" + str(I+1) + ": " + str(solve(*[int(i) for i in f.readline().split()]))
	print>>sys.stderr, I, time.clock()
