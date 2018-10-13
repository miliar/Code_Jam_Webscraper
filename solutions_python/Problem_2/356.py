#!/usr/bin/env python

## google code jam

# solver for train problem
# cat problem_data.txt | ./train.py

# author: seanj@xyke.com

import sys, string

def time_to_minutes( time_str):
	hours, minutes = time_str.split(":")
	return int( hours) * 60 + int( minutes)
	
def test_time_to_minutes():
	assert time_to_minutes( '00:00') == 0
	assert time_to_minutes( '01:01') == 61
	assert time_to_minutes( '12:00') == 720
	assert time_to_minutes( '00:30') == 30

test_time_to_minutes()

def get_cases( f, n):
	def sr():
		line = f.readline()
		return string.strip( line)
		
		
	case_l = []
		
	for case in range(n):	
		turn_around_time = int( sr())
		a, b = string.strip( sr()).split(' ')
		a = int( a)
		b = int( b)
		a_table = []
		for x in range( a):
			start, finish = sr().split( ' ')
			start = time_to_minutes( start)
			finish = time_to_minutes( finish) + turn_around_time
			a_table.append( (start, finish))
		b_table = []
		for x in range( b):
			start, finish = sr().split( ' ')
			start = time_to_minutes( start)
			finish = time_to_minutes( finish) + turn_around_time
			b_table.append( (start, finish))
			
		case_l.append( (a_table, b_table))
		
	return case_l

def dump_case( case):
	print "a => b"
	for entry in case[0]:
		print "\t", entry
	print "b => a"
	for entry in case[1]:
		print "\t", entry

def time_table_sort( a, b):
	if a[1] > b[1]:
		return 1
	if a[1] == b[1]:
		if a[0][1] == 'A' and b[0][1] == 'D':
			# swap if Departure before Arrival
			return -1
		else:
			return 0
	else:
		return -1
		
def test_table_sort():
	"""
	
	For the same time slot, we want all of the 
	arrivals, those entries ending in "A" to come
	before the the departures "D"
	
	"""
	
	schedule = [ ('AD',20), ('AA', 20), ('AA', 20), ('AD', 20), ('BD', 30) ]
	schedule.sort( time_table_sort)
	assert schedule == [('AA', 20), ('AA', 20), ('AD', 20), ('AD', 20), ('BD', 30)]
		
test_table_sort()
		
		
def calc_times( time_table, a = 0, b = 0):
	"returns the number of trains at a and b to guarantee the schedule"
	time_table.sort( time_table_sort)
	trains_at_a = a
	trains_at_b = b
	for entry in time_table:
		if entry[0] == 'AD':
			trains_at_a -= 1
		if entry[0] == 'BD':
			trains_at_b -= 1
		if entry[0] == 'AA':
			trains_at_a += 1
		if entry[0] == 'BA':
			trains_at_b += 1
	
		if trains_at_a < 0:
			# if trains goes negative, restart with another train at the station
			return calc_times( time_table, a + 1, b)
		if trains_at_b < 0:
			return calc_times( time_table, a, b + 1)

	# make sure no trains are lost
	assert a+b == trains_at_a + trains_at_b
	return a,b
	
def test_calc_schedules():
	s = [ ('AD', 0), ('BA', 100), ('BD', 102), ( 'AA', 200), ('AD', 102), ('BA', 200) ]
	assert (2,0) == calc_times( s, 0, 0)
	s = [
			('AD', 0), ('BA', 100),
			('AD', 0), ('BA', 100),
			('AD', 0), ('BA', 100),
			('AD', 0), ('BA', 100),
			('AD', 0), ('BA', 100),
			('BD', 101), ('AA', 200),
			('BD', 101), ('AA', 200),
			('BD', 101), ('AA', 200),
			('BD', 101), ('AA', 200),
			('BD', 101), ('AA', 200),
			('BD', 101), ('AA', 200)
	]
	assert (5,1) == calc_times( s, 0, 0)
	s = [
		('AD', 0), ('BA', 1),
		('BD', 2), ('AA', 3),
		('AD', 4), ('BA', 5),
		('BD', 6), ('AA', 7),
		('AD', 8), ('BA', 9),
		('BD', 10), ('AA', 11)
	]
	assert( 1,0) == calc_times( s, 0, 0)

	
if __name__ == '__main__':
	input_file = sys.stdin
	# input_file = open( sys.argv[1])
	num_cases = int( input_file.readline())
	

	# print 'number of test cases', num_cases
	cases = get_cases( input_file, num_cases)
	
	for i,case in enumerate(cases):
		time_table = []
		# dump_case( case)
		for a_entry in case[0]:
			time_table.append( ("AD", a_entry[0]))
			time_table.append( ("BA", a_entry[1]))
		for b_entry in case[1]:
			time_table.append( ("BD", b_entry[0]))
			time_table.append( ("AA", b_entry[1]))
		
		trains = calc_times( time_table, 0, 0)
		
		print "Case #%d: %d %d" % (i+1, trains[0], trains[1])
			
		
