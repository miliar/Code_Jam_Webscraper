### MAIN PROGRAM ###

input_filename  = "D-large.in"
output_filename = "D-large-ans.txt"


f = open(input_filename, "r")
g = open(output_filename, "w")

number_of_cases = int(f.readline())

case_cnt = 0
while case_cnt < number_of_cases:
	# get the blocks
	no_of_blocks = int(f.readline())
	N = [float(x) for x in f.readline().strip().split(' ')]
	K = [float(x) for x in f.readline().strip().split(' ')]
	N.sort()
	K.sort()
	
	# count Naomi's points when she plays War.
	# Naomi will play her blocks from smallest to largest. If Ken can beat the block
	# Naomi puts out, then he will put out the smallest possible block that wins. If he
	# can't possibly win, he will put out his smallest block.
	N_war_score = 0
	eligible_blocks = K[:]
	for n_block in N:
		eligible_blocks = [x for x in eligible_blocks if x > n_block]
		if len(eligible_blocks) == 0:
			N_war_score += 1
		else:
			k_block = eligible_blocks.pop(0)

	# count Naomi's points when she plays Deceitful War.
	# Basic strategy as follows: run through Naomi's blocks starting with the smallest.
	# Once we hit an N block ni which is larger than Ken's smallest block kj,
	# Naomi can lie and say 1.0 for weight. Ken will give up and chose kj. Naomi can then
	# choose ni and score a point.
	N_dwar_score = 0
	Ncopy = N[:]
	Kcopy = K[:]
	i, j = 0, 0		# indices for Naomi & Ken respectively
	while True:
		while i < len(Ncopy) and Ncopy[i] < Kcopy[j]:
			i += 1
		if i == len(Ncopy):
			break
		N_dwar_score += 1
		Ncopy.remove(Ncopy[i])
		Kcopy.remove(Kcopy[j])

	# output to screen & file
	output_string = "Case #" + str(case_cnt+1) + ": " + str(N_dwar_score) + \
					" " + str(N_war_score) + "\n"
	print output_string
	g.write(output_string)
	
	# move on to the next case
	case_cnt += 1

f.close()
g.close()

