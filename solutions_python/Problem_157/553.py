#!/usr/bin/env python
# encoding: utf-8

from contextlib import nested

#debug = True
debug = False


def compute(c1, c2):
    if c1 is None:
        return c2
    if c2 is None:
        return c1
    neg = 0
    if c1.startswith('-'):
        neg += 1
        c1 = c1[1:]
    if c2.startswith('-'):
        neg += 1
        c2 = c2[1:]
    table = {'1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
             'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'},
             'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
             'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'}}
    ret = table[c1][c2]
    if ret.startswith('-'):
        neg += 1
        ret = ret[1:]
    if neg % 2 == 1:
        ret = '-' + ret
    return ret


def compute_str(s, r=None):
    for c in s:
        r = compute(r, c)
    return r


def solve(s, x):
    ss = s * x
    i_pos = find('i', ss)
    if i_pos is None:
        return False
    k_pos = rfind('k', ss)
    if k_pos is None:
        return False
    if debug:
        print i_pos, k_pos
        print '%s-%s-%s' % (ss[:i_pos+1], ss[i_pos+1:k_pos], ss[k_pos:])
    r = None
    for c in ss[i_pos+1:k_pos]:
        r = compute(r, c)
    if r == 'j':
        return True
    else:
        return False


def solve_large(s, x):
    prod = compute_str(s)
    mul_prod = prod
    cnt = 1
    while mul_prod != '1':
        mul_prod = compute(mul_prod, prod)
        cnt += 1
    if debug:
        print 's:', s, ' x:', x, ' cnt:', cnt

    ss = None
    ss = s * min(x, cnt)
    i_pos = find('i', ss)
    if i_pos is None:
        return False
    k_pos = rfind('k', ss)
    if k_pos is None:
        return False
    if x < cnt and k_pos <= i_pos:
        return False
    if debug:
        print 'i_pos:', i_pos, ' k_pos:', k_pos
        print ss
        print '%s-%s-%s' % (ss[:i_pos+1], ss[i_pos+1:k_pos], ss[k_pos:])
    i_cnt = i_pos / len(s) + 1
    i_pos_in_s = i_pos % len(s)
    #if i_pos_in_s != len(s) - 1:
        #i_cnt += 1
    if debug:
        print 'i_cnt:', i_cnt, ' i_pos_in_s:', i_pos_in_s
    prefix = s[i_pos_in_s+1:]
    k_cnt = (len(ss) - k_pos) / len(s)
    k_pos_in_s = k_pos % len(s)
    if k_pos_in_s != 0:
        k_cnt += 1
    if debug:
        print 'k_cnt:', k_cnt, ' k_pos_in_s:', k_pos_in_s
    suffix = s[:k_pos_in_s]
    if debug:
        print 'prefix:', prefix
        print 'suffix:', suffix

    pr = compute_str(prefix)
    sr = compute_str(suffix)

    real_x = x - i_cnt - k_cnt
    if debug:
        print 'real_x:', real_x, ' real_x % cnt: ', real_x % cnt
    real_x %= cnt
    r = pr
    for i in range(real_x):
        r = compute(r, prod)
    r = compute(r, sr)
    if r == 'j':
        return True
    else:
        return False


def find(c, s, end_pos=-1):
    r = None
    for idx, i in enumerate(s):
        r = compute(r, i)
        #print idx, end_pos, i, r, c
        if idx > end_pos and r == c:
            return idx
    return None


def rfind(c, s, end_pos=None):
    if end_pos is None:
        end_pos = len(s)
    r = None
    for idx, i in enumerate(reversed(s)):
        r = compute(i, r)
        real_idx = len(s) - idx - 1
        if real_idx < end_pos and r == c:
            return real_idx
    return None

if __name__ == '__main__':
    #finame = 'C-small-attempt0.in'
    #foname = 'C-small-attempt0.out'
    finame = 'C-large.in'
    foname = 'C-large.out'
    if debug:
        finame = 'C-small.in'
        foname = 'C-small.out'
    with nested(open(finame),
                open(foname, 'w')) as (fi, fo):
        num_case = int(fi.readline().strip())
        for i in range(1, num_case + 1):
            print '=== Case: %d ===' % i
            l, x = map(int, fi.readline().strip().split(' '))
            s = fi.readline().strip()
            #ret = 'YES' if solve(s, x) else 'NO'
            ret = 'YES' if solve_large(s, x) else 'NO'
            print 'Case #%d: %s' % (i, ret)
            fo.write('Case #%d: %s\n' % (i, ret))
