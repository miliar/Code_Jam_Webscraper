# -*- coding: utf-8 -*-

import sys
t = int(raw_input())

def solve(toinvoke, combine_rules, oppose_rules):
    res = '' 
    for e in toinvoke:
        if res:
            if combine_rules.has_key(res[-1] + e):
                res = list(res)
                res.append(combine_rules[res[-1] + e])
                res.pop(-2)
                res = ''.join(res)
            else:
                res += e
                for oppose_rule in oppose_rules:
                    if (oppose_rule[0] in res) and (oppose_rule[1] in res):
                        res = ''
        else:
            res += e
    return res

for i in xrange(1, t + 1):
    case = raw_input().split(' ')
    c = int(case.pop(0))
    combine_rules = {}
    for j in xrange(0, c):
        h = case.pop(0)
        combine_rules[h[0] + h[1]] = h[2]
        combine_rules[h[1] + h[0]] = h[2]
    d = int(case.pop(0))
    oppose_rules = []
    for j in xrange(0, d):
        h = case.pop(0)
        oppose_rules.append((h[0], h[1]))
    n = case.pop(0)
    toinvoke = case.pop(0)
    res = solve(toinvoke, combine_rules, oppose_rules)
    sys.stdout.write('Case #' + str(i) + ': [')
    for e in res[:-1]:
        sys.stdout.write(e + ', ')
    if res:
        sys.stdout.write(res[-1])
    sys.stdout.write(']\n')

