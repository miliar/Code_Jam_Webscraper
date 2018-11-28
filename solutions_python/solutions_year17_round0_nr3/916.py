import math

def solve(stalls, people):
	if stalls == people:
		return 0, 0

	blocks = {stalls: 1}
	served = 0
	while served < people:
		largest = sorted(blocks.keys())[-1]
		number_cases = blocks.get(largest)
		del blocks[largest]

		if served + number_cases >= people:
			if largest % 2 == 0:
				return largest / 2, max(largest / 2 - 1, 0)
			else:
				return largest / 2, largest / 2
		else:
			if largest % 2 == 0:
				left = max(largest/2-1, 0)
			else:
				left = largest/2
			right = largest/2

			if not blocks.get(left):
				blocks[left] = number_cases
			else:
				blocks[left] += number_cases

			if not blocks.get(right):
				blocks[right] = number_cases
			else:
				blocks[right] += number_cases

			served += number_cases


with open('large.in') as f:
	num_cases = int(f.readline())
	for i in range(num_cases):
		line = f.readline()
		stalls = int(line.split(' ')[0].strip())
		people = int(line.split(' ')[1].strip())
		result = solve(stalls, people)
		print "Case #{}: {} {}".format(i + 1, result[0], result[1])