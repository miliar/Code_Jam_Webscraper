
def read_strings (prompt = ''):
	return raw_input(prompt).split()

def read_ints (prompt = ''):
	value = map(int, read_strings(prompt))
	return value

def read_int (prompt = ''):
	try:
		value = read_ints(prompt)[0]
	except:
		value = None
	return value


def process_test_case (params):
	Smax = int(params[0])
	levels = map(int, list(params[1]))
	personCounter = 0
	friendsCounter = 0
	for j in xrange(0, Smax + 1):
		friends = j - personCounter
		if friends < 0:
			friends = 0
		personCounter += friends + levels[j]
		friendsCounter += friends
#		print j, ' ', friends

	value = friendsCounter
#	print 'Case #%d: %d - %dx%d %r' % (i + 1, min(tests), max_value, num_maxes, Pi)
	print 'Case #%d: %d' % (i + 1, value)


T = read_int() # number of test cases

for i in xrange(0, T):
#	print i
	line = read_strings()
	process_test_case(line)
#	if i == 5:
#		break
	pass
