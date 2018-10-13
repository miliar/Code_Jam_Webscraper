import sys
import time
import itertools #use combinations!
import random
import math


def iterate_cases_1lpc(filepath):	#1lpc = 1 line per case
	with file(filepath, 'rb') as f_in:
		for line_index, line in enumerate(f_in):
			if line_index == 0: #T
				continue
			yield line_index, line.strip().split(' ')

def iterate_cases_nlpc(filepath, n):	#nlpc = n line per case
	with file(filepath, 'rb') as f_in:
		case_counter = 1
		case = []
		for line_index, line in enumerate(f_in):
			if line_index == 0: #T
				continue
			case.append(line.strip().split(' '))
			if not line_index % n:
				yield case_counter, case
				case_counter += 1
				case = []

def iterate_cases_glpc(filepath):		#glpc - given lines per case
	with file(filepath, 'rb') as f_in:
		case_counter = 0
		new_case = True
		for line_index, line in enumerate(f_in):
			if line_index == 0: #T
				continue
			if new_case:
				new_case = False
				case_counter += 1
				case = [line.strip().split(' ')]
				assert len(line.strip().split(' ')) == 3
				lines_left = int(line.strip().split(' ')[2])
				if not lines_left:
					new_case = True
					yield case_counter, case
				continue
			if lines_left:
				lines_left -= 1
				case.append(line.strip().split(' '))
			if not lines_left:
				new_case = True
				yield case_counter, case

def part_of_list_to_int(array, flags):
	assert len(array) == len(flags)
	output = []
	for index, elem in enumerate(array):
		if flags[index]:
			output.append(int(elem))
		else:
			output.append(elem)
	return output

def list_to_int(array):
	return part_of_list_to_int(array, [True] * len(array))

def part_of_list_to_float(array, flags):
	assert len(array) == len(flags)
	output = []
	for index, elem in enumerate(array):
		if flags[index]:
			output.append(float(elem))
		else:
			output.append(elem)
	return output

def list_to_float(array):
	return part_of_list_to_float(array, [True] * len(array))

def get_max_array_on_index(array, index):
	elem_len = len(array[0])
	assert index < elem_len
	for elem in array:
		assert elem_len == len(elem)
	max_sub = array[0][index]
	max_elem = array[0]
	for elem in array:
		if elem[index] > max_sub:
			max_sub = elem[index]
			max_elem = elem
	return max_elem

def list_index_in_sorted_with_position(a_list, value, pos):
	list_len = len(a_list)
	if list_len == 1:
		if a_list[0] == value:
			return pos
		return -1
	if a_list[list_len/2] > value:
		return list_index_in_sorted_with_position(a_list[:(list_len/2)], value, pos)
	else:
		return list_index_in_sorted_with_position(a_list[(list_len/2):], value, pos + (list_len/2))

def list_index_in_sorted_list(a_list, value):
	return list_index_in_sorted_with_position(a_list, value, 0)

def copy_list(list):
	res = []
	for elem in list:
		res.append(elem)
	return res

############################################################
#### add solution here 					####
#### don't forget to change data from str to int/float  ####
############################################################

def calc_result(case):
    print case
    N, C, M = list_to_int(case[0])
    Ms = [list_to_int(cc) for cc in case[1:]]
    print N, C, M
    print Ms

    trains = []
    proms = 0
    customers = {i: set() for i in xrange(C)}

    for m in sorted(Ms):
        seat = m[0] - 1
        customer = m[1] - 1
        for train_index, train in enumerate(trains):
            is_seated = False

            if train[seat] is None and train_index not in customers[customer]:
                train[seat] = customer
                customers[customer].add(train_index)
                is_seated = True

            if not is_seated:
                for s in range(seat-1,-1,-1):
                    if train[s] == 'STOP':
                        break
                    if train[s] is None and train_index not in customers[customer]:
                        train[s] = customer
                        customers[customer].add(train_index)
                        proms += 1
                        is_seated = True
                        break

            if is_seated:
                for i in xrange(N):
                    if train[i] is None:
                        break
                    train[i] = 'STOP'
                break

        else:
            trains.append([None] * N)
            trains[-1][seat] = customer
            customers[customer].add(len(trains) - 1)
    num_of_trains = len(trains)

    seats = {i: 0 for i in xrange(N)}
    for m in Ms:
        seat = m[0] - 1
        seats[seat] += 1

    min_proms = 0
    for seat, amount in seats.iteritems():
        min_proms += max(0, amount - num_of_trains)
    print num_of_trains
    print proms, min_proms

    result = '%d %d' % (num_of_trains, min_proms)
    return result

def main(filepath):
	start_time = time.time()
	with file('output.txt', 'wb') as f_out:

		######################################
		#### select input iteration type: ####
		####	- iterate_cases_1lpc	  ####
		####	- iterate_cases_nlpc +n	  ####
		####	- iterate_cases_glpc	  ####
		######################################
		for case_index, case in iterate_cases_glpc(filepath):

			print "case #%d: time:%.02f" % (case_index, time.time() - start_time)
			result = calc_result(case)

			#######################
			#### format output ####
			#######################
			f_out.write("Case #%d: %s\n" % (case_index, result))
	print time.time() - start_time

if __name__ == '__main__':
	main(sys.argv[1])
