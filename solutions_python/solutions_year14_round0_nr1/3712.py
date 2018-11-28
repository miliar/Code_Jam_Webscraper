from sys import argv

f = open(argv[1], 'r')

games = f.read()
games = games.split('\n')

number_of_tests = int(games[0])

i = 1
j = 1

while i < (10 * number_of_tests):
	row1 = int(games[i])
	nums_in_row1 = [int(num) for num in games[i + row1].split()]
	row2 = int(games[i+5])
	nums_in_row2 = [int(num) for num in games[i + 5 + row2].split()]

	possible_nums = []

	for num in nums_in_row1:
		if num in nums_in_row2:
			possible_nums.append(num)

	number_of_cards = len(possible_nums)

	if number_of_cards == 0:
		print "Case #" + str(j) + ": Volunteer cheated!"
	elif number_of_cards == 1:
		print "Case #" + str(j) + ": " + str(possible_nums[0])
	else:
		print "Case #" + str(j) + ": Bad magician!"

	j += 1
	i += 10
