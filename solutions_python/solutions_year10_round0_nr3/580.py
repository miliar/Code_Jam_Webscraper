#!/usr/bin/python

T = int(raw_input(""))
output = []
for t in xrange(T):
    R, k, N = map(int, raw_input("").split())
    g = list(map(int, raw_input("").split()))
    euro = 0
    gone = []
    group = g[:]
    for run in xrange(R):
        space_left = k
        group = group[:] + gone[:]
        gone = []
        while group and space_left >= group[0]:
            euro += group[0]
            space_left -= group[0]
            gone.append(group[0])
            group.remove(group[0])        
    output.append("Case #%d: %d" % (t+1, euro))

for k in output:
    print k
