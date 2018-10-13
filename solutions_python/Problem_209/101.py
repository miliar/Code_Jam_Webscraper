#!/usr/bin/env python3
#coding=UTF-8

'''

Google Code Jam 2017
Round 1C
Problem A
Ample Syrup

Instructions:
	chmod u+x process.py
	./process.py <input_file >output_file
	# stderr output is intended to display on a console

Notes:
	* we have:
		* plan area
		* + side area
	* plan area is just the area of the base pancake
	* side area is maximised by putting the widest and tallest at the bottom....
		* that's not very precise
	* so... we always pick biggest radius first to maximise plan area
	* then it becomes more complicated:
		* side area for a pancake = circumference * height
		* order of pancakes is already decided based on radius, and doesn't affect anything
		* but we have to choose which pancakes to include
		* simply calculate the side area of all pancakes, sort, and pick the top K pancakes
	* but.... it's possible that the biggest radius pancake is not actually in the optimal solution...
		* how to handle this?
		* consider the biggest radius...
		* ...
	* like this:
		* first take the top K pancakes for side area
		* work out the top area based on the largest radius in that
		* if the biggest radius is in there, then that's the solution... otherwise...
		* work from the top pancake by plan area downwards, and consider replacing the lowest side area with that
		* 

'''

################################################################################

import math

class Pancake:
	def __init__(self, R, H):
		self.radius = R
		self.height = H
		self.plan = math.pi * (self.radius ** 2)
		self.side = 2 * math.pi * self.radius * self.height
	
	def __repr__(self):
		return repr((self.radius, self.height, self.plan, self.side))

def stack_area(stack):
	side = sum([ pancake.side for pancake in stack ])
	plan = max([ pancake.plan for pancake in stack ])
	return side + plan

def solution(N, K, pancakes):
	
	by_plan = sorted(pancakes, key=lambda p: (p.plan, p.side), reverse=True)  # could just pick first...
	by_side = sorted(pancakes, key=lambda p: (p.side, p.plan), reverse=True)
	
	stacks = []
	
	# pick K biggest by side
	stack1 = by_side[:K]
	stacks.append(stack1)
	
	# either ensure biggest by plan is included
	# consider replacing biggest by plan with smallest by side
	# whichever result is biggest, wins
	
	if not (by_plan[0] in stack1):
		stack2 = stack1[:]
		stack2[K-1] = by_plan[0]
		stacks.append(stack2)
	
	if 0:
		for i, stack in enumerate(stacks):
			report('stack {}: {} = {}\n'.format(i, stack, stack_area(stack)))
	
	return max([ stack_area(stack) for stack in stacks ])

def solve_case(id, case):
	N, K, pancakes = case
	return "Case #{}: {}\n".format(id, solution(N, K, pancakes))

def read_case(id, input):
	N, K = [ int(n) for n in input.readline().split() ]
	pancakes = []
	for i in range(N):
		R, H = [ int(n) for n in input.readline().split() ]
		pancakes.append(Pancake(R, H))
	case = N, K, pancakes
	return case

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

