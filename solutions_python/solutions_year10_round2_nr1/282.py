import sys
import re
from pprint import pprint


def diff(present,not_present):
    c = 0
    for x in not_present.keys():
        if x not in present.keys():
            c += 1
            c += diff({},not_present[x])
        else:
            c += diff(present[x], not_present[x])
    return c

input = sys.stdin
T=int(input.readline())
for i in xrange(1,T+1):
    N, M = map(int, input.readline().split())
    #print N,M
    present = {}
    not_present = {}
    for k in range(N):
        path = input.readline()
        path = re.sub('\n','', path)
        path = [x for x in path.split('/') if x != '']
        ps = present
        for p in path:
            if p not in ps:
                ps[p] = {}
            ps = ps[p]
    for k in range(M):
        path = input.readline()
        path = re.sub('\n','', path)
        path = [x for x in path.split('/') if x != '']
        ps = not_present
        for p in path:
            if p not in ps:
                ps[p] = {}
            ps = ps[p]

    c = diff(present, not_present)
    print "Case #%s: %s" % (i, c)
