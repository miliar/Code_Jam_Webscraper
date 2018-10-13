#!/usr/bin/python3
import math

def process_fs(fo, a, b, order):
	m = math.ceil(math.sqrt(int(a)))
	n = math.floor(math.sqrt(int(b)))
	i = m
	count = 0
	while i <= n:
		if i % 10 == 0:
			i += 1
			continue
		a = ''
		k = i
		while k:
			a += str(k % 10)
			k //= 10
		if a != str(i):
			i += 1
			continue
		a = ''
		k = i * i
		while k:
			a += str(k % 10)
			k //= 10
		if a == str(i * i):
			i += 1
			count += 1
			continue
		i += 1
	fo.write('Case #{0:d}: {1:d}\n'.format(order, count))

import sys
if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("feed me the input file\n")
		sys.exit(-1)
	try:
		fi = open(sys.argv[1], 'r')
		fo = open(sys.argv[1][:-3] + '.out', 'w')
	except:
		print("can't open {:s}".format(sys.argv[1]))
		sys.exit(-2)

	lines = fi.readlines()
	lines.append('')
	fi.close()
	loop = int(lines[0])
	i = 1
	j = 1
	while i < len(lines) and j <= loop:
		mn = lines[i].split()
		m = mn[0]
		n = mn[1]
		process_fs(fo, m, n, j)
		i += 1
		j += 1
	fo.close()
