#!/usr/env python3
# -*- coding: utf-8 -*-


def resolve_ttt(grid, case):
    dot = 0
    for line in range(4):
        sequence = 0
        for col in range(4):
            if grid[line][col] == '.':
                dot += 1
                break
            elif col == 0 or grid[line][col] == 'T':
                sequence += 1
            elif grid[line][col] == grid[line][col-1]:
                sequence += 1
            if sequence == 4:
                test = grid[line][col]
                if test == 'T':
                    test = grid[line][col-1]
                return "Case #" + str(case) + ": " + str(test) + " won"
    for col in range(4):
        sequence = 0
        for line in range(4):
            if grid[line][col] == '.':
                dot += 1
                break
            elif line == 0 or grid[line][col] == 'T':
                sequence += 1
            elif grid[line][col] == grid[line-1][col]:
                sequence += 1
            if sequence == 4:
                test = grid[line][col]
                if test == 'T':
                    test = grid[line-1][col]
                return "Case #" + str(case) + ": " + str(test) + " won"
    for diag in range(1):
            sequence = 0
            sequence2 = 0
            for count in range(4):
                col2 = -(count+1)
                if (count == 0 and grid[count][count] != '.') or (count == 0 and grid[count][col2] != '.'):
                    sequence += 1
                    sequence2 += 1
                if count != 0 and grid[count][count] == 'T':
                    sequence += 1
                if count != 0 and grid[count][col2] == 'T':
                    sequence2 += 1
                if count != 0 and (grid[count][count] == grid[count-1][count-1] or grid[count-1][count-1] == 'T') :
                    sequence += 1
                if count != 0 and (grid[count][col2] == grid[count-1][col2+1] or grid[count-1][col2+1] == 'T'):
                    sequence2 += 1
                if sequence == 4:
                    test = grid[count][count]
                    if test == 'T':
                        test = grid[count-1][count-1]
                    return "Case #" + str(case) + ": " + str(test) + " won"
                if sequence2 == 4:
                    test = grid[count][col2]
                    if test == 'T':
                        test = grid[count-1][col2+1]
                    return "Case #" + str(case) + ": " + str(test) + " won"

    if dot > 0:
        return "Case #" + str(case) + ": " + "Game has not completed"
    else:
        return "Case #" + str(case) + ": " + "Draw"
test_case = int(input())

for case in range(test_case):
    grid = []
    for raw in range(4):
        grid.append(input())
    if case != test_case - 1 :
        a = input()

    result = resolve_ttt(grid, case + 1)
    print(result)


