def main():
	num_cases = int_input()
	for i in range(1, num_cases + 1):
		do_case(i)


def list_input():
	line = raw_input()
	chunks = line.split(' ')
	return [int(x) for x in chunks]


def int_input():
	return int(raw_input())


def do_case(case_num):
	ans1 = int_input()
	table1 = [list_input() for i in range(4)]
	ans2 = int_input()
	table2 = [list_input() for i in range(4)]
	# print table1
	print("Case #%s: %s" % (case_num, solve(ans1, table1, ans2, table2)))


def solve(ans1, table1, ans2, table2):
	possible1 = table1[ans1 - 1]
	possible2 = table2[ans2 - 1]
	answers = []
	for x in possible1:
		if x in possible2:
			answers.append(x)
	if len(answers) == 1:
		return answers[0]
	elif len(answers) == 0:
		return 'Volunteer cheated!'
	else:
		return 'Bad magician!'


if __name__ == '__main__':
	main()
