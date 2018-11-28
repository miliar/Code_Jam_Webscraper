import re

testcase = int(raw_input())

for i in range(1, testcase + 1, 1):
	inp = raw_input()
	init = map(int, re.findall(r'\d+', inp))

	R = init[0]
	K = init[1]
	N = init[2]

	inp = raw_input()
	group = map(int, re.findall(r'\d+', inp))

	euro = 0

	for looP in range(0, R, 1):
		riders = []
		sumof = 0;

		while len(group):
			ex = group[0]

			if sumof + ex > K:
				break

			sumof += ex
			group.pop(0)
			riders.append(ex)

		for ppls in riders:
			group.append(ppls)

		euro += sumof

	print "Case #%d: %d" % (i, euro)
