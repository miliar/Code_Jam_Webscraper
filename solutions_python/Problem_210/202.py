from math import pi
from numpy import *

def DEBUG(*args):
    pass
    # print args                  # 

def calc(slices):
    ini = slices[0][-1]
    cur = ini
    n = 0
    for s in slices:
        if s[-1] != cur:
            cur = s[-1]
            n += 1
    if ini != cur:
        n += 1

    return n

def free_slices(slices):
    prev = slices[0][-1]
    iniprev = prev
    r = []
    if 0 < slices[0][0]:
        beg = 0
        for s in slices:
            cur = s[-1]
            if beg < s[0]:
                r.append([beg, s[0], prev+cur])
            beg = s[1]
            prev = cur
    else:
        beg = slices[0][1]
        for s in slices[1:]:
            cur = s[-1]
            if beg < s[0]:
                r.append([beg, s[0], prev+cur])
            beg = s[1]
            prev = cur
    if beg < 1440:
        r.append([beg, 1440, prev+iniprev])
    r[-1][-1] = prev+iniprev
    r[0][-1] = prev + iniprev
    return r

def sum_(slices, k):
    res = 0
    for s in slices:
        if k == s[-1]:
            res += s[1]-s[0]
    return res

def dur(sl):
    return sl[1]-sl[0]

def invert(s):
    c = s[-1]
    if c == 'c':
        return s[:2]+['j']
    elif c == 'j':
        return s[:2]+['c']
    elif c == 'jj':
        return s[:2]+['cc']
    elif c == 'cc':
        return s[:2]+['jj']
    elif c == 'cj':
        return s[:2]+['jc']
    elif c == 'jc':
        return s[:2]+['cj']
    else:
        raise RuntimeError('invert:: Unknown: %s' % s)

def solve_(slices, frees):
    t_a = 1440
    t_c = sum_(slices, 'c')
    t_j = sum_(slices, 'j')
    tf_c = sum_(frees, 'cc')
    tf_j = sum_(frees, 'jj')
    t_bet = t_a - (t_c + t_j + tf_c + tf_j)
    if t_c + tf_c < t_j + tf_j: # make C larger
        DEBUG("INVERT")
        return solve_(map(invert, slices), map(invert, frees))
    DEBUG('TIMES:', t_c, tf_c, t_j, tf_j, t_bet)
    if (t_j + tf_j + t_bet) >= 720:
        DEBUG("OK!!")
        return calc(slices)
    r = 720 - (t_j + tf_j + t_bet)
    # frees_cc = [s in frees if s[-1] == 'cc']
    frees_cc = []
    fl = 0
    t_0 = 0
    for s in frees:
        if s[-1] == 'cc':
            if s[0] == 0:
                fl+=1
                t_0 = dur(s)
            if s[1] == 1440: fl+=1
            frees_cc.append(s)
    if fl == 2:
        DEBUG('FL')
        frees_cc = []
        for s in frees:
            if s[-1] == 'cc':
                if s[0] == 0:
                    DEBUG('skip', s)
                if s[1] == 1440:
                    DEBUG('filled to', s)
                    frees_cc.append([s[0], s[1]+t_0, s[2]])
                else:
                    frees_cc.append(s)
    frees_cc = sorted(frees_cc, key = dur, reverse=True)
    c = calc(slices)
    for f in frees_cc:
        DEBUG('use', f)
        r -= dur(f)
        c += 2
        if r <= 0:
            break
    return c

def solve(Ac, Aj, Sc, Sj):
    slices = sorted(Sc + Sj)
    if not slices:
        return 2
    frees = free_slices(slices)
    DEBUG(slices)
    DEBUG(frees)

    return solve_(slices, frees)

def main():
    T = input()

    for i in range(T):
        Ac, Aj = map(int, raw_input().split())
        Sc = []
        Sj = []
        for j in range(Ac):
            Sc.append(map(int, raw_input().split())+ ['c'])
        for j in range(Aj):
            Sj.append(map(int, raw_input().split())+ ['j'])
        print 'Case #%d: %d' % ((i+1), solve(Ac, Aj, Sc, Sj))

main()
