import sys, math, copy

cases = int(sys.stdin.readline().rstrip())

for case in range(cases):

	# Number of blocks
	num_blocks = int(sys.stdin.readline().rstrip())

	# Each person's blocks
	naomi_blocks = map(float, sys.stdin.readline().rstrip().split())
	ken_blocks = map(float, sys.stdin.readline().rstrip().split())

	# Initialize each of their points
	naomi_deceit = 0
	naomi_honest = 0

	# Sort each list
	naomi_blocks.sort()
	ken_blocks.sort()

	# Run the calculations for deceit

	# Make a clone of each of the lists
	naomi_deceit_blocks = copy.deepcopy(naomi_blocks)
	ken_deceit_blocks = copy.deepcopy(ken_blocks)

	while len(naomi_deceit_blocks) > 0:

		naomi_deceit_block = naomi_deceit_blocks[0]

		if naomi_deceit_block < ken_deceit_blocks[0]:

			# Force removal of ken's last block
			ken_deceit_blocks.remove(ken_deceit_blocks[-1])

		else:

			# Remove ken's first block
			ken_deceit_blocks.remove(ken_deceit_blocks[0])

			naomi_deceit += 1

		# remove naomi's first block
		naomi_deceit_blocks.remove(naomi_deceit_block)

	# Calculations for honest
	while len(naomi_blocks) > 0:

		naomi_block = naomi_blocks.pop()

		ken_block = -1

		for block in ken_blocks:

			if block > naomi_block:

				ken_block = block

				break

		# If we did not find an appropriate block
		if ken_block == -1:

			# Throw away the lowest valued block
			ken_blocks.remove(ken_blocks[0])

			# Call a loss
			naomi_honest += 1

		# Otherwise, remove the block we just found
		else:

			ken_blocks.remove(ken_block)

	print 'Case #' + str(case+1) + ': ' + str(naomi_deceit) + ' ' + str(naomi_honest)
