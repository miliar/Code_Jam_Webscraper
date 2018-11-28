#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
	tests=raw_input()

	for t in range(int(tests)):
		A, B = [int(x) for x in raw_input().split()]
		recycles = 0

		for n in range(A, B):
			N=str(n)
			for m in range(n+1, B+1):
				M=str(m)
				for index in range(len(M)):
					new_number=M[index:] + M[:index]
					if new_number == N:
						recycles += 1
						continue

		print "Case #%d: %d"%(t+1, recycles)
