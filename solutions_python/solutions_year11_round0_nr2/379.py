#! /usr/bin/env python

#usage: cat input | this_program > output

import sys

num_testcases = int(sys.stdin.readline())

### main
for case in range(1, num_testcases + 1):
    data = sys.stdin.readline().split()
    c = int(data[0])
    combine = data[1: 1 + c]
    combine = dict((frozenset((i, j)), k) for i, j, k in combine)
    d = int(data[1 + c])
    destroy = data[2 + c: 2 + c + d]
    invoke = data[-1]
    result = []
    for element in invoke:
        if result == []:
            result.append(element)
            continue
        e = result[-1]
        key = frozenset([e, element])
        if key in combine:
            result[-1] = combine[key]
            continue
        destroy_candidates = [d for d in destroy if element in d]
        destroy_candidates = map(lambda d: d[1] if d[0] == element else d[0],
                                 destroy_candidates)
        for d in destroy_candidates:
            if d in result:
                result = []
                break
        else:
            result.append(element)
    res_str = "[" + ", ".join(result) + "]"
    print "Case #%i: %s" %(case, res_str)
