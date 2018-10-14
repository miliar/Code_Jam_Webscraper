#! /usr/bin/env python3

import sys

def paired(n, a, b):
	n_int = int(n)
	result = 0
	s = set([])
	for i in range(1, len(n)):
		m = n[i:] + n[:i]
		if n_int < int(m) <= b: 
			s.add((n, m))
	return len(s)


if __name__ == '__main__':
	
	if len(sys.argv) < 2:
		shift = 0
	else:
		shift = int(sys.argv[1])

	T = int(input())
	for i in range(T):
		a,b = input().split()
		a = int(a)
		b = int(b)
		
		result = 0
		for j in range(a,b):
			result += paired(str(j), a, b)
		print("Case #" + str(i+1+shift) + ": " + str(result))
