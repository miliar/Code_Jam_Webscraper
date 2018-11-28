#!/usr/bin/python

from sys import stdin, stdout

total_cases = int( stdin.readline() )
input = stdin.readlines()

results = []
for case_num in range(total_cases):
    summary = input[case_num*2]
    groups = input[case_num*2+1]
    rounds, capacity, n_groups = [int(n) for n in summary.split(' ')]
    group_sizes = [int(n) for n in groups.split(' ')]

    positions = []
    for n in range(n_groups):
        size = group_sizes[n]
        next = (n+1) % n_groups
        while size <= capacity and next != n:
            if size + group_sizes[next] <= capacity:
                size += group_sizes[next]
                next = (next+1) % n_groups
            else:
                break
        positions.append((size, next))
#        print "(%d, %d)" % (size, next)

    pos, profit = 0, 0
    for r in range(rounds):
        profit += positions[pos][0]
        pos = positions[pos][1]

    results.append("Case #%d: %d\n" % (case_num+1, profit))

stdout.writelines(results)
