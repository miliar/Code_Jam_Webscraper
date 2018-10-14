#!/usr/bin/env python
import sys
import math
import random
	

def main():
	# Setup input and output file handlers
	if len(sys.argv) == 1:
		f_in = sys.stdin
		f_out = sys.stdout
	else:
		f_in = open(sys.argv[1])
		if len(sys.argv) > 2:
			f_out = open(sys.argv[2], 'w')
		else:
			f_out = sys.stdout

	T = int(f_in.readline())
	for t in range(T):
		f_out.write('Case #%d: ' % (t+1))

		out = 0
		A, B, K = list(map(int, f_in.readline().split(' ')))
		for a in range(A):
			for b in range(B):
				if a&b < K:
					out += 1
		f_out.write(str(out))
		f_out.write('\n')

	f_in.close()
	f_out.close()

if __name__=='__main__':
	main()
