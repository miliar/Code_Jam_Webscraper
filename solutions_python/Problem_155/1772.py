with open("A-large.in") as input:
	T = int(input.readline())
	i = 0
	for test in input:
		i += 1
		result = 0
		tmp = test.split(' ')
		Smax = int(tmp[0])
		S = tmp[1].strip()
		nb_clap = 0
		for j in xrange(len(S)):
			need = 0
			if nb_clap < j:
				need = j - nb_clap
				nb_clap += need
			result += need
			nb_clap += int(S[j])
		print("Case #"+str(i)+": "+str(result))