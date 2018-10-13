from random import uniform, random
from string import split, strip
import sys


def read_input(fname):
	cases = []
	infile = open(fname, 'rt')
	
	N = int(infile.readline())	
 	for c in range(N):
		S = int(infile.readline())
		searchEngines = []
		for s in range(S):
			searchEngines.append(infile.readline().strip())
		
		Q = int(infile.readline())
		queries = []
		for q in range(Q):
			queries.append(infile.readline().strip())
			
		cases.append((searchEngines, queries))			
 	return cases


def index_of(lst, val):
	"""
	Find first index of val in lst. If lst does not contain val,
	then return len(lst)
	"""
	if not lst:
		return 0
	else:
		try:
			i = lst.index(val)
			return i;
		except ValueError:	# val not found, so no more switches necessary
			return len(lst)


def main():
 	inps = read_input(sys.argv[1])
 	for i in range(len(inps)):
		(engines, queries) = inps[i]
		queries = tuple(queries) # lists are not hashable, but tuples are
		
		# Consider this a game where each state is described by:
		# (switches_up_to_now, current_engine, remaining_queries)
		# We solve the problem by finding a state with remaining_queries
		# empty, that has the minimum number of switches_up_to_now.
		# Two nodes with the same (current_engine, remaining_queries),
		# evolve in the same way, so we only need to expand the one with the
		# smallest switches_up_to_now, which allows us to prune the search graph
		
		min_switches = len(queries)

		# Dict of already visited states, stored as:
		# (switches, engine, remaining_queries) : switches
		visited_states = {}

		# Queue of states to process. When this is empty, we've searched all
		# states, and min_switches is a global minimum.
		state_q = []
		
		# Initialize the state_q with all possible starting states:
		for e in engines:
			state_q.append((0, e, queries))
			
		# Look at states, until done, updating min_switches...
		max_steps = None
		steps = 0
		while state_q:
			#@debug
			if max_steps and steps >= max_steps:
				break
			steps += 1
				
#			print len(state_q)
#			print state_q
			cur_state = state_q[0]
			state_q = state_q[1:]
			(cur_switches, cur_engine, remaining_queries) = cur_state
			
			# Have we visited this state before?
			if visited_states.has_key(cur_state):
				# If we visited it before, with lower switches_up_to_now,
				# then ignore current state: it's not as good.
				visited_state_switches = visited_states[cur_state]
#				print 'visited: ', cur_state, visited_state_switches
				if cur_switches >= visited_state_switches:
					continue
					
			# Er. better mark this visited or infinite loop. Not that I'd forget
			# to do that. No sir.
			
			visited_states[cur_state] = cur_switches
#			print visited_states
			
			# Haven't visited a better state yet, so
			# add all states we can get to from here to the queue for later
			# processing.

			for e in engines:
				safe_run_length = index_of(list(remaining_queries), e)
				
				# If this is a solution, then see if it's a global minimum now,
				# instead of putting it in the queue and only figuring that out
				# later (causes off by one in visits if you can solve with 0 visits)

				if safe_run_length >= len(remaining_queries):
					if cur_switches < min_switches:
						min_switches = cur_switches
					continue
				
#				print remaining_queries
				if e != remaining_queries[0]:	# Don't destroy the world!!!
					next_state = (1 + cur_switches, e, remaining_queries[safe_run_length:])
					state_q.append(next_state)
			
		print "Case #%d: %d" % (i+1, min_switches)
		
			
if __name__=='__main__':
  	main()
