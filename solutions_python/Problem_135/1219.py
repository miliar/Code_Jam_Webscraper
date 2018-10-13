def guess_card(guess1, arrangement1, guess2, arrangement2):

	# Track card re-arangements
	fixed_range = range(4)
	card_paths = [
		[
			[line + 1 for line in fixed_range if str(i) in arrangement1[line].split()][0],
			[line + 1 for line in fixed_range if str(i) in arrangement2[line].split()][0]
		] for i in range(1, 17)
	]

	guess1 = int(guess1)
	guess2 = int(guess2)

	answers = []
	for i in range(16):
		if card_paths[i][0] == guess1 and card_paths[i][1] == guess2:
			answers.append(i+1)

	return answers

# Get data
file = open('in','r')
data = file.read().splitlines()
file.close()

# Start solving
results = []
test_cases = int(data[0])
data.pop(0)
for i in range(test_cases):
	case_index = 10 * i
	results.append(guess_card(
		data[case_index],
		data[case_index + 1: case_index + 5],
		data[case_index + 5],
		data[case_index + 6: case_index + 10]))

# print results
file = open('out', 'w')
for i in range(test_cases):
	file.write('Case #' + str(i + 1) + ': ')
	length = len(results[i])
	if length == 1:
		file.write(str(results[i][0])+'\n')
	elif length == 0:
		file.write('Volunteer cheated!\n')
	else:
		file.write('Bad magician!\n')

file.close()





