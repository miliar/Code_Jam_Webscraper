from sys import stdin

def solve():
	stdin.readline()
	a = map(int, stdin.readline().split())

	r=0

	for i, x in enumerate(a):
		if i+1 != x:
			r+=1

	return r

n, = map(int, stdin.readline().split())
for i in range(n):
	print "Case #{}: {}".format(i+1, solve())
