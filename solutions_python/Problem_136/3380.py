with open("B-small-attempt0.in", "r") as f:
	T = int(f.readline())
	for i in range(0, T):
		line = f.readline().split()
		C = float(line[0])
		F = float(line[1])
		X = float(line[2])
		A = 0
		# We initialize with the number of seconds if we didn't buy any farms
		S = X / 2 + 1
		s = X / 2
		n = 0 # number of farms we bought
		while s < S:
			S = s
			s = 0
			n += 1
			#print("")
			#print("Let's say we build " + str(n) + " farms")
			for j in range(n):
				#print("We have " + str(j) + " farms")
				#print("So the " + str(j+1) + "th farm will take " + str(C / (2 + j * F)) + " cookies to build")
				s += C / (2 + j * F) # time to buy a farm
			s += X / (2 + n * F)
			#print("s=" + str(s))
			#print("S=" + str(S))

		print("Case #" + str(i+1) + ": " + str(S))