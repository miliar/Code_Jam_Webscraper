
import numpy as np

inputfile = 'A-small-attempt4.in'
outputfile = 'outputfile.txt'

fi = open(inputfile)
fo = open(outputfile, 'w')
size = 4

matrix_1 = []
matrix_2 = []

test_cases = int(fi.readline())
print test_cases
for case in range(test_cases):
	answer_1 = int(fi.readline())
	matrix_1 = []
	for i in range(size):
		line = fi.readline()
		values = []
		values = line.split(' ')
		values = map(int, values)
		matrix_1.append(values)

	row_1 = matrix_1[answer_1-1]
	answer_2 = int(fi.readline())
	matrix_2 = []
	for i in range(size):
		line = fi.readline()
		values = []
		values = line.split(' ')
		values = map(int, values)
		matrix_2.append(values)

	row_2 = matrix_2[answer_2-1]
	intersection = list(set(row_1).intersection(set(row_2)))
	
	if len(intersection) == 1:
		fo.write('Case #' + str(case + 1) + ': ' + str(intersection[0]) + '\n')
	elif len(intersection) > 1: 
		fo.write('Case #' + str(case + 1) + ': Bad magician!' + '\n')
	elif len(intersection) == 0: 
		fo.write('Case #' + str(case + 1) + ': Volunteer cheated!' + '\n')
	

