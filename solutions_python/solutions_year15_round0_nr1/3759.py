import sys




def read_lines(file_path):
	return open(file_path, 'r').read()


if __name__ == '__main__':
	txt = read_lines(sys.argv[1])

	result = txt.split('\n')
	print "----INPUT----"
	print result
	nbr_test_case = int(result[0])
	print "----OUTPUT----"
	for i in range(1, nbr_test_case + 1):
		# print "----index----"
		# print i 
		test_case = result[i]
		# print "----TEST CASE---- %d" % i
		# print test_case
		test_case = test_case.split(' ')
		nbr_person = int(test_case[0])
		case = test_case[1]
		invited_person = 0
		current_audience = 0
		for j in range(nbr_person + 1):
			# print case[i]
			if int(case[j]) == 0:
				continue

			if j > current_audience:
				invited_person += j - current_audience
				current_audience += invited_person
			current_audience += int(case[j])

		# print "invited_person %d" % invited_person
		print "Case #{0}: {1}".format(i, invited_person)