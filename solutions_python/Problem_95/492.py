#!/usr/bin/env python

import sys

def main () :
    mapping = {}
    mapping['y'] = 'a'
    mapping['e'] = 'o'
    mapping['q'] = 'z'

    inp = 'ejp mysljylc kd kxveddknmc re jsicpdrysi ' \
          'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd ' \
          'de kr kd eoya kw aej tysr re ujdr lkgc jv'

    out = 'our language is impossible to understand ' \
          'there are twenty six factorial possibilities ' \
          'so it is okay if you want to just give up'

    for i in range(len(inp)) :
        mapping[inp[i]] = out[i]

    # figured out this last one manually by inspecting mapping
    mapping['z'] = 'q'
    
    f = open(sys.argv[1])

    ncases = int(f.readline())
    for icase in range(ncases) :
        inp = f.readline().strip('\n')
        out = ''
        for i in range(len(inp)) :
            out += mapping[inp[i]]

        print 'Case #%i:'%(icase+1),
        print out
            
    f.close()
    
main()
