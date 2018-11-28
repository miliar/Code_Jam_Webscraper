#!/usr/bin/python
import resource, sys

# Result printer
def print_results(case, result):
    print 'Case #' + str(case) + ': ' + str(result[0]) + ' ' + str(result[1])

# Recursive solve
def pow_solve(n, intervals):
    
    new = max(intervals)
    intervals.remove(new)

    if new % 2 == 0:
        if n == 1:
            return (new / 2, new / 2 - 1)
        intervals.append(new / 2)
        intervals.append(new / 2 - 1)

    else:
        if n == 1:
            return (int(new / 2), int(new / 2))
        intervals.append(int(new / 2))
        intervals.append(int(new / 2))

    return pow_solve(n - 1, intervals)

# Loop instead of recursion
def pow_solve_loop(n, size):
    
    intervals = [(size, 1)]
    sol1 = 0
    sol2 = 0

    for i in xrange(n):
        
        new = max(intervals, key=lambda i: i[0])
        index = intervals.index(new)
        if new[1] <= 1:
            del intervals[index]
        else:
            intervals[index] = (intervals[index][0], intervals[index][1] - 1)

        new = new[0]

        if new % 2 == 0:
            sol1 = new / 2
            sol2 = new / 2 - 1
            intervals.append((new / 2, 1))
            intervals.append((new / 2 - 1, 1))

        else:
            sol1 = new / 2
            sol2 = new / 2
            intervals.append((int(new / 2), 2))

        set_list = set([elem[0] for elem in intervals])
        
        new_intervals = []
        for set_elem in set_list:
            new_intervals.append((set_elem, sum([elem[1] for elem in intervals if elem[0] == set_elem])))

        intervals = new_intervals
        n -= 1

    return (sol1, sol2)

# Solver function
def solve(N, K):

    if N == 1 or N == K:
        return (0, 0)

    last = pow_solve_loop(K, N)

    return last

nb_tests = int(raw_input())

for i in range(nb_tests):

    # Initialization
    N, K = [int(n) for n in raw_input().split()]

    # Solving
    result = solve(N, K)

    # Printing results
    print_results(i + 1, result)
