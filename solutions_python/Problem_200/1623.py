def main():
	n_cases = int(raw_input())
	for i in xrange(n_cases):
		print "Case #%d: %s" % (i + 1, get_tidy(raw_input()))


def get_tidy(case):
	case = map(int, case)
	i = 0
	while i < len(case) - 1:
		if case[i] > case[i + 1]:
			case[i] -= 1
			case[i + 1:] = [9] * len(case[i + 1:])
			i = -1
		i += 1

	return str(int(''.join(map(str, case))))

def test_example_1():
	assert get_tidy("132") == "129"


def test_example_2():
	assert get_tidy("1000") == "999"


def test_example_3():
	assert get_tidy("7") == "7"


def test_example_4():
	assert get_tidy("111111111111111110") == "99999999999999999"


def test_example_5():
	assert get_tidy("972935720934") == "7"


if __name__ == '__main__':
	main()
