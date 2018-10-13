# coding: utf8

import os, sys, re, string

def main():
	cnt = int(sys.stdin.readline())
	for i in xrange(1, cnt + 1):
		R,k,n = map(int, sys.stdin.readline().split(" "))
		g = map(int, sys.stdin.readline().split(" "))
		if len(g) == 1:
			print 'Case #%d: %d' % (i, R*min(k, g[0]))
		else:
			table = []
			leng = len(g)
			for j in xrange(leng):
				sum = 0
				for kk in xrange(leng):
					v = g[(j + kk) % leng]
					if sum + v > k:
						break
					sum += v
				table.append((sum, (j + kk) % leng))
			euro = 0
			index = 0
			for j in xrange(R):
				euro += table[index][0]
				index = table[index][1]
			print 'Case #%d: %d' % (i, euro)


if __name__ == '__main__':
	main()


