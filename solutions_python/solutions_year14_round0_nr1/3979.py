with open('input.in') as input_file:
	lines = input_file.readlines()

lines = [line.rstrip() for line in lines]
lines.reverse()
n = int(lines.pop())
result = []

for i in range(n):
	first_pick = int(lines.pop())
	first_arrangment = []
	first_arrangment.append(lines.pop().split())
	first_arrangment.append(lines.pop().split())
	first_arrangment.append(lines.pop().split())
	first_arrangment.append(lines.pop().split())

	set1 = set(first_arrangment[first_pick - 1])

	second_pick = int(lines.pop())
	second_arrangment = []
	second_arrangment.append(lines.pop().split())
	second_arrangment.append(lines.pop().split())
	second_arrangment.append(lines.pop().split())
	second_arrangment.append(lines.pop().split())

	set2 = set(second_arrangment[second_pick - 1])

	if len(set1.intersection(set2)) > 1:
		result.append("Bad magician!")
	elif len(set1.intersection(set2)) == 1:
		result.append(set1.intersection(set2).pop())
	else:
		result.append("Volunteer cheated!")

with open('output.out', 'w') as out_file:
	for i, r in enumerate(result):
		out_file.write('Case #{}: {}\n'.format(i + 1, r))

