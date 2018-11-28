from __future__ import print_function

__author__ = 'shreyas kulkarni (shyran@gmail.com)'

import fileinput

input_lines = [line.strip() for line in fileinput.input()]

testCaseCounter = 1
for x in range(1, len(input_lines), 10):
    set1 = set([int(v) for v in input_lines[x + int(input_lines[x])].split()])
    set2 = set([int(v) for v in input_lines[x + 5 + int(input_lines[x + 5])].split()])

    common_vals = set1 & set2
    if len(common_vals) == 0:
        result = "Volunteer cheated!"
    elif len(common_vals) == 1:
        result = str(common_vals.pop())
    elif len(common_vals) > 1:
        result = "Bad magician!"

    print("Case #%d: %s" % (testCaseCounter, result))
    testCaseCounter += 1
