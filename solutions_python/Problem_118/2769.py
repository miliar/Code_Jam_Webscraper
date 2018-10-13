#!/usr/bin/python

import math

PALINDROME_CACHE = {}

def is_palindrome(number):
	if number in PALINDROME_CACHE:
		return PALINDROME_CACHE[number]

	str_number = str(number)
	
	size = len(str_number)
	
	if size == 1:
		PALINDROME_CACHE[number] = True
		return True
	p = True
	for x in xrange(size/2):
	#	print str_number, x, str_number[x], str_number[-x]
		if str_number[x] != str_number[-(x+1)]:
			p = False
			break

	PALINDROME_CACHE[number] = p

	return p

PALINDROME_SQUARE_CACHE = {}

def is_palindrom_square(number):
	if number in PALINDROME_SQUARE_CACHE:
		return PALINDROME_SQUARE_CACHE[number]
	
	p_s = False
	if is_palindrome(number):
		#print '%d is palindrome' % number
		sr = math.sqrt(number)
		#print sr
		if sr - int(sr) == 0 and is_palindrome(int(sr)):
			p_s = True
			#print 'and square'
	
			

	PALINDROME_SQUARE_CACHE[number] = p_s
	return p_s

def get_count(starting, ending):
	x = map(is_palindrom_square, (x for x in xrange(starting, ending+1)))
	return len(filter(lambda y: y, x))	

if __name__ == '__main__':
	import sys
	open_filename = sys.argv[1]
	results_filename = 'results.txt'
	file_text = ''
	with open(open_filename) as f:
		cases = int(f.readline())
		for case in xrange(cases):
			start, stop = f.readline().split(' ')
			file_text += 'Case #%d: %s\n' % (case+1, get_count(int(start), int(stop)))
	#print file_text
	with open(results_filename, 'w+') as f:
		f.write(file_text)
