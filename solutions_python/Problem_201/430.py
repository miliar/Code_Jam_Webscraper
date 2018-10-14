from sortedcontainers import SortedList

def import_file(file):
	with open(file) as data:
		T = int(data.readline().rstrip('\n'))
		tests = []
		for datum in data:
			line = datum.rstrip('\n')
			toks = datum.split(' ')
			tests.append((long(toks[0]), long(toks[1])))
	return (T, tests)

def bathroom_stall(N, K):
	if K == 1:
		return (N/2, N - N/2 - 1)
	elif N % 2 == 0 and K % 2 == 0:
		return bathroom_stall(N/2, K/2)
	else:
		return bathroom_stall((N - 1)/2, K/2)

(T, test_cases) = import_file('test.in')
for idx in range(len(test_cases)):
	test = test_cases[idx]
	print('Case #' + str(idx + 1) + ':'),
	(maxStall, minStall) = bathroom_stall(test[0], test[1])
	print(maxStall),
	print(minStall)