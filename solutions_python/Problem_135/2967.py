with open("A-small-attempt0.in") as f:
	T = int(f.readline())
	for tt in range(0,T):
		ans1 = int(f.readline())
		grid1 = []
		for i in range(0,4):
			grid1.append([int(n) for n in f.readline().split(' ')])

		ans2 = int(f.readline())
		grid2 = []
		for i in range(0,4):
			grid2.append([int(n) for n in f.readline().split(' ')])

		guesses = []
		for g in grid1[ans1-1]:
			if g in grid2[ans2-1]:
				guesses.append(g)

		print("Case #{0}:".format(tt+1)),
		if len(guesses) == 1:
			print(guesses[0])
		elif len(guesses) == 0:
			print("Volunteer cheated!")
		else:
			print("Bad magician!")