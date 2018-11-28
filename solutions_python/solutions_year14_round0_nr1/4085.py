from itertools import *
import fileinput

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)

def parse_case(ten_lines):
    return [
        parse_subcase(ten_lines[:5]),
        parse_subcase(ten_lines[5:])
    ]
    
def parse_subcase(five_lines):
    answer = int(five_lines[0])
    grid = parse_grid(five_lines[1:])
    return {'answer':answer, 'grid':grid}

def parse_grid(four_lines):
    grid = []
    for line in four_lines:
        row = [int(x) for x in line.split(' ')]
        grid.append(row)
    return grid

def subcase_possibilities(subcase):
    row_index = subcase['answer']-1
    return set(subcase['grid'][row_index])

def solve_case(parsed_case):
    first_try = parsed_case[0]
    possibilities = subcase_possibilities(first_try)
    second_try = parsed_case[1]
    second_possibilities = subcase_possibilities(second_try)
    
    answer = possibilities.intersection(second_possibilities)
    if len(answer) == 0:
        return "Volunteer cheated!"
    elif len(answer) == 1:
        return str(answer.pop())
    else:
        return "Bad Magician!"
    

f = open('A-small-attempt0.in', 'r')
num_test_cases = int(f.readline())

cases = grouper(f, 10)
case_number = 1
for case in cases:
    parsed_case = parse_case(case)
    print ("Case #%d: " % case_number) + solve_case(parsed_case)
    case_number += 1
f.close()
