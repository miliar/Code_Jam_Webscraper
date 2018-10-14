file = open('input', 'r')

problems = int(file.readline())

for z in range(1, problems+1):
	moves = 0
	strings = int(file.readline())
	first = file.readline()
	win = True
	for i in range(1, strings):
		other = file.readline()
		k = 0
		j = 0
		while (k < len(other) and j < len(first)):		
			if (first[j] != other[k]):
				if (k - 1 >= 0 and first[j] == other[k - 1]):
					last_consumed = other[k - 1]
					j += 1
					moves += 1
				elif (j - 1 >= 0 and first[j - 1] == other[k]):
					last_consumed = first[j - 1]
					k += 1
					moves += 1
				else: 				
					win = False
					break;
			else:
				last_consumed = first[j]
				k += 1
				j += 1
	if win: 
		print "Case #" + str(z) + ": " + str(moves)
	else:
		print "Case #" + str(z) + ": Fegla won"	
