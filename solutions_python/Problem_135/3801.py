#!/usr/bin/python3

import sys

input_file = sys.argv[-1]

file = open(input_file, 'r')

twerk = file.readlines()

num_test_cases = int(twerk[0])

cursor = 1
case = 1
cursor_final = (num_test_cases * 10) - 9

while cursor <= cursor_final:
	first_row_index = int(twerk[cursor])
	second_row_index = int(twerk[cursor+5])

	first_row = twerk[first_row_index + cursor].split()
	second_row = twerk[second_row_index + cursor + 5].split()

	found = []
	for item in first_row:
		if item in second_row:
			found.append(item)
	
	found_len = len(found)

	if found_len == 0:
		print("Case #", case, ": Volunteer cheated!", sep='')
	elif found_len > 1:
		print("Case #", case, ": Bad magician!", sep='')
	else:
		print("Case #", case, ": ", found[0], sep='')

	cursor = cursor + 10
	case = case + 1

