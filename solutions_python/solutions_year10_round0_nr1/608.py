# coding: utf8

import os, sys, re, string

def main():
	cnt = int(sys.stdin.readline())
	for i in xrange(1, cnt+1):
		n,k = map(int, sys.stdin.readline().strip().split(" "))
		flag = (1 << n) - 1
		check = 'ON' if (k & flag) == flag else 'OFF'
		print 'Case #%d: %s' % (i, check)

if __name__ == '__main__':
	main()


