#!/usr/bin/env python3
#coding=UTF-8

'''

Google Code Jam 2017
Round 1C
Problem B
Parenting Partnering

Instructions:
	chmod u+x process.py
	./process.py <input_file >output_file
	# stderr output is intended to display on a console

Notes:
	* in charge for 12 hours = 720 minutes, per day
	* absolute minimum overall is 2, for any problem
	* there needs to be 1 exchange between any pair of activities belonging to a different partner
	* the positions of those exchanges can range between the end of the earlier task and the beginning of the later
	* the circular pattern here adds some complexity
	* 
	* algorithm ideas for assigning segments:
		* we have a required exchange whenever a J activity is followed by a C activity, or vice-versa
		* we may require additional exchanges to meet the goal of 720 minutes per person
		* we could start by assuming a person's activity extends as far as it can until the next activity (ie. they won't take the baby for this time)
		* then if required, we can reduce that at all the boundaries between C and J activities
		* and if still required, we can reduce that at the boundaries between C and C, or J and J activities
		* or would it be better to begin with James taking maximum time (ahead and behind his activities), and then assign more time to cameron as required?
		* this would maybe be simpler as we're going from one extreme to the other...
		* right now I'm thinking in terms of activities... but perhaps I should be thinking in terms of baby sessions?
		* or... we could assign a C baby session for each J activity, and vice-versa, extending as required to cover all time
	
	* algorithm:
		* make special case for very low numbers of activities (work out details later)
		* build a list of JC boundaries (JC or CJ), and the size of each (be careful at wrap point)
			* to handle wrap point: start loop at index -1 (last item in python)
		* build a list of JJ boundaries and CC boundaries, and the size of each
		* assign as much time as possible to cameron - ie. all time in the JC boundaries is assigned to cameron
		* set the initial number of exchanges to the number of jc boundaries
		* go through the jc boundaries, passing time from cameron to james, as much as required to meet 720 minute goal
			* changing jc boundary allocations won't affect the number of exchanges
		* if jc boundaries run out, go through....
	* revised algorithm:
		* sum the size of all CJ boundaries (this means either CJ or JC - they're the same at this point)
		* base_j = sum(J activities, JJ boundaries)
		* base_c = sum(C activities, CC boundaries)
		* the base time represents the minimum time assigned to a partner such that we can achieve the minimum exchanges
		* free_time = sum(CJ boundaries)
			* we don't have to consider the individual chunks for this - the whole sum can be allocated as required
		* if we can meet our target 720 by allocating free time to c and j, we get the minimum exchanges
		* otherwise, we must continue...
		* assign all free time to the smallest of C or J, and then consider the CC or JJ boundaries, as appropriate to reduce that person's time down to 720
		* work from largest to smallest of these boundaries, until we hit the 720 goal
		* the problem is always possible, so we should always be able to hit it
		* for each boundary we subtract from the partner (and add to the other), we add 2 exchanges
			* is this really optimal? probably
	* time to start coding this, to help with thinking about the small details

'''

################################################################################

def asize(start, end):
	return (end - start) if end >= start else ((end + (24 * 60)) - start)

def solution(activities):
	target = 720
	
	# problem says james and cameron activities don't overlap
	# I think also they won't overlap with themselves
	
	# our loop should work so long as there's at least 1 activity
	# for 0 or 1 activities, the answer will be 2
	# (for 1, we could use the loop or the special case - we go with the special case)
	if len(activities) < 2:
		return 2  # otherwise this is the answer
	
	activities = sorted(activities, key=lambda a: a.start)
	
	report('{}\n'.format(activities))
	
	c_act = []
	j_act = []
	c_break = []
	j_break = []
	cj_break = []
	
	for i in range(len(activities)):
		prev = activities[i-1] # index -1 is last in python
		this = activities[i]
		
		if this.partner == 'J':
			j_act.append(asize(this.start, this.end))
			if prev.partner == 'J':
				j_break.append(asize(prev.end, this.start))
			else:
				cj_break.append(asize(prev.end, this.start))
		else: # 'C'
			c_act.append(asize(this.start, this.end))
			if prev.partner == 'C':
				c_break.append(asize(prev.end, this.start))
			else:
				cj_break.append(asize(prev.end, this.start))
	
	c_base = sum(c_act) + sum(c_break)
	j_base = sum(j_act) + sum(j_break)
	
	report('c: {} = {}\ncb: {} = {}\nj: {} = {}\njb: {} = {}\nfree: {} = {}\n'.format(c_act, sum(c_act), c_break, sum(c_break), j_act, sum(j_act), j_break, sum(j_break), cj_break, sum(cj_break)))
	
	exchanges = len(cj_break)
	total_free = sum(cj_break)
	
	assert((c_base + j_base + total_free) == (24 * 60))
	
	if j_base < c_base:
		c_base, j_base = j_base, c_base
		c_act, j_act = j_act, c_act
		c_break, j_break = j_break, c_break
	
	# c_base is now smaller
	
	if c_base + total_free >= target:
		return exchanges
	
	# allocate all free breaks to smallest (c)
	c_base = c_base + total_free
	
	for size in sorted(j_break, reverse=True):
		exchanges += 2
		c_base += size
		j_base -= size
		if c_base >= target:
			return exchanges
	
	# should not reach here
	assert(False)

def solve_case(id, case):
	activities = case
	return "Case #{}: {}\n".format(id, solution(activities))

class Activity:
	def __init__(self, start, end, partner):
		self.start = start
		self.end = end
		self.partner = partner
	
	def __repr__(self):
		return str((self.start, self.end, self.partner))

def read_case(id, input):
	Ac, Aj = [ int(n) for n in input.readline().split() ]
	activities = []
	for i in range(Ac):
		C, D = [ int(n) for n in input.readline().split() ]
		activities.append(Activity(C, D, 'C'))
	
	for i in range(Aj):
		J, K = [ int(n) for n in input.readline().split() ]
		activities.append(Activity(J, K, 'J'))
	
	case = activities
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

