#!/usr/bin/env python

import sys

def main():
	#f = file("test.in")
	f = file("B-large.in")
	#fout= file("test.out", "w")
	fout= file("B-large.out", "w")
	C = int(f.readline())
	cnt = 1
	for i in range(C):
		nswap = 0
		inc_swap = 0
		cnt_chicks = 0
		N, K, B, T = map(int, f.readline().strip().split())
		X = map(int, f.readline().strip().split())
		V = map(int, f.readline().strip().split())
		TM = [(B - X[j]) / float(V[j]) for j in range(N)]
		TM.reverse()
		for tm in TM:
			if tm <= T:
				cnt_chicks += 1
				nswap += inc_swap
			else: inc_swap += 1
			if cnt_chicks >= K: break
		print >>fout, "Case #%d: %s" % (cnt, str(nswap) if cnt_chicks >= K else "IMPOSSIBLE")
		cnt += 1

if __name__ == "__main__": main()
