#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def extend(mapping, a, b):
	assert len(a)==len(b)
	for i, j in zip(a, b):
		if i not in mapping:
			mapping[i] = j
		else:
			assert mapping[i]==j


if __name__=='__main__':
	mapping = {'y': 'a', 'e': 'o', 'q': 'z'}
	extend(mapping, 'ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand')
	extend(mapping, 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities')
	extend(mapping, 'de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up')
	for i in range(ord('a'), ord('z')+1):
		if chr(i) not in mapping:
			vals = set(mapping.values())
			for j in range(ord('a'), ord('z')+1):
				if chr(j) not in vals:
					mapping[chr(i)] = chr(j)

	def convert(c):
		if c in mapping:
			return mapping[c]
		else:
			return c

	n = None
	for i, line in enumerate(sys.stdin, 0):
		if i==0:
			n = int(line)
		elif i>n:
			break
		else:
			print("Case #{x}: {s}".format(x=i, s="".join(map(convert, line))), end='')

