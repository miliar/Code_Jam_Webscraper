#!/usr/bin/python

def snapper(n,k):
	b = map(lambda x: True if x=='1' else False, bin(k))
	return 'ON' if all(b[-n:]) else 'OFF'
	

if __name__ == '__main__':
	import sys
	file_name = sys.argv[1]
	f = open(file_name, 'r')
	C = int(f.readline())
	cases = C+0
	while cases > 0:
		cases -= 1
		n, k = f.readline().split()
		print 'Case #%d: %s' % (C-cases, snapper(int(n),int(k)))
