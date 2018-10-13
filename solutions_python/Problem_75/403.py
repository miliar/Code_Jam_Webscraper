#!/usr/bin/python

def solve():
    
    combinations = {}
    opposed = {}
    
    
    l = raw_input().split(' ')
    c = int(l.pop(0))
    for i in range(c):
        c1, c2, r = l.pop(0)
        combinations[tuple(sorted((c1, c2)))] = r
    
    d = int(l.pop(0))
    for i in range(d):
        d1, d2 = l.pop(0)
        if d1 in opposed:
            opposed[d1].add(d2)
        else:
            opposed[d1] = set([d2])
        if d2 in opposed:
            opposed[d2].add(d1)
        else:
            opposed[d2] = set([d1])
    
    n = int(l.pop(0))
    s = list(l.pop(0))
    empty_set = set()
    result = ['#', ]
    for char in s:
        result.append(char)
        combine = combinations.get(tuple(sorted(result[-2:])), None)
        if combine:
            result = result[:-2]
            result.append(combine)
        elif opposed.get(char, empty_set).intersection(result):
            result = ['#', ]
    
    return str(result[1:]).replace("'", "")     

if __name__ == '__main__':
    T = int(raw_input())
    for c in range(1, T+1):
        print "Case #{0}: {1}".format(c, solve())
