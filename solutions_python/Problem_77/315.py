#!/opt/local/bin/python

from itertools import combinations
import operator
import sys
from random import shuffle
from fractions import Fraction

#                 + cycle length
#                 | 
#                 | 
# f(n) -> 1/n * (f(1)   + max(1, f(n-1)))
#       + 1/n * (f(2)   + max(1, f(n-2)))
#       + 1/n * (f(3)   + max(1, f(n-3)))
#       + ...
#       + 1/n * (f(n-1) + max(1, f(1)  )) = f(n-1) + 1
#       + 1/n * (f(n)   + max(1, f(0)  ))
# 
# f: sorting n without any correctly placed
# 
# f(0) = 0
# 
# f(1) = 0
# 
# f(2) = 1/2 * (0 + 1) + 1/2 * (f(2) + 1)
#      = 1/2 + 1/2 * f(2) + 1/2
# 1/2 * f(2) = 1
# f(2) = 2
# 
# f(3) = 1/3 * (0 + 2) + 1/3 * (2 + 1) + 1/3 * (f(n) + 1)
#      = 2/3 + 3/3 + f(n)/3 + 1/3
# 2/3 * f(3) = 6/3
# f(3) = 3/2 * 6/3 = 6/2
# 
# (n-1)/n * f(n) = 1/n * sum(f(i) + max(1, f(n-i)) for i in range(1,n)) + 1/n
# f(n) = 1/(n-1) * sum(f(i) + max(1, f(n-i)) for i in range(1,n))

# f = [Fraction(0), Fraction(0)]
# for n in range(2, 101):
#     numerator = sum(f[i] + max(1, f[n-i]) for i in range(1, n)) + 1
#     denominator = n-1
#     frac = numerator / denominator
#     f.append(frac)
# 
# print 'f:', f

########################################
# f[i] = 0 if i < 2 else i
########################################

def time_to_sort(n):
    return 0 if n < 2 else n


input_it = iter(sys.stdin.readlines())
T = int(input_it.next())

for case in range(T):
    N = int(input_it.next())
    values = [int(i) for i in input_it.next().split()]

    cycles = []
    cycle = []
    in_cycle = [False for value in values]
    for i, value in enumerate(values):
        if in_cycle[i]:
            continue
        else:
            # print 'i, value, in_cycle', i, value, in_cycle
            in_cycle[i] = True
            cycle.append(i)
            # print 'cycle', cycle
            j = value - 1
            while j != i:
                in_cycle[j] = True
                cycle.append(j)
                # print 'cycle', cycle
                j = values[j] - 1
            cycles.append(cycle)
            cycle = []

    # print cycles

    result = sum(time_to_sort(len(c)) for c in cycles)

    print 'Case #%s: %.6f' % (case + 1, result)

