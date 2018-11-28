#!/usr/bin/env python3

import fileinput

user_input = fileinput.input()

T = int(user_input.readline().rstrip())

def read_grid():
    grid = []
    for r in range(4):
        row = []
        for c in user_input.readline().split():
            row.append(int(c))
        grid.append(row)    
    return grid

for case in range(1, T+1):
    answer = ""

    first_hint = int(user_input.readline())
    first_grid = read_grid()
    second_hint = int(user_input.readline())
    second_grid = read_grid()    

    possible_first = set(first_grid[first_hint - 1])
    possible_second = set(second_grid[second_hint - 1])
    
    final = possible_first.intersection(possible_second)

    #print(possible_first, possible_second, final)

    if len(final) == 1:
        answer = final.pop()
    elif len(final) > 1:
        answer = 'Bad magician!'
    else:
        answer = 'Volunteer cheated!'
    
    print("Case #{:d}: {}".format(case, answer))
