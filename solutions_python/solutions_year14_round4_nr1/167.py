import random
import sys

def Solve():
	(n, m) = map(int, raw_input().split(' '))
	T = map(int, raw_input().split(' '))
	T.sort()
	T.reverse()
	pos = n-1
	result = 0
	for i in xrange(n):
		if i > pos:
			break
		if T[i]+T[pos] <= m:
			pos -= 1
		result += 1
	print result

if __name__ == '__main__':
  q = int(raw_input())
  for i in xrange(1, q+1):
    print "Case #%d:" % (i),
    Solve()
