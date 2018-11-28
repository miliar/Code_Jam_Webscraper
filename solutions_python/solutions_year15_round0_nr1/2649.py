#!/usr/bin/python

import sys

def analyze(file_name):
	input_file = open(file_name, 'r')
	output_file = open(file_name.replace('.in', '.out'), 'w')

	all_data = iter(input_file.readlines())

	test_cases = int(all_data.next())
	for i in range(0, test_cases):
		each_case = iter(all_data.next().split(' '))
		s_max = int(each_case.next())
		s = list()
		for k in each_case.next().lstrip().rstrip():
			s.append(int(k))
		
		cumulative_person = s[0]
		extra_person = 0

		for (shyness, person) in enumerate(s[1:]):
			for p in range(person):

				# if cumulative_person < shyness+1:
				# 	extra_person += 1
				# 	# edited 
				# 	cumulative_person += 1
				# cumulative_person += 1

				#
				while True:
					if cumulative_person < (shyness + 1):
						extra_person += 1
						cumulative_person += 1
						continue
					else:
						cumulative_person += 1
						break 
				#
		output_file.write('Case #{}: {}\n'.format(i+1, extra_person))

	input_file.close()
	output_file.close()

if __name__ == '__main__':
	analyze(sys.argv[1])
