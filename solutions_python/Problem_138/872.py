n = int(raw_input())
for i in range(0,n):
	plays = int(raw_input())

	n_blocks = raw_input()
	n_blocks = n_blocks.split()
	n_blocks = [float(x) for x in n_blocks]
	n_blocks = sorted(n_blocks)
	n_blocks_dec = n_blocks[:]

	k_blocks = raw_input()
	k_blocks = k_blocks.split()
	k_blocks = [float(x) for x in k_blocks]
	k_blocks = sorted(k_blocks)
	k_blocks_dec = k_blocks[:]

	n_points_leg = 0
	n_points_dec = 0


	for j in range(0,plays):
		k_play = -1.0
		n_play = n_blocks[len(n_blocks) - 1]
		
		for x in k_blocks:
			if x > n_play:
				k_play = x
				break
		
		if k_play < 0.0:
			k_play = k_blocks[0]
			n_points_leg += 1

		n_blocks.remove(n_play)
		k_blocks.remove(k_play)

		n_play = -1.0
		k_play = -1.0

		if(n_blocks_dec[len(n_blocks_dec) - 1] > k_blocks_dec[len(k_blocks_dec) - 1]):
			n_play = n_blocks_dec[len(n_blocks_dec) - 1]
			k_play = k_blocks_dec[len(k_blocks_dec) - 1]
			n_points_dec += 1
		else:
			n_play = n_blocks_dec[0]
			k_play = k_blocks_dec[len(k_blocks_dec) - 1]

		n_blocks_dec.remove(n_play)
		k_blocks_dec.remove(k_play)

	print 'Case #' + str(i + 1) + ': ' + str(n_points_dec) + ' ' + str(n_points_leg)