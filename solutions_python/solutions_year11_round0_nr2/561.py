import sys
import re

input = sys.stdin
T=int(input.readline())
for i in xrange(1,T+1):
    data = input.readline()
    data = data.split()
    C = int(data[0])
    cs = data[1:1+C]
    CS = {}
    for s in cs:
        CS["%s%s" % (s[0], s[1])] = s[2]
        CS["%s%s" % (s[1], s[0])] = s[2]
    D = int(data[1+C])
    ds = data[1+C+1:1+C+1+D]
    DS = {}
    for s in ds:
        DS[s[0]] = s[1]
        DS[s[1]] = s[0]
    N = int(data[1+C+1+D])
    ns = data[1+C+1+D+1:]

    S = ns[0] # one string
    res = []
    opposite = None
    pair = None
    for s in S:
        if len(res):
            k1 = "%s%s" % (res[-1], s)
            if k1 in CS:
                res[-1] = CS[k1]
                continue
        if s in DS:
            if DS[s] in res:
                # res = res[0:res.index(DS[s])]
                res = []
                continue
        res.append(s)

    # print data
    # print C, cs, CS
    # print D, ds, DS
    # print N, ns

    print re.sub("'", '', "Case #%s: %s" % (i, res))

