import sys

import numpy as np


f = open(sys.argv[1])
out = open('test.txt', 'w')
T = int(f.readline().strip())

case = 1
for cases in range(T):
    first_answer = int(f.readline().strip())
    orig_matrix = np.array([[f.readline().strip()] for i in range(4)])
    second_answer = int(f.readline().strip())
    new_matrix = np.array([[f.readline().strip()] for j in range(4)])
    first_row = orig_matrix[first_answer - 1]
    second_row = new_matrix[second_answer - 1]

    first_row_string = first_row[0].split(" ")
    second_row_string = second_row[0].split(" ")
    string_diff = [d for d in second_row_string if d not in first_row_string]

    if len(string_diff) < 3:
        out.write("Case #%i: Bad magician!\n" % case)

    if len(string_diff) == 3:
        eq = set(first_row_string) & set(second_row_string)
        eq_str = repr(eq)
        eq_str_strip = eq_str.strip("{'}")
        out.write("Case #%i: %s\n" % (case, eq_str_strip))

    if len(string_diff) == 4:
        out.write("Case #%i: Volunteer cheated!\n" % case)
    case += 1
