#!/usr/bin/python

import sys

def read_matrix():
    rows = []
    for _ in range(4):
        str_row = sys.stdin.readline().strip().split()
        row = []
        for num in str_row:
            row.append(int(num))
        rows.append(row)
    return rows

def hasNum(num, array):
    if num in array:
        return True
    else:
        return False

def distinct(row1, row2):
    found_num = None
    for num in row1:
        has = hasNum(num, row2)
        if has == True:
            if found_num is not None:
                return "Bad magician!"
            found_num = num
    
    if found_num is None:
        return "Volunteer cheated!"
    else:
        return str(found_num)

# MAIN
test_count = int(sys.stdin.readline().strip())

for this_round in range(test_count):
    answer1 = int(sys.stdin.readline().strip())
    matrix1 = read_matrix()

    answer2 = int(sys.stdin.readline().strip())
    matrix2 = read_matrix()


    result = distinct(matrix1[answer1-1], matrix2[answer2-1])
    print("Case #" + str(this_round+1) + ": " + result)
