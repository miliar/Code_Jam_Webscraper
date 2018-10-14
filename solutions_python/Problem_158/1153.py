import sys, math

sys.stdin = open('D-small-attempt1.in')
# sys.stdin = open('b.in')

def minside(size):
	if size <= 2:
		return 1
	elif size<= 4:
		return 2
	elif size<=6:
		return 3

def solve(x, r, c):


	if x >= 7:
		return "RICHARD"

	if minside(x) > min(r,c):
		return "RICHARD"

	if x > max(r,c):
		return "RICHARD"

	if r*c % x != 0:
		return "RICHARD"

	if r>c:
		r,c=c,r

	if x==4 and r==2 and c==4:
		return "RICHARD"

	return "GABRIEL"

T = int(sys.stdin.readline())

for i in xrange(T):
	x,r,c = map(int, sys.stdin.readline().split())
	print 'Case #' + str(i+1) + ': ' + str(solve(x, r, c))
		# print 'Case #' + str(i+1) + ': ' + " ".join([str(x),str(r),str(c)]) + ' ' + str(solve(x, r, c))