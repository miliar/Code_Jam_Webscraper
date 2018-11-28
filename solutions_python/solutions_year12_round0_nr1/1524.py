#!/usr/bin/env python
# encoding: utf-8
"""
A.py

Created by Graham Dennis on 2012-04-14.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys

source = """y qee
a zoo
ejp mysljylc kd kxveddknmc re jsicpdrysi
our language is impossible to understand
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
there are twenty six factorial possibilities
de kr kd eoya kw aej tysr re ujdr lkgc jv
so it is okay if you want to just give up
"""

def deduce_mapping(mapping):
    lines = source.splitlines()
    for google, english in zip(lines[::2], lines[1::2]):
        for g, e in zip(google, english):
            if not g in mapping:
                mapping[g] = e
            else:
                assert mapping[g] == e
    # print len(mapping), mapping
    assert len(mapping) >= 26
    alphabet = set([chr(ord('a') + offset) for offset in xrange(26)])
    if len(mapping) == 26:
        for character in alphabet:
            if not character in mapping:
                missing_value = list(alphabet.difference(mapping.values()))
                assert len(missing_value) == 1
                mapping[character] = list(missing_value)[0]

def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    
    mapping = {}
    
    deduce_mapping(mapping)
    
    for t in xrange(T):
        line = f.readline().strip()
        new_line = ''.join(mapping[c] for c in line)
        
        print "Case #%i: %s" % (t+1, new_line)

if __name__ == "__main__":
    sys.exit(main())
