#!/usr/bin/env python3
#coding=UTF-8

'''

Google Code Jam 2017
Round 1B
Problem B
Stable Neigh-bors

Instructions:
	chmod u+x process.py
	./process.py <input_file >output_file
	# stderr output is intended to display on a console

Notes:
	* we could just hardcode a table of allowed neighbors, if we can't think of anything better
	* for small dataset, we just have to avoid putting the same color next to itself
	* 
	* what if we just cycle until a color runs out?
		* not sure...
	* what if we emit the color with the largest remaining horses, excluding any that would conflict with the previous cell?
		* could work for the small dataset
	
	* I've failed to handle the end of the string correctly...
		* so I'm getting false IMPOSSIBLE reports
		* the second-last one has to be chosen more carefully
		* not completely sure if you can get away with only being careful at that stage, but we'll try it
		* last one must differ from first
		* therefore, second-last must be the same as the first if we still have that color at that stage
		* but what if 3rd last was that color?
		* I don't have time to consider this carefully....
		* add a rule: prefer the first color, if all else equal...
		* but we can still be forced into alternation between the first and another color
		* and our fate would be sealed from the moment we entered the final alternation between 2 colors
		* we have to choose the first color of the alternation based on whether there's an even or odd number of slots left to fill?
		* so... 


'''

################################################################################

def solve_case(id, case):
	N, R, O, Y, G, B, V = case
	
	# small dataset: O = G = V = 0
	# so only care about R Y B
	
	def solve(N, R, O, Y, G, B, V):
		colors = [[R, 'R'], [O, 'O'], [Y, 'Y'], [G, 'G'], [B, 'B'], [V, 'V']]
		
		debug('N:{} R:{} O:{} Y:{} G:{} B:{} V:{}\n'.format(N, R, O, Y, G, B, V))
		
		out = []
		prev = None
		for i in range(N):
			odd = (N - i) % 2
			def pref(col):
				if len(out) and col == out[0]:
					if odd:
						# prefer other color
						return -1
					else:
						# prefer first color
						return 1
				else:
					return 0
			colors = sorted([ col for col in colors if col[0] > 0 ], reverse=True, key=lambda col: (col[0], pref(col[1])))
			if prev:
				if prev == colors[0][1]:
					if len(colors) < 2:
						debug('impossible: {}\n'.format(''.join(out)))
						return 'IMPOSSIBLE'
					pick = 1
				else:
					pick = 0
			else:
				pick = 0
			
			if prev and prev == colors[0][1]:
				pick = 1
			else:
				pick = 0
			
			out.append(colors[pick][1])
			colors[pick][0] -= 1
			prev = colors[pick][1]
		
		if out[-1] == out[0]:
			debug('impossible: {}\n'.format(''.join(out)))
			return 'IMPOSSIBLE'
		
		#debug('{}\n'.format(''.join(out)))
		
		debug('R: {}\n'.format(sum( 1 for col in out if col == 'R' )))
		debug('Y: {}\n'.format(sum( 1 for col in out if col == 'Y' )))
		debug('B: {}\n'.format(sum( 1 for col in out if col == 'B' )))
		
		assert(R == sum( 1 for col in out if col == 'R' ))
		assert(Y == sum( 1 for col in out if col == 'Y' ))
		assert(B == sum( 1 for col in out if col == 'B' ))
		
		assert(V == sum( 1 for col in out if col == 'V' ))
		assert(O == sum( 1 for col in out if col == 'O' ))
		assert(G == sum( 1 for col in out if col == 'G' ))
		
		return ''.join(out)
	
	solution = solve(N, R, O, Y, G, B, V)
	
	return "Case #{}: {}\n".format(id, solution)

def read_case(id, input):
	N, R, O, Y, G, B, V = [int(n) for n in input.readline().split()]
	case = N, R, O, Y, G, B, V
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

