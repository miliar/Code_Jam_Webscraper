#!/usr/bin/env python
# -*- coding: utf-8 -*-

def f(combine, oppose, bases):
    l = []
    for b in bases:
        if not l:
            l.append(b)
            continue
        if (b, l[-1]) in combine:
            l[-1] = combine[(b, l[-1])]
        elif b in oppose and set(l) & oppose[b]:
            l = []
        else:
            l.append(b)
    return l

n = int(raw_input())
for case in range(1, n+1):
    data = raw_input().split()
    c, data = int(data[0]), data[1:]
    c_strs, data = data[:c], data[c:]
    d, data = int(data[0]), data[1:]
    d_strs, data = data[:d], data[d:]
    _, bases = data
    combine_dict = {}
    for b1, b2, e in c_strs:
        combine_dict[(b1, b2)] = e
        combine_dict[(b2, b1)] = e
    oppose_dict = {}
    for b1, b2 in d_strs:
        oppose_dict.setdefault(b1, set()).add(b2)
        oppose_dict.setdefault(b2, set()).add(b1)
    res = f(combine_dict, oppose_dict, bases)
    print 'Case #{0}: [{1}]'.format(case, ', '.join(res))

