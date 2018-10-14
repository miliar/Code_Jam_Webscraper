#!/usr/bin/env python

from sys import stdin

def areOposites(s, o, i):
    idx = 0
    while idx >= 0:
        try:
            idx = o.index(i, idx)
            op = ''
            if idx % 2 == 0:
                op = o[idx+1]
            else:
                op = o[idx-1]
            if op in s:
                return True
        except:
            return False
        idx += 1

def areCombined(s, c, r, i):
    idx = 0
    ch = s[-1]
    while idx >= 0:
        try:
            idx = c.index(i, idx)
            #print 'idx:', idx, c
            res = idx
            i = idx + 1
            if idx % 2 != 0:
                res -= 1
                i -= 2
            if c[i] == ch:
                ch = r[res/2]
                #print 's:', ch
                s[-1] = ch
                return True
        except:
            return False
        idx += 1

def solve():
    l = stdin.readline().split(' ')
    idx = 0
    combs = []
    res = []
    ops = []
    elems = l[len(l)-1][:-1]
    c = int(l[idx])
    for i in xrange(c):
        idx += 1
        cmb = l[idx]
        if cmb[0] in elems and cmb[1] in elems:
            combs += [cmb[0], cmb[1]]
            res += cmb[2]
    idx += 1
    d = int(l[idx])
    for i in xrange(d):
        idx += 1
        o = l[idx]
        if o[0] in elems and o[1] in elems:
            ops += [o[0], o[1]]
    idx += 1
    #n = int(l[idx])
    if len(combs) == 0 and len(ops) == 0:
        return list(elems)
    solution = []
    for i in elems:
        #print solution, i, 'here'
        if solution == []:
            solution += i
        elif i in combs and solution[-1] in combs and areCombined(solution, combs, res, i):
            pass
        elif i in ops and areOposites(solution, ops, i):
            solution = []
        else:
            solution += i
    return solution

def parse(solution):
    sol = '['
    for i in solution:
        sol += i + ', '
    if sol != '[':
        sol = sol[:-2]
    return sol + ']'

if __name__ == '__main__':
    T = int(stdin.readline())
    for i in xrange(T):
        print 'Case #' + str(i+1) + ':', parse(solve())
