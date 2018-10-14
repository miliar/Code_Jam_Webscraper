import sys

input = open(sys.argv[1], 'r')

t = int(input.readline())

for i in range(t):
	answer1 = int(input.readline())
	cards1 = [	input.readline().split(),
				input.readline().split(),
				input.readline().split(),
				input.readline().split()]
	answer2 = int(input.readline())
	cards2 = [	input.readline().split(),
				input.readline().split(),
				input.readline().split(),
				input.readline().split()]
	
	matches = []
	for card in cards1[answer1 - 1]:
		if (card in cards2[answer2 - 1]):
			matches.append(card)
	
	sys.stdout.write('Case #' + str(i + 1) + ': ')

	if (len(matches) == 0):
		print('Volunteer cheated!')
	elif (len(matches) > 1):
		print('Bad magician!')
	else:
		print(matches[0])

input.close()
