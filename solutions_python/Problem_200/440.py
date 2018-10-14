def import_file(file):
	with open(file) as data:
		T = int(data.readline().rstrip('\n'))
		tests = []
		for datum in data:
			toks = datum.rstrip('\n')
			tests.append(toks)
	return (T, tests)

def tidy(num):
	digits = [0] + [int(x) for x in list(num)]
	for idx in reversed(range(1, len(digits))):
		if digits[idx] < digits[idx - 1]:
			digits[idx - 1] -= 1
			for idx2 in range(idx, len(digits)):
				digits[idx2] = 9
	return ''.join([str(x) for x in digits]).lstrip('0')

(T, test_cases) = import_file('test.in')
for idx in range(len(test_cases)):
	test = test_cases[idx]
	print('Case #' + str(idx + 1) + ':'),
	print(tidy(test))
