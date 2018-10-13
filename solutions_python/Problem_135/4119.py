import fileinput

f = open('A-small-attempt0.in')

i = []

for line in f:
	i.append(line)

test_cases = int(i.pop(0))
test_cases2 = test_cases
cases = []

while test_cases > 0:
	a = int(i.pop(0))
	
	grid1 = [
			[int(d) for d in i.pop(0).strip().split(" ")],
			[int(d) for d in i.pop(0).strip().split(" ")],
			[int(d) for d in i.pop(0).strip().split(" ")],
			[int(d) for d in i.pop(0).strip().split(" ")]
			]

	b = int(i.pop(0))

	grid2 = [
			[int(d) for d in i.pop(0).strip().split(" ")],
			[int(d) for d in i.pop(0).strip().split(" ")],
			[int(d) for d in i.pop(0).strip().split(" ")],
			[int(d) for d in i.pop(0).strip().split(" ")]
			]

	cases.append([a, b, grid1, grid2])
	test_cases -= 1

answer = 0

def findcard(row1, row2, grid1, grid2):
	possibilities1 = []
	possibilities2 = []
	card = []
	
	for num in grid1[row1 - 1]:
		possibilities1.append(num)
	
	for num in grid2[row2 - 1]:
		possibilities2.append(num)

	for num in possibilities1:
		for num2 in possibilities2:
			if num == num2:
				card.append(num)

	if len(card) > 1:
		return "bad"

	if len(card) == 0:
		return "vol"

	if len(card) == 1:
		return card[0]

case_number = 1
while case_number <= test_cases2:
	v = cases[case_number - 1][0]
	b = cases[case_number - 1][1]
	n = cases[case_number - 1][2]
	m = cases[case_number - 1][3]
	if findcard(v, b, n, m) == "bad":
		print("Case #%d: Bad magician!" % (case_number))
	elif findcard(v, b, n, m) == "vol":
		print("Case #%d: Volunteer cheated!" % (case_number))
	else:
		print("Case #%d: %d" % (case_number, findcard(v, b, n, m)))
	case_number += 1