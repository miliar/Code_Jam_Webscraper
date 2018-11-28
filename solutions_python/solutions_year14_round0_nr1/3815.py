#!/usr/bin/python
input_file = open("A-small", 'r')
output_file = open("output", "w")
BAD_MAGICIAN = "Bad magician!"
CHEATED = "Volunteer cheated!"
SIZE = 4

nb_case = int(input_file.readline())

for case in range(nb_case):

    first_row_ind = int(input_file.readline())-1
    rows = []
    for _ in range(SIZE):
	rows.append(input_file.readline())
    first_row = rows[first_row_ind][:-1].split(' ')

    second_row_ind = int(input_file.readline())-1
    rows = []
    for _ in range(SIZE):
	rows.append(input_file.readline())
    second_row = rows[second_row_ind][:-1].split(' ')
   
    intersection = set(first_row).intersection(set(second_row))

    length = len(intersection)
    if length == 1:
	output_file.write('Case #%i: %s\n' % (case+1, list(intersection)[0]))
    elif length == 0:
	output_file.write('Case #%i: %s\n' % (case+1, CHEATED))
    else:
	output_file.write('Case #%i: %s\n' % (case+1, BAD_MAGICIAN))

input_file.close()
output_file.close()

