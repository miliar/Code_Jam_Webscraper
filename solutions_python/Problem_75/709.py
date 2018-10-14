#!/usr/bin/env python
"""
magicka.py: Magicka is an action-adventure game developed by Arrowhead
Game Studios. In Magicka you play a wizard, invoking and combining
elements to create Magicks. This problem has a similar idea, but it
does not assume that you have played Magicka.

Google Code Jam
Qualification Round 2011
Problem B: Magicka


Author: Kelsey Jordahl <kajord@gmail.com>
Time-stamp: <Sat May  7 15:22:57 EDT 2011>

"""

import sys
#from numpy import array

verbose = True
debug = False

def invoke(l):
    """
    Set up a test case and invoke given elements
    """
    elist = []                          # start with empty element list
    # parse combine list
    C = int(l[0])
    l.pop(0)
    combinelist = l[:C]
    l = l[C:]
    # parse opposed list
    D = int(l[0])
    l.pop(0)
    opposelist = l[:D]
    l = l[D:]
    # get the starting base element list
    N = int(l[0])
    b = list(l[1])
    if len(b) != N:
        print 'Base element list size does not match expected!'
    if verbose:
        print 'Combines: %s' % combinelist
        print 'Opposed: %s' % opposelist
        print 'Initial base list: %s' % b
    while b:
        elist = elist + [b[0]]
        b.pop(0)
        if len(elist) > 1:
            if C:                       # check for elements to combine
                for combine in combinelist:
                    if combine[:2] == elist[-2] + elist[-1] or combine[:2] == elist[-1] + elist[-2]:
                        if debug:
                            print 'Combine match'
                        elist = elist[:-2] + [combine[-1]]
                        if len(elist)<2:
                            break
            if D:                       # check for opposed elements
                for oppose in opposelist:
                    if oppose[0] in elist and oppose[1] in elist:
                        if debug:
                            print 'Oppose match - clearing list'
                        elist = []
                        break
    s = str(elist)
    return s.replace("'","")                   # remove single quotes
    
def main():
    if len(sys.argv) < 2:
        infile = 'matest.in'
    else:
        infile = sys.argv[1]
    if len(sys.argv) < 3:
        outfile = infile + '.out'
    else:
        outfile = sys.argv[2]
    if verbose:
        print 'infile %s, outfile %s' % (infile, outfile)
    f = open(infile)
    o = open(outfile,'w')
    T = int(f.readline())
    print 'T = %d' % T
    for i in range(0,T):
        print 'Case #%d' % (i+1)
        o.write('Case #%d: %s\n' % (i+1, invoke(f.readline().split())))
    f.close
    o.close

if __name__ == '__main__':
    main()
