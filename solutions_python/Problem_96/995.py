# coding: utf8

import os, sys, re, string

def get_tripets(num):
	if num == 0: 
		return [0, 0]
	if num == 1:
		return [1, 1]
	base_value, mo = num / 3, num % 3
	base = [base_value + ((mo + 3) >> 2), base_value + ((mo + 2) >> 2), base_value]
	def other():
		v = base[0]
		if v == base[2]:
			return [v + 1, v, v - 1]
		if v == base[1]:
			return [v + 1, v - 1, v - 1]
		return [v, v, v - 2]
	return [max(base), min(10, max(other()))]
	

def main():
	tripets_maps = map(get_tripets, xrange(31))
	T = int(sys.stdin.readline())
	for index in xrange(1, T+1):
		s = sys.stdin.readline().strip()
		ss = map(int, s.split(" "))
		N,S,p,scores = ss[0], ss[1], ss[2], ss[3:]
		normal, surp = 0, 0
		for score in scores:
			value = tripets_maps[score]
			if value[0] >= p:
				normal += 1
			elif value[1] >= p:
				surp += 1
		print "Case #%d: %d" % (index, normal + min(S, surp))

if __name__ == '__main__':
	main()


