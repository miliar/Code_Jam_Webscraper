from __future__ import division

__author__ = "huynh.trung.anh@gmail.com (Anh Huynh)"

def read(file_name):
	"""
		Read input file
		Args:
			file_name: str
		Returns:

	"""
	fi = open(file_name, "rb")
	number_test_cases = int(fi.readline())

	case_dict = read_case(fi, number_test_cases)

	fi.close()
	return (number_test_cases, case_dict)

def read_case(fi, number_test_cases):
	"""
		Read relevant data for each case,
		depending on the problem
	"""
	case_dict = {}
	# make changes here

	## Africa2010 Store Credit
	for case in xrange(number_test_cases):
		case_dict[case] = []
		first_answer = int(fi.readline())
		first_arrangement = [map(int, fi.readline().split(" ")) for _ in xrange(4)]
		second_answer = int(fi.readline())
		second_arrangement = [map(int, fi.readline().split(" ")) for _ in xrange(4)]
		case_dict[case] = [first_answer, first_arrangement, second_answer, second_arrangement]

	return case_dict

def write(file_name, number_test_cases, answer):
	"""
		Write output file
		Args:
			file_name: str
		Returns:

	"""
	# make changes here

	## Africa2010 Store Credit
	fo = open(file_name, "wb")
	for i in range(number_test_cases):
		fo.write("Case #%d: %s\n" % (i+1, answer[i]))

	fo.close