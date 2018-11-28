import math

def calcmax(x, n):

	team = 2 ** n
	left = team - 1 - x
	win = 0

	while(left > 0):
		win += 1
		left = (left - 1) / 2

	lose = n - win

	return (2 ** lose) - 1

def findmax(n, p):

	lb = 0
	ub = (2 ** n) - 1

	if(calcmax(ub, n) < p):
		return ub

	while (ub - lb > 1):

		mid = (lb + ub) / 2

		if(calcmax(mid, n) < p):
			lb = mid
		else:
			ub = mid

	return lb

def calcmin(x, n):

	team = 2 ** n
	left = x
	lose = 0

	while(left > 0):
		lose += 1
		left = (left - 1) / 2

	win = n - lose

	return (2 ** n) - (2 ** win)

def findmin(n, p):

	lb = 0
	ub = (2 ** n) - 1

	if(calcmin(ub, n) < p):
		return ub

	while (ub - lb > 1):

		mid = (lb + ub) / 2

		if(calcmin(mid, n) < p):
			lb = mid
		else:
			ub = mid

	return lb

t = int(raw_input())
cases = []
for i in range(t):
	n, p = map(int, raw_input().split())
	cases.append((n, p))

for i, c in enumerate(cases):

	n, p = c
	print "Case #%d: %d %d" % (i + 1, findmin(n, p), findmax(n, p))