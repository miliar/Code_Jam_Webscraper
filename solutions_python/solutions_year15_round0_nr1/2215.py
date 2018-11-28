__author__ = 'Jeffrey Burton'


import numpy as np


text = open('problem1text.txt')
output = open('output.txt', 'w')
number_of_test_cases = text.readline()

try:
    number_of_test_cases = int(number_of_test_cases)
except:
    pass

line_number = 0
valid = True
for line in text:
    line_number += 1
    if line_number > number_of_test_cases and valid:
        print "## number of test cases is larger than the line number"
        valid = False
    max_shyness, shyness_array = line.split()
    max_shyness = int(max_shyness)
    shyness_string = list(shyness_array)
    array = np.zeros((max_shyness + 1), dtype=int)
    for i in xrange(0, max_shyness + 1):
        try:
            array[i] = int(shyness_string[i])
        except:
            array[i] = 0

    running_sum = 0
    num_extras = 0
    for j in xrange(1, max_shyness + 1):
        running_sum += array[j - 1]
        if j > running_sum + num_extras:
            num_extras += j - running_sum - num_extras
    output.write("Case #" + str(line_number) + ": " + str(num_extras) + '\n')

text.close()
output.close()

