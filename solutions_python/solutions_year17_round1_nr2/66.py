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
				case = []
				assert len(line.strip().split(' ')) == 2
				lines_left = int(line.strip().split(' ')[0]) + 1
                                case = [line.strip().split(' ')]
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
#### add solution here 									####
#### don't forget to change data from str to int/float  ####
############################################################


def calc_result(case):
    #print case
    N, P = list_to_int(case[0])
    Gs = list_to_int(case[1])
    assert len(Gs) == N
    Qs = [list_to_int(row) for row in case[2:]]
    Floats = [[float(q)/Gs[n] for q in row] for n, row in enumerate(Qs)]
    # Nums = [[int(round(f)) for f in row if 0.9 <= f / int(round(f)) <= 1.1] for row in Floats]
    #print N, P
    #print Gs
    #print Qs

    [row.sort() for row in Floats]
    #print Floats
    count = 0
    while all(Floats):
        Floats.sort(reverse=True)
        #print count, Floats,
        max_min_f = Floats[0].pop(0)
        max_min = int(math.ceil(max_min_f / 1.1))
        if not 0.9 <= max_min_f / max_min <= 1.1:
            #print 'bad'
            continue
        #print max_min
        for row in Floats[1:]:
            while row:
                elem = row.pop(0)
                if elem / max_min < 0.9:
                    continue
                break
            else:
                return count
            if elem / max_min > 1.1:
                row.insert(0, elem)
                break
            # 0.9 <= elem / max_min <= 1.1, continue
        else:
            count += 1
            continue
        # found bigger than max_min, continue

    return count

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
                        print result

			#######################
			#### format output ####
			#######################
			f_out.write("Case #%d: %s\n" % (case_index, result))
	print time.time() - start_time

if __name__ == '__main__':
	main(sys.argv[1])
