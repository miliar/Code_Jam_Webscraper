def allStanding(Sarray):
	Standing = [0 for x in Sarray]
	
	for i,x in enumerate(Sarray):
		standing_count = sum([int(x) for x in Standing])
		if standing_count >= i:
			Standing[i] = Sarray[i]
	if(Standing == Sarray):
		return True

	return False

def sumFriends(Sarray):
	friends = 0
	while(True):
		if(allStanding(Sarray)):
			return friends
		else:
			friends += 1
			Sarray[0] += 1

def main():
	output = []
	with open('A-small-attempt1.in', 'r') as f:
		count = 0
		for line in f:
			if (count == 0):
				count += 1
			else:
				Smin, S = line.split()
				Sarray = [int(n) for n in S]
				output.append(sumFriends(Sarray))

	print output

	with open('A-small-attempt1.out', 'w') as fout:
		for i, x in enumerate(output):
			fout.write('Case #' + str(i + 1) + ': ' + str(x) + '\n')

if __name__ == "__main__":
	main()