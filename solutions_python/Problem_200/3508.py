def lastTidyNumber(N):
	i = N
	while (i > 0):
		number = str(i)
		tidy = True
		for j in range(1, len(number)):
			if number[j] < number[j-1]:
				offset = len(number)-j
				tidy = False
				break
		if tidy:
			return i
		power = 1
		for k in range(offset):
			power *= 10
		i = i - (i%power)-1

with open("B-large.out", 'w') as output:
	with open("B-large.in", 'r') as input:
		input.readline()
		case = 1
		for line in input:			
			output.write("Case #" + str(case) + ": " + str(lastTidyNumber(int(line))) + "\n")
			case += 1