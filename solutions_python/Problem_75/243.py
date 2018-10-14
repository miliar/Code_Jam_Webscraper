#!/usr/bin/python
# -*- coding: utf-8 -*-

import re,os
import sys

###### Variable&constants definition
All = set( [ chr(c) for c in range(ord('A'), ord('Z')+1)] )
Base = set(['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'])
Other = All - Base

if "DEBUG" in os.environ:
    DEBUG = True
else:
    DEBUG = False

def parse_file(fn):
    return parse_input(open(fn, 'r').read())
    
def parse_input(s):
    ln = re.split(r'\r|\n|\r\n', s)
    T = int( ln.pop(0) )

    cases = []

    for t in range(0, T):
        # A dict of 'opposed' pairs of elements
        # ex. If F and R are opposed, opp[F] == R and opp[R] == F.
        opp = {}
    
        # A dict of pairs to 'combine'.
        # ex. If Q and F combine to form T, Comb[(Q,F)] = T, Comb[(F,Q)] = T.
        comb = {}
    
        seq = re.split(r'\s+', ln[t])
        C = int( seq.pop(0) )
        
        for c in range(0, C):
            cb = list(seq.pop(0))
            comb[ (cb[0], cb[1]) ] = cb[2]
            comb[ (cb[1], cb[0]) ] = cb[2]

        D = int( seq.pop(0) )
        for d in range(0, D):
            op = list(seq.pop(0))
            opp[op[0]] = op[1]
            opp[op[1]] = op[0]

        N = int( seq.pop(0) )
        chars = seq.pop(0)

        if not len(chars) == N:
            raise

        cases.append( (list(chars), comb, opp) )

    return cases

def print_list(ls):
    print "\t[%s]" % ', '.join(elem_list)


if __name__ == '__main__':
    cases = None
    
    if len(sys.argv) > 1:
        cases = parse_file(sys.argv[1])
    else:
        cases = parse_input(sys.stdin.read())

    for t in range(0, len(cases)):
        chars = cases[t][0]
        comb  = cases[t][1]
        opp   = cases[t][2]
        
        elem_set = set()
        elem_list = []
        
        for c in chars:
            if DEBUG: print "Character: %s" % c
            
            if len(elem_list) == 0:
                elem_list.append(c)
                elem_set.add(c)
                if DEBUG:
                    print "list is empty"
                    print_list(elem_list)
                    print
                continue
                    
            if (elem_list[-1], c) in comb:
                new = comb[(elem_list[-1], c)]
                if DEBUG:
                    print "%s and %s combines to form %s" % (elem_list[-1], c, new)
                elem_list.pop()
                elem_list.append(new)
                elem_set = set(elem_list)

                if DEBUG:
                    print_list(elem_list)
                    print
                continue
                
            if c in opp and opp[c] in elem_set:
                elem_list[:] = []
                elem_set.clear()

                if DEBUG:
                    print "Found an opposed pair: (%s,%s)" % (c, opp[c])
                    print_list(elem_list)
                    print
                continue
                    

            elem_list.append(c)
            elem_set.add(c)
            if DEBUG:
                print "Nothing to special. Pushing %s" % c
                print_list(elem_list)
                print

        print "Case #%d: [%s]" % (t+1, ', '.join(elem_list))
            
 
