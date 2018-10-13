#!/usr/bin/env python3

import sys

input = open(sys.argv[1], "r")
output = open("output.out", "w")

test_cases = int(input.readline())

for case in range(0, test_cases):
    first = int(input.readline()) - 1
    first_rows = []
    for index in range(0, 4):
        first_rows.append(input.readline().split())
    second = int(input.readline()) - 1
    second_rows = []
    for index in range(0, 4):
        second_rows.append(input.readline().split())
    answer = set(first_rows[first]).intersection(set(second_rows[second]))

    output_string = "Case #" + str(case + 1) + ": "

    if not answer:
        output_string += "Volunteer cheated!"
    elif len(answer) == 1:
        output_string += str(list(answer)[0])
    elif len(answer) > 1:
        output_string += "Bad magician!"

    output.write(output_string + "\n")

input.close()
output.close()

