#!/usr/bin/env python
import sys

sentences = [
    ('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand'),
    ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities'),
    ('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up'),
]

alpha = 'abcdefghijklmnopqrstuvwxyz '
alpha_set = set(alpha)
mapping = {}

def do_map():
    # init map
    for a in alpha:
        mapping[a] = '?'
    mapping['a'] = 'y'
    mapping['e'] = 'o'
    mapping['q'] = 'z'
    mapping['z'] = 'q'
    inset = set()
    outset = set()
    
    # do map
    for s in sentences:
        inwords = s[0]
        outwords = s[1]
        for index in range(len(inwords)):
            i = inwords[index]
            o = outwords[index]
            inset.add(i)
            outset.add(o)
            if mapping[i] == '?':
                mapping[i] = o
            else:
                if mapping[i] != o:
                    print 'different mapping %s -> %s, was %s' % (i, o, mapping[i])
    #map_dbg(inset, outset)

def map_dbg(inset, outset):
    # missing?
    missing = alpha_set.difference(inset)
    if missing:
        print 'in is missing %s' % missing
    missing = alpha_set.difference(outset)
    if missing:
        print 'out is missing %s' % missing
    # print results
    for a in alpha:
        print '%s -> %s' % (a, mapping[a])

def translate(fname):
    with open(fname) as f:
        count = int(f.readline().strip())
        tc = 1
        for l in f.readlines():
            l = l.strip()
            if not l:
                continue
            o = ''
            for c in l:
                o += mapping[c]
            print 'Case #%d: %s' % (tc, o)
            tc += 1
    
def main():
    do_map()
    if len(sys.argv) > 1:
        for a in sys.argv[1:]:
            translate(a)


if __name__ == '__main__':
    main()
    