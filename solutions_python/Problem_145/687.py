#!/usr/bin/env python3.2
#coding=UTF-8

'''

Google Code Jam 2014
Round 1C
Problem A
XXXXXXXX

Instructions:
	chmod u+x process.py
	./process.py <input_file >output_file
	# stderr output is intended to display on a console

Notes:
	* my first instinct is that you could simply keep halving the "value" of a 1/1 elf as you go up the chain of ancestors, until you find a value that is smaller than or equal to the indicated fraction
		* this indicates her fraction elf if there were 1 full 1/1 elf at this level and all other ancestors at this level were 0/1
		* but it may be impossible to get the exact value....
	* let's step up the heirarchy, calculating the value at Vida's generation of a 1/1 elf at the current generation
	* when the value is equal to her given fraction, we know it's possible by having exactly 1 1/1 elf here and all others 0/1 elves
	* if the value is smaller than the given fraction...
		* this is where I'm a little unsure of the logic
		* I'm not sure if it's always going to be okay to decide that there is a 1/1 elf at this level, just because the required proportion is greater than that
			* maybe it's only possible to reach the desired fraction by combining 2 or more different fractions at this level, which are both less than 1 and greater than 0
		* but let's assume for now it's okay
		* we would simply subtract the current generation's fraction from the target fraction, and keep going until we reach the target fraction or hit generation 40
		* I feel this should be obvious to me, whether ....
		* no... the overall fraction can always be expressed as 0..2**40 / 2**40, which represents some arbitrary proportion of full elves at generation 40
		* the position of these elves doesn't matter - how they combine doesn't matter
		* therefore they can always be shifted to one side without affecting the final fraction
		* which means you can always get a full elf at..... can't express it well but I'm convinced
		* this means my above algorithm should work...
		* except we need to consider the issue of large numbers, integer operations, and how to deal with that
	* now... thinking about issues about the size of the numbers
		* if it were possible to do this in floating point, the number sizes between small and large wouldn't really be an issue, right?
		* to keep it in the integer domain, we need to keep the numerator and denominator separate?
		* is this really necessary?
		* so that means we might have to adjust the denominators (by multiplication/division) to get compatible fractions for summing/subtracting?
	* large numbers / integer operations
		* I was talking about always halving the Vida value of a full elf at generation i
		* this would correspond to always doubling the denominator
		* then we needed to subtract the value from the target value....
		* but we can't do that without compatible (equal) denominators
		* I suppose we could simply try using GCD on the fractions to simplify them first
		* and if they don't simplify to a power of 2 under 2**40, it can't be done
		* algorithm:
			* simplify the input fraction
			* check if denominator is power of 2 less than or equal to 2**40
				* only 1 bit set
			* if not, it's "impossible"
			* if so, it's possible
			* keep doubling 1 up to 40 times to try to get the simplified input denominator
			* report the generation we reached
	* darn... I'm losing confidence in all my assumptions
		* I just noticed "P/Q is a fraction in lowest terms", which I guess means I don't have to simplify

'''

################################################################################


def simplify(x, y):
	g = abs(gcd(x, y))
	if g == 0: return (0, 0)
	return (x // g, y // g)

def gcd(a, b):
	while b: a, b = b, a % b
	return a

def read_case(id, input):
	P, Q = [int(x) for x in input.readline().split('/')]
	case = (P, Q)
	return case

def sol(P, Q):
	if Q > 2**40:
		# note it's already simplified
		return 'impossible'
	# I'm really not certain that we shouldn't be using floating point division here, but it won't hand't large numbers so we can't...
	# we could get a floating point scale which results in integral values for the multiplied P and Q, couldn't we?
	# I'm going to gamble that that's not possible for now...  nope, failed the sample cases
	# I'm bound to run into both floating point and number size issues, but I've wasted so much time so let's just try anything...
	scale = 2**40 / Q
	target_P = P * scale
	target_Q = Q * scale
	if not target_P.is_integer():
		return 'impossible'
	gen = 40
	val = target_P
	while val:
		val //= 2
		gen -= 1
	
	return gen + 1

def solve_case(id, case):
	P, Q = case
	solution = sol(P, Q)
	return "Case #{}: {}\n".format(id, solution)


def prepare():
	def prepare_data():
		return None
	
	global prepared_data
	prepared_data = prepare_cached(prepare_data, 'prepared_data.cached')


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
		data = pickle.load(io.open(pickle_path, 'rb'))
		report("Loaded {}.\n".format(pickle_path))
	except IOError:
		data = prepare_data()
		report("Prepared {}.\n".format(pickle_path))
		pickle.dump(data, io.open(pickle_path, 'wb'))
	return data

def main():
	t0 = execution_timer()
	#prepare()
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

