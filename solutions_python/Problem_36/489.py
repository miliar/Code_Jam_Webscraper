#!/usr/bin/env python
import sys

str = 'welcome to code jam'

def make_simple(line):
	firstW = line.find('w')
	lastM = line.rfind('m')
	return line[firstW:lastM+1].translate(None, 'bfghiknpqrsuvxyz')

def count(text):
	l1 = [0]*len(text)

	for i, v in enumerate(text):
		if v == 'w':
			l1[i] = 1

	for letter in str[1:]:
		sum = 0
		for i, v in enumerate(text):
			if l1[i] != 0:
				sum += l1[i]
				l1[i] = 0
			elif v == letter:
				l1[i] = sum
	
	total = 0
	for n in l1:
		total += n
	
	return total

def main():
	filename = sys.argv[1]
	f = open(filename, 'r')
	N = int(f.readline())
	x = 1 
	for l in f:
		line = make_simple(l)
		c = count(line) % 10000
		print 'Case #' + repr(x) + ': ' + repr(int(c)).zfill(4) 
 		x += 1

main()
