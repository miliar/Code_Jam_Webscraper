#!/usr/bin/env python

import sys, os, re, operator, itertools

def ciclos(p):
	us = [False] * len(p)
	res = []
	for i in xrange(len(p)):
		if not us[i]:
			cnt = 0
			while not us[i]:
				us[i] = True
				i = p[i]
				cnt += 1
			res.append(cnt)
	return res


mem = dict()

def run(n):
	global mem
	if n in mem:
		return mem[n]
	if n == 1:
		return 0
	cnt = 0
	esp = 0
	tot = 0
	for p in itertools.permutations(range(n)):
		tot += 1
		cl = ciclos(p)
		#print p, "-->", cl
		if cl == [n]:
			cnt += 1
		else:
			for x in cl:
				esp += run(x)
	res = (tot+esp) / (tot-cnt)
	if (tot+esp) % (tot-cnt) != 0:
		print "La conjetura es banana."
	mem[n] = res
	print n, '=', res
	return res

def magic_run(n):
	if n == 1: return 0
	else: return n

def solve(f):
	f.readline()
	l = [int(x)-1 for x in f.readline().split()]
	return '%d.00000' % sum(map(magic_run, ciclos(l)))

def main():
	tt = int(sys.stdin.readline())
	for t in xrange(tt):
		res = solve(sys.stdin)
		print "Case #%d:" % (t+1), res


if __name__ == "__main__":
	main()

	#for n in range(1, 9):
	#	run(n)
	#print mem
