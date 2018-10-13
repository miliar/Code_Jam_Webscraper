#!/usr/bin/env python
# Python 2.6.6

t = int(raw_input())

for tc in xrange(1, t+1):
    case = raw_input().split()
    c = int(case[0])
    d = int(case[c+1])
    n = int(case[c+d+2])
    combine = {}
    for s1, s2, p in (case[i] for i in xrange(1, c+1)):
        combine[frozenset([s1, s2])] = p
    opposed = {}
    for l, r in (case[i] for i in xrange(c+2, c+2+d)):
        opposed.setdefault(l, set()).add(r)
        opposed.setdefault(r, set()).add(l)
    to_invoke = list(case[c+d+3])
    elem_lst = [to_invoke[0]]
    elem_set = set(elem_lst)
    for e in to_invoke[1:]:
        elem_lst.append(e)
        elem_set.add(e)
        while True:
            if len(elem_lst) > 1 and frozenset(elem_lst[-2:]) in combine:
                p = combine[frozenset(elem_lst[-2:])]
                elem_lst[-2:] = [p]
                elem_set = set(elem_lst)
            else:
                break
        if (len(elem_lst) > 0 and
            elem_lst[-1] in opposed and
            len(opposed[elem_lst[-1]] & elem_set) > 0):
            elem_lst = []
            elem_set = set(elem_lst)
    print("Case #%d: [%s]" % (tc, ", ".join(elem_lst)))
