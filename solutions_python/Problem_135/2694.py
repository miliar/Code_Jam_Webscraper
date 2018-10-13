# -*- coding: utf-8 -*-

import fileinput

provider = fileinput.input()

test_cases_count = int(provider.next())

def read_test_case():
    lines = []
    for x in range(0, 10):
        lines.append(
            [ int(x) for x in provider.next().split() ])
    first_answer = lines[0][0]
    first_row = lines[first_answer]
    second_answer = lines[5][0]
    second_row = lines[5+second_answer]
    return first_row, second_row
        

for case_no in range(1, test_cases_count+1):
    row1, row2 = read_test_case()
    common = [x for x in row1 if x in row2]
    if len(common) > 1:
        reply = "Bad magician!"
    elif common:
        reply = str(common[0])
    else:
        reply = "Volunteer cheated!"
    print "Case #{0}: {1}".format(case_no, reply)

