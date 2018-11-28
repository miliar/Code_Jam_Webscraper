#!/usr/bin/python

# Result printer
def print_results(case, result):
    print 'Case #' + str(case) + ': ' + str(result)

# Checks if a number is tidy
def isTidy(number):
    strn = str(number)

    current = strn[0]

    for elem in strn:
        if elem < current:
            return False
        current = elem

    return True

# Solver function
def solve(number):
    for n in range(number, 1, -1):
        if isTidy(n):
            return n

    return 1

nb_tests = int(raw_input())

for i in range(nb_tests):

    # Initialization
    number = int(raw_input())

    # Solving
    result = solve(number)

    # Printing results
    print_results(i + 1, result)
