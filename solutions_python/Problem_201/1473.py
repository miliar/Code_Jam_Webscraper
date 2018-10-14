import sys
import re
from math import floor, ceil
from heapq import *

def problemA(n, k, case):
	count = 0
	for i in range(len(n)):
		if n[i] == "-" and i+k <= len(n):
			count += 1
			for j in range(k):
				if n[i+j] == "+":
					n[i+j] = "-"
				else:
					n[i+j] = "+"
			i = k + i
	if "-" in n:
		return f'Case #{case}: IMPOSSIBLE\n'
	else:
		return f'Case #{case}: {count}\n'


def problemB(n, case):
	print(f'Case #{case}: {n}')
	val = int(n)
	diff = 0
	if len(n) > 1:
		for i in range(1, len(n)):
			if n[i-1] > n[i]:
				diff += int(n[i:]) + 1
				break
			elif n[i-1] == n[i] and i < len(n) - 1:
				diff += int(n[i]) * (10 ** (len(n)- i - 1))
			else:
				diff = 0

		val = val - diff
		return f'Case #{case}: {val}\n'
	else:
		return f'Case #{case}: {val}\n'


def problemC1(n, k, case):
	for i in range(k):
		if n % 2 == 1:
			#middle choice
			s = ceil(n/2)
		else: 
			#leftmost choice
			s = floor(n/2)
		ls= abs(s - 1)
		rs = n - s
		z = min(ls, rs)
		y = max(ls, rs)
		n = y
	return f'Case #{case}:  {y} {z}\n'

def problemC(n, k, case):
	ls = []
	rs = []
	for i in range(k):
		if n % 2 == 1:
			#middle choice
			s = ceil(n/2)
		else: 
			#leftmost choice
			s = floor(n/2)
		z = min(abs(s-1), (n-s))
		y = max(abs(s-1), (n-s))
		heappush(ls, 1 - s)
		heappush(rs, s - n)
		if abs(ls[0]) >= abs(rs[0]):
			n = abs(heappop(ls))
		else:
			n = abs(heappop(rs))
	return f'Case #{case}:  {y} {z}\n'


if __name__ == '__main__':
	output = open(sys.argv[2], 'w')
	with open(sys.argv[1]) as f:
		i = 0
		for w in re.split('\n', f.read()):
			x = re.split('\s', w)
			if i != 0:
				print(f'Case #{i}: {x[0]} {x[1]}')
				output.write(problemC(int(x[0]), int(x[1]), i))
			i += 1
	output.close()