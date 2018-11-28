#!/usr/bin/env python


# Files
# input_file_name = 'A-small-attempt1.in'
# output_file_name = 'A-small-attempt1.out'
input_file_name = 'A-large.in'
output_file_name = 'A-large.out'
# input_file_name = 'test.in'
# output_file_name = 'test.out'

input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')


# Logic
num_cases = int(input_file.readline())
for case in range(1, num_cases+1):
    result = 0
    tokens = input_file.readline().split()
    flipper = int(tokens[1])  # size of the flipper
    pancakes = map(
        lambda x: True if x == '+' else False,
        tokens[0]
    )
    # print pancakes
    if False in pancakes:
        for i in range(len(pancakes) - flipper + 1):
            if pancakes[i] is False:
                for j in range(flipper):
                    pancakes[i+j] = not pancakes[i+j]
                result += 1
        if False in pancakes:
            result = "IMPOSSIBLE"

    # print "Case #" + str(case) + ": " + str(result)
    output_file.write("Case #" + str(case) + ": " + str(result) + '\n')


# Clean up
input_file.close()
output_file.close()
