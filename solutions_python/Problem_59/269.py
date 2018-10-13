# coding: utf8

import os, sys, re, string

def create_dir(directory, path):
	if path == '/':
		return 0
	s = path.split("/")
	base = directory
	res = 0
	for name in s[1:]:	
		if base.has_key(name):
			base = base[name]
		else:
			base[name] = {}
			base = base[name]
			res += 1
	return res	
def main():
	T = int(sys.stdin.readline())
	for index in xrange(1, T + 1):
		N,M = map(int, sys.stdin.readline().split(" "))
		exists = [sys.stdin.readline().strip() for i in xrange(N)]
		create = [sys.stdin.readline().strip() for i in xrange(M)]
		filesystem = {}
		for s in exists:
			create_dir(filesystem, s)
		sum = 0
		for s in create:
			sum += create_dir(filesystem, s)
		print 'Case #%d: %d' % (index, sum)

if __name__ == '__main__':
	main()


