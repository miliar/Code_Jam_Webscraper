import sys
from collections import *

def solve(D, horses):
	duration = 0
	for K,S in horses:
		eta = (D-K)/S
		duration = max(duration, eta)
	return D/duration

T = int(input())
for case in range(T):
	D,N = map(int, input().split())
	horses = []
	for row in range(N):
		horses.append(list(map(int, input().split())))
	print("Case #{}: {}".format(case+1, solve(D,horses)))