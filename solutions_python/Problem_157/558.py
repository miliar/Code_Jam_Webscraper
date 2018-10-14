#!/usr/bin/env python

import sys
import os

table = {"ii": ("", -1),
		 "ij": ("k", 1),
		 "ik": ("j", -1),
		 "ji": ("k", -1),
		 "jj": ("", -1),
		 "jk": ("i", 1),
		 "ki": ("j", 1),
		 "kj": ("i", -1),
		 "kk": ("", -1)}

def reduce_s(s, r):
	while (len(s) > 1):
		for k, v in table.iteritems():
			n = s.count(k)
			r *= v[1]**n
			s = s.replace(k, v[0])
	return s, r

def check_ijk(s):
	r = 1
	found_i = False
	found_j = False
	found_k = False
	while True:
		if len(s) < 3:
			return "", 0
		if not found_i:
			if s[0] == "i":
				found_i = True
			else:
				r *= table[s[:2]][1]
				s = table[s[:2]][0] + s[2:]
			continue
		if not found_j:
			if s[1] == "j":
				found_j = True
			else:
				r *= table[s[1:3]][1]
				s = s[0] + table[s[1:3]][0] + s[3:]
			continue
		if not found_k:
			if s[2] == "k":
				found_k = True
				return s[3:], r
			else:
				if len(s) < 4:
					return "", 0
				r *= table[s[2:4]][1]
				s = s[:2] + table[s[2:4]][0] + s[4:]
			continue
	return "", 0

def solve(s, X):
	x = s
	cnt = 1
	while len(x) < 10:
		if X <= cnt: break
		x += s
		cnt += 1
	x, r0 = check_ijk(x)
	if r0 == 0: return False
	r = 1
	s, r = reduce_s(s, r)
	r = r**(X - cnt)
	s = x + s * (X - cnt)
	r *= r0
	s, r = reduce_s(s, r)
	if s == "" and r == 1: return True
	return False

def main(args):
	f = file(args[1])
	N = int(f.readline().strip())
	for i in range(N):
		L, X = map(int, f.readline().strip().split())
		s = f.readline().strip()
		print "Case #%d: %s" % (i + 1, "YES" if solve(s, X) else "NO")

if __name__ == "__main__": main(sys.argv)
