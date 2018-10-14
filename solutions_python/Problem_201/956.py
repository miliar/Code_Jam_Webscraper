import sys

###########################################################

# Produce output in format suitable for submission
def generate_output(answers):

	# Iterate over all test cases
	for i in range(len(answers)):
		print "Case #" + str(i+1) + ":", answers[i][0], answers[i][1]

###########################################################

def get_last_max_min(N, K):

	# Terminating case, last occupant
	if K == 1:
		if N % 2 == 1:
			return [N/2, N/2]
		else:
			return [N/2, N/2 - 1]

	# If evenly split, halve remaining occupants
	if N % 2 == 1:

		stall = N/2 + 1
		Nnew = stall - 1

		if (K-1) % 2 == 1:
			Knew = (K-1)/2 + 1
		else:
			Knew = (K-1)/2

	# If uneven split, will occupy right, left, right ...
	else:
		stall = N/2

		# If odd number remaining, will occupy right
		if (K-1) % 2 == 1:
			Nnew = N/2
			Knew = (K-1)/2 + 1

		# If even number remaining, will occupy left
		else:
			Nnew = N/2 - 1
			Knew = (K-1)/2

	return get_last_max_min(Nnew, Knew)

###########################################################


input_file = open(sys.argv[1], 'r')

header_line = input_file.readline()
T = int(header_line.rstrip())

input_data = input_file.readlines()
input_file.close()

answers = []
for entry in input_data:
	data = entry.rstrip().split(' ')
	N = int(data[0])
	K = int(data[1])
	answers.append(get_last_max_min(N, K))

generate_output(answers)


