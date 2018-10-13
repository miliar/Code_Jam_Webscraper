import fileinput
import copy

testCases = None


def process(caseNumber, line):
	cp = copy.deepcopy(line)

	smax = cp[0]
	rem = cp[2:]
	rem = rem.rstrip()

	tally = [int(x) for x in rem]

	needed = 0

	# rev = reversed(tally):

	for i, startValue in enumerate(tally):

		if i != 0:
			currSum = 0
			for j in range(i):
				currSum += tally[j]

			currSum += needed

			if currSum < i:
				# print("CURR SUM < i")
				# print("i: ", i, "     currSum: ", currSum)
				needed += i - currSum

	msg = "Case #{}: {}"
	msg = str.format(msg, caseNumber, needed)
	print(msg)

caseNumber = 0

for line in fileinput.input():
	if fileinput.isfirstline():
		testCases = int(line)

	else:
		caseNumber += 1
		process(caseNumber, line)