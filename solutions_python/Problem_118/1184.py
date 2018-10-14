#coding: utf-8
#!/usr/bin/env python2.7

import sys
import math
DEBUG = 0

def read_line():
	buf = []
	for l in sys.stdin: buf.append(l[:-1])
	return buf


def palin(num):
	str_num = str(num)
	l = len(str_num)

	flag = 1
	c = 0
	while 1:
		if str_num[c] != str_num[l-c-1]: flag = 0
		if str_num[c] == str_num[l-c-1] or flag == 0: break
	
	if flag and DEBUG: print num
	return flag

def solver(A, B):
	begin_sqrt = int(math.sqrt(A))
	if begin_sqrt**2 != A: begin_sqrt += 1

	end_sqrt = int(math.sqrt(B))+1

	counter = 0
	for i in range(begin_sqrt, end_sqrt):
		if palin(i) and palin(i**2): counter += 1
	
	return counter


def main():
	buf = read_line()

	num = int(buf[0])
	for i in range(1, num+1):
		X = int(buf[i].split(' ')[0])
		Y = int(buf[i].split(' ')[1])

		ans = solver(X, Y)
		print 'Case #%d: %d' % (i, ans)

if __name__ == '__main__':
	main()
