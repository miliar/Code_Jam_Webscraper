import sys
D = {}
# M = 3000
M = 2000001
for i in xrange(M):
    if i % 1000 == 0:
        # print i
        pass
    s = str(i)
    D[i] = set()
    for x in range(1, len(s)):
        if s[x] == '0':
            continue
        p = int(s[x:] + s[:x])
        if p > i:
            D[i].add(p)

l = open('input3.txt')
l.readline()
for index, line in enumerate(l):
    A, B = map(int, line.split())
    c = 0
    for i in xrange(A, B):
        c += len([x for x in D[i] if x <= B])
    print "Case #%d: %d" % (index+1, c)
