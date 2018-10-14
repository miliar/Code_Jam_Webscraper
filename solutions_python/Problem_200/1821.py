#!/usr/bin/env python


# Files
# input_file_name = 'B-small-attempt0.in'
# output_file_name = 'B-small-attempt0.out'
input_file_name = 'B-large.in'
output_file_name = 'B-large.out'
# input_file_name = 'test.in'
# output_file_name = 'test.out'

input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')


# Logic
num_cases = int(input_file.readline())
for case in range(1, num_cases+1):
    numbers = [int(x) for x in input_file.readline().strip()]
    if len(numbers) != 1:
        while not all(numbers[i] <= numbers[i+1] for i in xrange(len(numbers)-1)):  # while the number is not "tidy"
            for j in range(len(numbers)-1):
                if numbers[j] > numbers[j+1]:  # if these two numbers are not themselves "tidy"...
                    for k in range(j+1, len(numbers)):
                        numbers[k] = 9  # set the second number and each one to the end of the list to 9
                    numbers[j] -= 1  # reduce the current number by one (don't have to worry about zero here)
                    break

    # print "Case #" + str(case) + ": " + ''.join(map(str, numbers)).lstrip('0')
    output_file.write("Case #" + str(case) + ": " + ''.join(map(str, numbers)).lstrip('0') + '\n')


# Clean up
input_file.close()
output_file.close()
