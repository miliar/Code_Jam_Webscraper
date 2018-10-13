#!/usr/bin/python

import sys

def validate(num, choice0, choice1, layout0, layout1):
    output = 'Case #' + str(num + 1) + ': '
    intersect = set(layout0[choice0-1]).intersection(set(layout1[choice1-1]))
    if (len(intersect) == 0):
      output += 'Volunteer cheated!'
    elif (len(intersect) == 1):
      output += str(intersect.pop())
    else:
      output += 'Bad magician!'
    print output

def parse_input(file_pointer):
    lines = file_pointer.readlines()
    num_cases = int(lines[0])
    for i in range(num_cases):
        choice0 = int(lines[i * 10 + 1])
        choice1 = int(lines[i * 10 + 6])
        layout0 = []
        layout1 = []
        for j in range(4):
            list0 = [int(k) for k in lines[i * 10 + 2 + j].split(' ')]
            layout0.append(list0)
            list1 = [int(k) for k in lines[i * 10 + 7 + j].split(' ')]
            layout1.append(list1)
        validate(i, choice0, choice1, layout0, layout1)

def read_file(file_name):
    return open(file_name, 'r')

# main
file_pointer = read_file(sys.argv[1])
parse_input(file_pointer)
