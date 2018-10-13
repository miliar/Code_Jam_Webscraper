#!/usr/bin/python
import sys

from collections import defaultdict

T = int(sys.stdin.readline())
base = set(['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'])
for test_case in range(T):
    args = sys.stdin.readline().strip().split()
    num_comb = int(args[0])
    comb = {}
    for i in range(1, num_comb+1):
        assert args[i][0] in base
        assert args[i][1] in base
        assert args[i][2] not in base
        comb[args[i][:2]] = args[i][2]
        comb[args[i][1]+args[i][0]] = args[i][2]

    num_opp = int(args[num_comb+1])
    opp = defaultdict(set)
    for i in range(num_comb+2,num_comb+2+num_opp):
        assert args[i][0] in base
        assert args[i][1] in base

        opp[args[i][0]].add(args[i][1])
        opp[args[i][1]].add(args[i][0])

    N = args[num_comb+2+num_opp]
    elements = args[num_comb+2+num_opp+1]

    if False:
        print
        print "Case #%d:" % (test_case+1)
        print comb
        print opp
        print elements

    l = []
    for e in elements:
        if len(l) == 0:
            l = [e]
        else:
            c = l[-1] + e
            if c in comb:
                l[-1] = comb[c]
            elif opp[e].intersection(set(l)):
                l = []
            else:
                l.append(e)
    
    print "Case #%d: [%s]" % (test_case+1, ', '.join(l))
    

