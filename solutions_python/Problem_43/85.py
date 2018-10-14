#! /usr/bin/env python

def comp(s):
    dic = {}
    min_base = max(2, len(set(s)))
    nums = [1, 0] + range(2, min_base)
    def rep(c):
        if c in dic:
            return dic[c]
        dic[c] = nums.pop(0)
        return dic[c]
    ds = map(rep, s)
    return tob(ds, min_base)

def tob(ds, base):
    return reduce(lambda acc, d: acc * base + d, ds, 0)

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t+1):
        print 'Case #%d:' % i,
        s = raw_input()
        print comp(s)
