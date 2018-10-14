__author__ = 'Llostris'

# parses a group (answer, cards) to integer
def parse_to_int(answer, cards):
	for row in range(len(cards)):
		cards[row] = map(int, cards[row].split())
	return int(answer), cards


def form_output(testcase, possibilities):
	length = len(possibilities)
	with file('output.txt', 'w') as output:
		if length == 1:
			#output.write("Case #%d: %d\n" % (testcase, possibilities.pop()))
			print "Case #%d: %d" % (testcase, possibilities.pop())
		elif length == 0:
			print "Case #%d: Volunteer cheated!" % testcase
		else:
			print "Case #%d: Bad magician!" % testcase
		output.flush()


def pretend_magician(testcase, answer1, cards1, answer2, cards2):
	[answer1, cards1] = parse_to_int(answer1, cards1)
	[answer2, cards2] = parse_to_int(answer2, cards2)

	# print(answer1)
	# print(cards1)
	# print(answer2)
	# print(cards2)
	# print(set(cards1[answer1 - 1]))
	# print(set(cards2[answer2 - 1]))
	possibilities = set(cards1[answer1 - 1]) & set(cards2[answer2 - 1])
	# print(possibilities)
	form_output(testcase, possibilities)


if __name__ == '__main__':
	input_data = open('input.txt').readlines()
	test_cases_num = int(input_data.pop(0))
	# print(test_cases_num)

	for i in range(test_cases_num):
		# print("test " + str(i))
		pretend_magician(
			i + 1,
			input_data[0],
			input_data[1:5],
			input_data[5],
			input_data[6:10]
		)
		# print(input_data[0])
		# print(input_data[1:5])
		# print(input_data[5])
		# print(input_data[6:10])
		input_data = input_data[10:]


