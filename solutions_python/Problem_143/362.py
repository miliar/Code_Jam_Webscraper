import sys
import math

sys.stdin = open('small.in')
debug = sys.stdout
sys.stdout = open('small.out', 'w')

def solve(a, b, k):
	return sum(ai & bi < k for ai in range(a) for bi in range(b))


n = int(raw_input())

for i in range(n):
	a, b, k = [int(x) for x in raw_input().split()]
	print "Case #{}: {}".format(i+1, solve(a, b, k))

