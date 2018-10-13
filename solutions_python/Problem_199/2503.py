#!/usr/bin/python

# Result printer
def print_results(case, result):
    if result < 0:
        print 'Case #' + str(case) + ': IMPOSSIBLE'
    else:
        print 'Case #' + str(case) + ': ' + str(result)

# Flip all the pancakes in the list
def flip(pancakes, length):
    result = ''
    for i in range(length):
        if pancakes[i] == '-':
            result += '+'
        else:
            result += '-'
    return result

# Solver function
def solve(row, K):
    
    len_row = len(row)
    if row == len_row * '+':
        return 0

    if row == len_row * '-':
        if len_row % K != 0:
            return 'IMPOSSIBLE'
        else:
            return len_row / K
    
    steps = 0

    for i in range(0, len_row):
        if row[i] == '+':
            continue

        if i + K > len_row:
            return 'IMPOSSIBLE'

        row = row[:i] + flip(row[i:i + K], K) + row[i + K:len_row]
        steps += 1

    return steps

nb_tests = int(raw_input())

for i in range(nb_tests):

    # Initialization
    row, K = raw_input().split()
    K = int(K)

    # Solving
    result = solve(row, K)

    # Printing results
    print_results(i + 1, result)
