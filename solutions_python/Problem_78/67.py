input = open("FreeCell.in")
output = open("FreeCell.out", "w")
T = int(input.readline())
for t in range(T):
	sequence = [int(i) for i in input.readline().split(" ")]
	if (sequence[2] == 100 and sequence[1] != 100) or (sequence[2] == 0 and sequence[1] != 0):
		result = "Broken"
	else:
		result = "Broken"
		if sequence[0] >= 100:
			result = "Possible"
		else:
			for i in range(1, sequence[0] + 1):
				if int(sequence[1] / (100 / i)) == sequence[1] / (100 / i):
					result = "Possible"
					break
	print("Case #{case}: {result}".format(case = t + 1, result = result), file = output)
