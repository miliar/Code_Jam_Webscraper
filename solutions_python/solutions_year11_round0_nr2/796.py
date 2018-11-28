#! /usr/bin/env python2

import sys

def remove_one(res, forb, dic):
    c = res.pop()
    if c not in dic:
        return
    for x in dic[c]:
        forb.remove(x)

def solve(s, c, d):
    dic = {}
    for opp in d:
        a, b = opp[0], opp[1]
        if a not in dic:
            dic[a] = []
        if b not in dic:
            dic[b] = []
        dic[a].append(b)
        dic[b].append(a)

    res = []
    forbidden = []
    for ch in s:
        res.append(ch)
        tr = None
        if len(res) >= 2:
            last = set(res[-2:])
            for trans in c:
                match = set(trans[:2])
                if last == match:
                    tr = trans[-1]
                    res.pop()
                    remove_one(res, forbidden, dic)
                    res.append(tr)
                    break
        if tr is not None:
            ch = tr
        if ch in forbidden:
            res = []
            forbidden = []
        elif ch in dic:
            forbidden.extend(dic[ch])

    s = '[%s]' % ', '.join(res)
    return s

if __name__ == '__main__':
    T = input()
    for t in xrange(T):
        print >>sys.stderr, 'Case #%d started' % (t + 1)
        fields = raw_input().split()
        C = int(fields[0])
        all_c = fields[1:C+1]
        D = int(fields[C+1])
        all_d = fields[C+2:C+2+D]
        s = fields[-1]
        print 'Case #%d: %s' % (t + 1, solve(s, all_c, all_d))
