#!/usr/bin/python

import re

def read_tree():
    r = {}
    while True:
        s = raw_input()
        if re.search('[0-9\.]+', s):
            break

    r['v'] = float(re.search('[0-9\.]+', s).group())
    if re.search('[a-z]', s):
        r['f'] = re.search('[a-z]+', s).group()
        r[1] = read_tree()
        r[0] = read_tree()
    return r

def cute(p, tree, feat):
    r = p * tree['v']
    if tree.has_key('f'):
        if tree['f'] in feat:
            return cute(r, tree[1], feat)
        else:
            return cute(r, tree[0], feat)
    return r
    
if __name__ == '__main__':
    N = int(raw_input())
    for n in xrange(1, N + 1):
        L = int(raw_input())
        tree = read_tree()
        while True:
            try:
                A = int(raw_input())
            except:
                A = 0
            if A:
                break
            
        print "Case #%d:" % n
        for a in xrange(1, A + 1):
            feat = raw_input().split()[2:]
            print "%.7f" % cute(1.0, tree, feat)

