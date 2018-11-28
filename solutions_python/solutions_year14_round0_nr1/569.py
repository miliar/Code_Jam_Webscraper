f = file('A-small-attempt0.in', 'r')
fo = file('A-small-attempt0.out', 'w')

def get_input():
	return f.readline()

num_cases = int(get_input())

for case in range(num_cases):
	first_row = int(get_input())
	first_nums = []
	for i in range(4):
		if i == first_row - 1:
			first_nums = [int(item) for item in get_input().split(" ")]
		else:
			get_input()
	second_row = int(get_input())
	second_nums = []
	for i in range(4):
			if i == second_row - 1:
				second_nums = [int(item) for item in get_input().split(" ")]
			else:
				get_input()
	answers = []
	for num in first_nums:
		if num in second_nums:
			answers.append(num)
	fo.write("Case #{}: ".format(case+1))
	if len(answers) > 1:
		fo.write("Bad magician!")
	elif len(answers) == 0:
		fo.write("Volunteer cheated!")
	else:
		fo.write(str(answers[0]))
	fo.write("\n")