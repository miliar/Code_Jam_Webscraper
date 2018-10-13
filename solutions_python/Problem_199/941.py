import sys

###########################################################

# Produce output in format suitable for submission
def generate_output(answers):

	# Iterate over all test cases
	for i in range(len(answers)):
		print "Case #" + str(i+1) + ":", answers[i]

###########################################################

def flip(pancakes):

	flipped_pancakes = ''

	for i in range(len(pancakes)):
		if pancakes[i] == '+':
			flipped_pancakes += '-'
		else:
			flipped_pancakes += '+'

	return flipped_pancakes

###########################################################

def flip_search(S, K, pancakes, max_depth, current_depth, last_i):

	# If maximum depth reached, terminate
	if current_depth == max_depth:
		return max_depth

	# If all happy side up, terminate
	if pancakes == ('+' * S):
		return current_depth

	# Apply single flip event, recurse search for new pancake string
	# NOTE: I expect to be useful up to S ~ 10, to collect data points for
	# use in developing a more analytical solution (i.e. construct best sequence)
	for i in range(S - K + 1):
		if i > last_i:
			applied_flip = pancakes[:i] + flip(pancakes[i:i+K]) + pancakes[i+K:]
			depth = flip_search(S, K, applied_flip, max_depth, current_depth+1, i)

			if depth < max_depth:
				max_depth = depth

	return max_depth

###########################################################

def find_flips(pancakes, K):
	S = len(pancakes)

	# An even sized spatula can only reverse even numbers of pancakes
	parity = 0
	for i in range(len(pancakes)):
		if pancakes[i] == '-':
			parity = 1 - parity

	if (parity % 2 == 1) and (K % 2 == 0):
		return 'IMPOSSIBLE'

	# All combinations are acheivable in S - K + 1 flips
	# Initialise depth to S - K + 2, so impossibility can be determined
	num_flips = flip_search(S, K, pancakes, S - K + 2, 0, -1)


	# Format output
	if num_flips > S - K + 1:
		return 'IMPOSSIBLE'
	else:
		return str(num_flips)

###########################################################


input_file = open(sys.argv[1], 'r')

header_line = input_file.readline()
T = int(header_line.rstrip())

input_data = input_file.readlines()
input_file.close()

answers = []
for entry in input_data:
	data = entry.rstrip().split(' ')
	pancakes = data[0]
	K = int(data[1])
	answers.append(find_flips(pancakes, K))

generate_output(answers)


