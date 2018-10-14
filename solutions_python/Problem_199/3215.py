from heapq import heappush, heappop

def pancakes(stack, flip_amount):
	# Returns the minimum number of flips to get a happy stack
	# of pancakes.

	starting_stack = stack
	frontier = []
	starting_cost = 0
	heappush(frontier, (starting_cost, starting_stack))
	explored = set()
	goal = '+'*len(stack)

	while frontier:
		# print('Exploring new frontier')
		(stack_cost, stack_state) = heappop(frontier)


		# If the stack is fully happy, no flips are required.
		if stack_state == goal:
			return stack_cost

		# add the stack state to the set of explored states
		explored.add(stack_state)

		# Identify neighbouring states
		# print('Current stack: ', stack_state)
		for i in range(len(stack_state) - flip_amount + 1):

			substack = stack_state[i:i+flip_amount]
			flipped_substack = flip(substack)
			neighbour_state = stack_state[:i] + flipped_substack + stack_state[i+flip_amount:]

			# print('Flipping index ', i)
			# print('Substack: ', substack)
			# print('Flipped Substack: ', flipped_substack)
			# print('Neighbour State: ', neighbour_state)

			# This whole thing sucks because I didn't set up the data structures for the nodes properly.
			if neighbour_state not in explored:

				# Check if the neighbour state exists in the frontier
				if neighbour_state not in [fs for (fc, fs) in frontier]:
					heappush(frontier, (stack_cost+1, neighbour_state))

				else:
					# Search the frontier states for the neighbouring state
					for (i, (c,v)) in enumerate(frontier):

						# If there is an entry with the same state and greater cost,
						# replace it with the neighbour and rebalance the heap.
						if neighbour_state == v and stack_cost+1 < c:
							frontier[i] = (stack_cost+1, neighbour_state)
							# print('Heapifying')
							heapify(frontier)
							break

def flip(stack):
	# Flips a stack of pancakes.
	# The sign of each individual pancake is reversed.
	# The order remains the same.

	flipped = []
	for s in stack:
		if s == '+':
			flipped.append('-')
		elif s == '-':
			flipped.append('+')

	return ''.join(flipped)


if __name__ == '__main__':

	num_test_cases = int(input())

	for i in range(num_test_cases):

		s, k = input().split()

		result_string = pancakes(s, int(k))
		if result_string is None:
			result_string = 'IMPOSSIBLE'

		print('Case #{}: {}'.format(i+1, result_string))

