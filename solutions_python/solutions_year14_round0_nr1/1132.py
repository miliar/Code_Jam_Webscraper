
from pprint import pprint


def result(case):
	answer_2 = case["answer-2"]
	first_row = case["1st_cards"]
	cards = case["2nd_cards"]

	isection = set(first_row) & set(cards[answer_2])

	# The first and second selected row do not have shared numbers.
	if len(isection) <= 0:
		return "Volunteer cheated!"

	if len(isection) > 1:
		return "Bad magician!"

	# Return shared number of 1st and 2nd rows.
	return isection.pop()


in_file = open("A-small-attempt1.in")
out_file = open("A-small-attempt1.out", "wt")
cases = {}

# Skip first line
n_cases = int(in_file.readline())

i = 0
case = 1
answer_1 = None

for line in in_file:
	line = line.rstrip()

	if i == 0:
		answer_1 = int(line)

		cases[case] = {
			"1st_cards": None,
			"2nd_cards": {}
		}
	elif i == 5:
		cases[case]["answer-2"] = int(line)
	elif i < 5:
		if i == answer_1:
			cases[case]["1st_cards"] = [int(i) for i in line.split()]
	elif i > 5:
		cases[case]["2nd_cards"][i - 5] = []

		for card in line.split():
			cases[case]["2nd_cards"][i - 5].append(int(card))

	i += 1

	if i > 9:
		i = 0
		case += 1

for i in range(1, n_cases + 1):
	print("Case #%s: %s" % (i, result(cases[i])))
	out_file.write("Case #%s: %s\n" % (i, result(cases[i])))

in_file.close()
out_file.close()