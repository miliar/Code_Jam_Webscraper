input = open("GoroSort.in")
output = open("GoroSort.out", "w")
T = int(input.readline())
for t in range(T):
	N = int(input.readline())
	sequence = [int(i) for i in input.readline().split(" ")]
	s = 0
	for i in range(len(sequence)):
		if sequence[i] != i + 1:
			s += 1
	print("Case #{case}: {result}".format(case = t + 1, result = s), file = output)
	print(s)
