# -*- coding: utf-8 -*-
import sys

def solve(C,F,X):
	a = 2.0
	t0 = 0
	best = X/a # no farm
	while True:
		#print('{}: {} {}'.format(n,a,t0),file=sys.stderr)
		t0 += C/a
		a += F
		if best>X/a+t0:
			best = X/a+t0
			continue
		break
	return best

if __name__ == '__main__':
	T = int(input())
	for t in range(T):
		C,F,X = [float(i) for i in sys.stdin.readline().split()]
		#print([C,F,X],file=sys.stderr)
		
		ans = solve(C,F,X)
		print('Case #{}: {}'.format(t+1,ans))
		print('Case #{}: {}'.format(t+1,ans),file=sys.stderr)
