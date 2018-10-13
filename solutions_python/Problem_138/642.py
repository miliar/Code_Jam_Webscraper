f = open("D-large.in", "r")

output = open("pd_test.out", "w")

T = int(f.readline().rstrip("\n"))

for round in range(1, T+1):
	N = int(f.readline().rstrip("\n"))
	Naomi_blocks = f.readline().rstrip("\n").split(" ")
	Naomi_blocks = [float(x) for x in Naomi_blocks]

	Ken_blocks = f.readline().rstrip("\n").split(" ")
	Ken_blocks = [float(x) for x in Ken_blocks]

	# optimal games
	Naomi_blocks = sorted(Naomi_blocks)
	Ken_blocks = sorted(Ken_blocks, reverse = False)
		
	### war
	Naomi_low = 0
	Ken_low = 0

	Ken_wins = 0
	for i in xrange(N):
		if Ken_blocks[Ken_low] > Naomi_blocks[Naomi_low]:
			# Ken wins this one
			Ken_wins += 1
			Ken_low += 1
			Naomi_low += 1
		else:
			Ken_low += 1
	war_num = N - Ken_wins

	### deceitful war
	Naomi_low = 0
	Naomi_high = len(Naomi_blocks) - 1

	Ken_low = 0
	Ken_high = len(Ken_blocks) - 1

	Naomi_wins = 0
	Ken_wins = 0
	for i in xrange(N):
		if Naomi_blocks[Naomi_high] > Ken_blocks[Ken_high]:
			# Naomi can get this one for sure
			Naomi_wins += 1
			Naomi_high -= 1
			Ken_high -= 1
		else:
			# Naomi uses lowest available weight to trick
			# Naomi loses this one but with minimum cost
			Ken_wins += 1
			Naomi_low += 1
			Ken_high -= 1
	deceitful_war_num = Naomi_wins

	print "Case #%d: %d %d" %(round, deceitful_war_num, war_num)