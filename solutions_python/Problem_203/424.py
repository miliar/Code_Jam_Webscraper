#!/usr/bin/env python3
#coding=UTF-8

'''

Google Code Jam 2017
Round 1A
Problem A
Alphabet Cake

Instructions:
	chmod u+x process.py
	./process.py <input_file >output_file
	# stderr output is intended to display on a console

Notes:
	* no need to split evenly? good
	* this problem feels tricky
	* small dataset <12 cells, large up to 625
	* will a greedy algorithm work?
	* based on the output description, it's always possible (but is that due to careful selection of inputs?)
	* can a rectangle choice for 1 letter interfere with a valid choice for another?
		* I think probably not...
			* thinking about it a little hasn't found any situations where this happens, as the letter blocking another rectangle can always take the role instead, in filling the empty space we were worried about
		* I'm going with a greedy algorithm
	* algorithm ideas:
		* list the possible rectangles for each child which don't cover any other child's letter?
		* ...
	* greedy algorithm:
		make a list of letters and their locations
		for each letter in the list:
			pick a letter (or cell if you like)
			make a biggest rectangle that covers that letter
				* extend in 4 directions in turn, checking new cells for other letters
			update grid accordingly
			

'''

################################################################################

def solve_case(id, case):
	R, C, grid = case
	
	letters = []
	for i in range(R):
		for j in range(C):
			val = grid[i, j]
			if val != '?':
				letters.append( (val, (i, j)) )
	
	if False:
		report('letters:\n')
		for letter in letters:
			report('\tletter: {}\n'.format(letter))
	
	for letter in letters:
		val, (i, j) = letter
		#report('{} {},{}\n'.format(val, i, j))
		
		# okay, we're just going to custom-code the 4 directions it'll extend in
		left = j
		while True:
			new_left = left-1
			# we could skip checks here, but simpler to put them all in and use the same set of checks everywhere
			if new_left >= 0 and new_left < C and grid[i, new_left] == '?':
				grid[i, new_left] = val
				left = new_left
			else:
				break
		
		right = j
		while True:
			new_right = right+1
			if new_right >= 0 and new_right < C and grid[i, new_right] == '?':
				grid[i, new_right] = val
				right = new_right
			else:
				break
		
		def row_is_clear(i, left, right):
			for k in range(left, right+1):
				if grid[i, k] != '?':
					return False
			return True
		
		def set_row(i, left, right, val):
			for k in range(left, right+1):
				grid[i, k] = val
		
		top = i
		while True:
			new_top = top-1
			if new_top >= 0 and new_top < R and row_is_clear(new_top, left, right):
				set_row(new_top, left, right, val)
				top = new_top
			else:
				break
		
		bottom = i
		while True:
			new_bottom = bottom+1
			if new_bottom >= 0 and new_bottom < R and row_is_clear(new_bottom, left, right):
				set_row(new_bottom, left, right, val)
				bottom = new_bottom
			else:
				break
	
	def valid():
		for i in range(R):
			for j in range(C):
				if grid[i, j] == '?':
					return False
		return True
	
	assert(valid())
	
	out = []
	out.append("Case #{}:\n".format(id))
	
	for i in range(R):
		out.append(''.join([ grid[i, j] for j in range(C) ]) + '\n')
	
	return ''.join(out)
	

def read_case(id, input):
	R, C = [ int(n) for n in input.readline().split() ]
	grid = dict()
	for i in range(R):
		row = list(input.readline().strip())
		assert(len(row) == C)
		for j in range(C):
			grid[i, j] = row[j]
	
	return R, C, grid

def prepare_data():
	return None

################################################################################


from sys import stdin, stdout, stderr
import time
import math
import pickle
import io

execution_timer = time.time
#execution_timer = time.clock
debugging = 1


################################################################################


def debug(message):
	if debugging:
		stderr.write(message() if hasattr(message, '__call__') else message)

def report(message):
	stderr.write(message)

def prepare_cached(prepare_data, pickle_path='data.pickle'):
	try:
		with io.open(pickle_path, 'rb') as file:
			data = pickle.load(file)
			report("Loaded {}.\n".format(pickle_path))
	except IOError:
		data = prepare_data()
		if data:
			report("Prepared {}.\n".format(pickle_path))
			with io.open(pickle_path, 'wb') as file:
				pickle.dump(data, file)
	return data

def prepare():
	global prepared_data
	prepared_data = prepare_cached(prepare_data, 'prepared_data.cached')

def main():
	t0 = execution_timer()
	prepare()
	t1 = execution_timer()
	report("Completed preparation in {:.6f} seconds.\n".format(t1 - t0))
	
	T = int(stdin.readline())
	for case_id in range(1,T+1):
		report("Processing test case {} of {} (output {}). {:.0f} seconds elapsed.".format(case_id, T, case_id-1, execution_timer() - t1))
		report("\n" if debugging else "\r")
		stderr.flush()
		stdout.write(solve_case(case_id, read_case(case_id, stdin)))
		stdout.flush()
	
	t2 = execution_timer()
	report("Processed {} test cases in {:.6f} seconds.                           \n".format(T, t2 - t1))
	report("Total time: {:.6f} seconds.\n".format(t2 - t0))

if __name__ == '__main__':
	main()

