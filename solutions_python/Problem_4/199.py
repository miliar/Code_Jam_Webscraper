# coding: cp932

import math

def main():
	fi = open('in_large.txt')
	#fo = open('out.txt', 'w')
	ncase = int(fi.readline())
	for i in range(ncase):
		n = int(fi.readline())
		vct1 = [int(t) for t in fi.readline().split()]
		vct2 = [int(t) for t in fi.readline().split()]
		val = calc(vct1, vct2)
		print 'Case #%d: %d' % (i+1,val)
	fi.close()
	#fo.close()

def calc(vct1, vct2):
	v1_p = [v for v in vct1 if v >= 0]
	v1_m = [v for v in vct1 if v < 0]
	v2_p = [v for v in vct2 if v >= 0]
	v2_m = [v for v in vct2 if v < 0]
	v1_p2 = iter(sorted(v1_p, key=abs, reverse=True))
	v1_m2 = iter(sorted(v1_m, key=abs, reverse=True))
	v2_p2 = iter(sorted(v2_p, key=abs, reverse=True))
	v2_m2 = iter(sorted(v2_m, key=abs, reverse=True))
	sum = 0
	for i in range(min(len(v1_m), len(v2_p))):
		sum += v1_m2.next() * v2_p2.next()
	for i in range(min(len(v1_p), len(v2_m))):
		sum += v1_p2.next() * v2_m2.next()
	v3, v4 = None, None
	if len(v1_m) > len(v2_p):
		v3 = v1_m2
	else:
		v3 = v2_p2
	if len(v1_p) > len(v2_m):
		v4 = v1_p2
	else:
		v4 = v2_m2
	v4 = iter(reversed(list(v4)))
	for a, b in zip(v3, v4):
		sum += a*b
	return sum

#import sys
#sys.setrecursionlimit(100000)
main()
