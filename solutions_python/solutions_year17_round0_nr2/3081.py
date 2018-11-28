#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(inp):
	numbers_list = [int(i) for i in list(inp)]
	offending_numbers = None
	for i in range(len(numbers_list)-1):
		if numbers_list[i] > numbers_list[i+1]:
			offending_numbers = (numbers_list[i], numbers_list[i+1])
			break
	if offending_numbers is None:
		return inp
	elif offending_numbers[0] == 1 and offending_numbers[1] == 0:
		return '9' * (len(numbers_list) - 1)
	else:
		index_first_offending_number = numbers_list.index(offending_numbers[0])
		new_list = [str(i) for i in numbers_list[:index_first_offending_number]]
		new_list += [str(offending_numbers[0] - 1)]
		new_list += ['9'] * (len(numbers_list) - index_first_offending_number - 1)
		
		return ''.join(new_list)

				
if __name__ == '__main__':
	testcases = int(input())

	for case in range(testcases):
		inp = raw_input()
		print("Case #{}: {}".format(case+1, main(inp))) 
