import sys
from sets import Set

sys.stdin = open('B-large.in','r')
sys.stdout = open('B-large.out','w')

def solve(case):
	C,F,X = map(float, sys.stdin.readline().strip().split())
	prev = 9999999999999999999999
	s = 0.0
	i = 0
	while True:
		r = s + X / (2 + i*F)
		s += C / (2 + i*F)
		if r>prev:
			return prev
		prev = r
		i += 1

T = int(raw_input())
for t in xrange(T):
	print "Case #" + str(t+1) + ": " + str(solve(t+1))