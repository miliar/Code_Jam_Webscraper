#!/usr/bin/python

from math import *

def is_fair(number):
	number = str(number)
	fair = 1
	if len(number) == 1:
		return 1
	else:
		mid = len(number)/2
		for i in range(0,mid):
			if number[i] != number[-1-i]:
				fair = 0
				break
	return fair

def is_square(number):
	square = 0
	s = int(sqrt(number))
	if s ** 2 == number:
		square = 1
	return (square, s)

def is_fair_square(number):
	result = 0
	if is_fair(number) == 1:
		(square, root) = is_square(number)
		if square == 1:
			if is_fair(root) == 1:
				result = 1
	return result

def deal_case(case_num, lower, upper):
	count = 0
	for num in range(lower,upper+1):
		if is_fair_square(num) == 1:
			print num
			count = count + 1

	return "Case #" + str(case_num) + ": " + str(count) + "\n"

def deal_file(fname1,fname2):
	f = open(fname1, 'r')
	f_r = open(fname2, 'w')
	line_num = 0
	case_num = 1
	for line in f:
		# print "line_num: %d" % line_num
		if line_num == 0:
 			pass
		else:
			(lower, upper) = map(int,line.split(' '))
			print "case_num: %d, lower: %d, upper: %d" % (case_num, lower, upper)
			result = deal_case(case_num, lower, upper)
			print result
			f_r.write(result)
			case_num += 1
		line_num += 1
	f.close()
	f_r.close()

def main():
	deal_file('C-small-attempt2.in.txt', 'C-small-attempt2.out.txt')
	#deal_file('C-sample.in.txt', 'C-sample.out.txt')

if __name__ == '__main__':
	main()