
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

def rec_cut (Pi):
	newPi = []
	Pi = Pi
	max_value = max(Pi)
	if max_value == 1:
		return None
	foundMax = False
#	print 'max = %d %r' % (max_value, Pi)
	for i in xrange(0, len(Pi)):
		if foundMax == False and Pi[i] == max_value:
#			print 'found %d' % (max_value)
			half1 = Pi[i] / 2
			half2 = Pi[i] - half1
			newPi.append(half1)
			newPi.append(half2)
			foundMax = True
		else:
#			print 'not found %d' % (max_value)
			newPi.append(Pi[i])
	return newPi

def biggest_prime_in (num):
	biggest = 2
	for i in xrange(num - 1, 1, -1):
		if num % i == 0:
			biggest = i
	return biggest

def rec_cut2 (Pi):
	newPi = []
	Pi = Pi
	max_value = max(Pi)
	if max_value == 1:
		return None
	foundMax = False
#	print 'max = %d %r' % (max_value, Pi)
	for i in xrange(0, len(Pi)):
#		if max_value % 2 != 0:
#			newPi.append(Pi[i] - 1)
		if foundMax == False and Pi[i] == max_value:
#			print 'found %d' % (max_value)
			divider = biggest_prime_in(Pi[i])
			half1 = Pi[i] / divider
			half2 = Pi[i] - half1
			newPi.append(half1)
			newPi.append(half2)
			foundMax = True
		else:
#			print 'not found %d' % (max_value)
			newPi.append(Pi[i])
	return newPi

def process_min_num_minutes (D, Pi):
	tests = []
	max_value = max(Pi)
	tests.append(max_value)
	num_maxes = Pi.count(max_value)
	"""
	newPi = []
	special_mins = 0
	for i in xrange(0, len(Pi)):
		halfmax1 = max_value / 2
		halfmax2 = max_value - halfmax1
		if Pi[i] > halfmax2:
			half1 = Pi[i] / 2
			half2 = Pi[i] - half1
			newPi.append(half1)
			newPi.append(half2)
			special_mins += 1
		else:
			newPi.append(Pi[i])
	tests.append(special_mins + max(newPi))
	"""
	found = False
	special_mins = 0
	oldPi = Pi
#	print '\n'
	while found == False:
#		print oldPi, "--"
		newPi = rec_cut(oldPi)
#		print newPi
#		break
		if newPi == None:
#			print 'tests: %r' % (tests)
			found = True
		else:
			special_mins += 1
			tests.append(special_mins + max(newPi))
		oldPi = newPi

	found = False
	special_mins = 0
	oldPi = Pi
	while found == False:
		newPi = rec_cut2(oldPi)
		if newPi == None:
			found = True
		else:
			special_mins += 1
			tests.append(special_mins + max(newPi))
		oldPi = newPi
		pass


#	print 'Case #%d: %d - %dx%d %r' % (i + 1, min(tests), max_value, num_maxes, Pi)
	print 'Case #%d: %d' % (i + 1, min(tests))


T = read_int() # number of test cases

for i in xrange(0, T):
#	print i
	D = read_int() # number of non-empty plates
	Pi = read_ints() # number of pancakes on the diners plates
	process_min_num_minutes(D, Pi)
#	if i == 5:
#		break
	pass
