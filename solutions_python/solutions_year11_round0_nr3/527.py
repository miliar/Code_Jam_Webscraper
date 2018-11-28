#!/opt/local/bin/python

from itertools import combinations
import operator
import sys

input_it = iter(sys.stdin.readlines())
T = int(input_it.next())

for case in range(T):
    N = int(input_it.next())
    values = [int(i) for i in input_it.next().split()]
    values.sort()

    total_sum = sum(values)
    total_xor = reduce(operator.xor, values)

    subresult = None
    for nrof_candy in range(1, N):
        for for_patrick in combinations(values, nrof_candy):
            if subresult is not None and sum(for_patrick) > sum(subresult):
                break # to get the lowest only
            patrick_xor = reduce(operator.xor, for_patrick)
            sean_xor    = total_xor ^ patrick_xor
            if patrick_xor == sean_xor:
                subresult = for_patrick

    result = total_sum - sum(subresult) if subresult is not None else 'NO'

    print 'Case #%s: %s' % (case + 1, result)

