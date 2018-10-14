# coding: utf8

import os, sys, re, string

def solve(R, C, data):
	oneline = []
	blues = 0
	for row in data:
		for ch in row:
			if ch == '.':
				oneline.append(0)
			else:
				oneline.append(1)
				blues += 1 
	if blues % 4 != 0:
		return "Impossible"
	if blues == 0:
		return "\n".join(data)
	cache = {}
	def convert():
		table = {0: '.', 1: '#',  2: '/', 3: '\\', 4: '\\', 5: '/'}
		res = []
		for i in xrange(R):
			r = []
			for j in xrange(C):
				p = i*C + j
				r.append(table[oneline[p]])
			res.append("".join(r))
		return "\n".join(res)
	def f(cnt):
		if cnt * 4 == blues:
			return convert()	
		key = tuple(oneline)
		if cache.has_key(key):
			return False
		cache[key] = 1
		for i in xrange(0, R - 1):
			for j in xrange(0, C - 1):
				p = i*C + j
				if oneline[p] == 1 and oneline[p+1] == 1 and oneline[p+C] == 1 and oneline[p+C+1] == 1:
					oneline[p] = 2
					oneline[p+1] = 3
					oneline[p+C] = 4
					oneline[p+C+1] = 5
					result = f(cnt+1)
					if type(result) == str:
						return result
					oneline[p] = 1
					oneline[p+1] = 1
					oneline[p+C] = 1
					oneline[p+C+1] = 1
		return "Impossible"	
	return f(0)

def main():
	T = int(sys.stdin.readline())
	for i in xrange(1, T + 1):
		R, C = map(int, sys.stdin.readline().split(" "))
		print "Case #%d: " % (i)
		print solve(R, C, map(lambda x: sys.stdin.readline().strip(), xrange(R)))

if __name__ == '__main__':
	main()


