#!/usr/bin/env python
#encoding: utf-8
from pprint import pprint

name_of_file = 'A-small-attempt0.in'
document = open(name_of_file, 'r')
lines = document.readlines()
document.close()

bad_magician='Bad magician!'
volunteer_cheated='Volunteer cheated!'

test_cases=[]
results=[]
ntest_cases=int(lines[0])

for i in range(0, ntest_cases):
	test_cases.append(
		{'first_try_row': int(lines[(i*10)+1]),
		 'first_try': [
		 	lines[(i*10)+2].split(' '),lines[(i*10)+3].split(' '),
		 	lines[(i*10)+4].split(' '),lines[(i*10)+5].split(' ')
		 ],
		 'second_try_row': int(lines[(i*10)+6]),
		 'second_try':[
		 	lines[(i*10)+7].split(' '), lines[(i*10)+8].split(' '), 
		 	lines[(i*10)+9].split(' '), lines[(i*10)+10].split(' ')
		 ]
		}
	)
pprint(test_cases)

for test_case in test_cases:
	first_row = set([int(x) for x in \
				test_case['first_try'][test_case['first_try_row']-1]])
	second_row = set([int(x) for x in\
				test_case['second_try'][test_case['second_try_row']-1]])
	print first_row
	print second_row
	common_elements = first_row.intersection(second_row)
	if len(common_elements) == 0:
		results.append(volunteer_cheated)
	elif len(common_elements) > 1:
		results.append(bad_magician)
	else:
		results.append(list(common_elements)[0])

resultset = open('result_' + name_of_file, 'w')

for i in range(1, ntest_cases + 1):
	resultset.write('Case #%(number)s: %(result)s\n'\
				% {'number': i, 'result': results[i - 1]})

resultset.close()