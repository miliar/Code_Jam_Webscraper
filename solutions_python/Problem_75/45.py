#!/usr/bin/python

import sys, re, string, math

def do_one_case(cnum):
    base = [ i for i in "QWERASDF" ]
    v = sys.stdin.readline().split()
    C = int(v[0])
    v1 = v[1:C+1]
    v[:C+1] = []
    D = int(v[0])
    v2 = v[1:D+1]
    v[:D+1] = []
    assert len(v)==2
    N = int(v[0])
    v3 = v[1]
    assert len(v1)==C
    assert len(v2)==D
    assert len(v3)==N
    comb = {}
    opp = dict([ (i, set()) for i in base])

    for s in v1:
        assert len(s)==3
        assert s[0] in base
        assert s[1] in base
        comb[(s[0],s[1])] = s[2]
        comb[(s[1],s[0])] = s[2]
    for s in v2:
        assert len(s)==2
        assert s[0] in base
        assert s[1] in base
        opp[s[0]].add(s[1])
        opp[s[1]].add(s[0])

    e = []
    o = set()
    ox = o
    for s in v3:
        if len(e)>=1 and (e[-1],s) in comb:
            e[-1] = comb[(e[-1],s)]
            o = ox
#        elif o & opp[s]:
        elif opp[s] & set(e):
            e = []
            o = set()
            ox = o
        else:
            e.append(s)
            ox = o
            o.add(s)

    ostr = ", ".join(e)
    print "Case #%d: [%s]" % (cnum, ostr)


def main():
    N = int(sys.stdin.readline().strip())
    for i in range(N):
        do_one_case(i+1)


if __name__ == "__main__":
    main()
