import os

import math

__author__ = 'Roberto'
import heapq

def finish(index, solution):

    print solution

    file_out.write("Case #{0}: {1}\n".format(index+1, solution))
    debug_out.write("{0}\n".format( solution))

def solve_test(index, test_case):

    debug_out.write("Case #{0} In: {1} Out: ".format(index, test_case))

    print "Case: [{0}]".format(test_case)

    N, K = map(int, test_case.split())

    finish(index, "{0} {1}".format(*solve(N, K)))

def solve(N, K):

    if N % 2 == 0:
        if K == 1:
            return (N / 2, (N / 2) - 1)

        elif K % 2 == 0:
            return solve(N / 2, K / 2)

        else:
            return solve((N / 2) - 1, (K - 1) / 2)

    else:
        if K == 1:
            return (N/ 2, N / 2)

        elif K % 2 == 0:
            return solve((N - 1) / 2, K / 2)

        else:
            return solve((N - 1) / 2, (K - 1) / 2)

if __name__ == "__main__":

    task = os.path.basename(os.path.dirname(__file__))
    level = 2
    attempts = 0

    if level == 0:
        file_name = "sample.in"
    elif level == 1:
        file_name = "{0}-small-2-attempt{1}.in".format(task, attempts)
    else:
        file_name = "{0}-large.in".format(task)



    file_out_name = file_name.replace("in", "out")
    file_out = open(file_out_name, 'w')
    debug_out = open(file_name.replace("in", "debug"), 'w')

    with open(file_name, 'r') as file:
        content = file.read()

    lines = content.split('\n')
    number_of_lines = int(lines[0])

    test_cases = lines[1:]

    for i in xrange(0, number_of_lines):

        solve_test(i, test_cases[i])

    file_out.close()