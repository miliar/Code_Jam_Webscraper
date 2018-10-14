#!/usr/bin/python

import sys

def read_input(filepath):
	f = open (filepath, 'r')
	
	cases = f.readline()
	for x in xrange(1, int(cases)+1):	
		solve_prob(x, [f.next() for i in xrange(5)], [f.next() for i in xrange(5)])

def solve_prob(case, board1, board2):
	list1 = [x.rstrip() for x in board1]
	list2 = [x.rstrip() for x in board2]
	row_number = board1[0]
	row = board1[int(row_number)].split()

	row_number2 = board2[0]
	row2 = board2[int(row_number2)].split()

	value = [val for val in row if val in row2]

	if (len(value) == 1):
		result = value[0]
	elif (len(value) == 0):
		result = "Volunteer cheated!"
	else:
		result = "Bad magician!"

	print "Case #%d: %s" % (case, result)
			

def main():
	if (len(sys.argv) < 2): 
		sys.exit("usage: blabla")

	read_input(sys.argv[1]) 


if __name__ == '__main__':
	main()