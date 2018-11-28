import sys
import itertools
sys.setrecursionlimit(10000)

with open('inputA') as fin:
	num_cases = int(fin.readline())

	cases = []
	for i in range(num_cases):
		num_strings = int(fin.readline())
		strings = [fin.readline().strip() for _ in range(num_strings)]
		cases.append((num_strings, strings))

# Give it a list of lens of elements
def min_distance(letter_lens):
	minimum = float("inf")
	for i in letter_lens:
	# for i in range(min(letter_lens), max(letter_lens) + 1):
		minimum = min(minimum, sum(abs(i - n) for n in letter_lens))

	return minimum

for index, case in enumerate(cases, 1):
	num_strings, strings = case
	letter_groups = [[k for k, _ in itertools.groupby(s)] for s in strings]
	lens = [[len(list(g)) for _, g in itertools.groupby(s)] for s in strings]

	test_group = letter_groups[0]
	if any(test_group != group for group in letter_groups):
		result = "Fegla Won"
	else:
		result = sum(min_distance(letter_lens) for letter_lens in zip(*lens))

	print "Case #{}: {}".format(index, result)
