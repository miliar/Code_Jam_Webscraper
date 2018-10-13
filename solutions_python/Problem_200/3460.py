import sys

def load(infile):
	with open(infile, 'r') as f:
		infile = f.read()
	infile = infile.splitlines()
	testcase_count = int(infile[0])
	return [x for x in infile[1:]]

def is_tidy(x):
	s = str(x)
	prev = '0'
	for c in s:
		if int(prev) > int(c):
			return False
		prev = c
	return True

def find_first_nontidy(x):
	s = str(x)
	test = ''
	for c in s:
		test += c
		if not is_tidy(test):
			return len(test) - 1
	raise Exception()

def run_test(case):
	if is_tidy(case):
		return case
	first_nontidy = find_first_nontidy(case) - 1
	digit_val = case[first_nontidy]
	first_nontidy = case.index(digit_val) # in case it's repeated
	base_nontidy = case[:first_nontidy + 1].ljust(len(case), '0')
	base_nontidy = str(int(base_nontidy) - 1)
	return base_nontidy
	return 0

def _main(infile):
	cases = load(infile)
	i = 1
	for case in cases:
		case = run_test(case)
		print('Case #{0}: {1}'.format(i, case))
		i += 1

if __name__ == "__main__":
	_main(sys.argv[1])
