from heapq_max import *
input = open('input3.txt', 'r')
t = int(input.readline())
for i in range(t):
    l = {}
    c = 0
    n, k = map(int, input.readline().split())
    l[n] = 1
    for j in range(k):
        d = max(l.keys())
        l[d] -= 1
        if l[d] == 0:
            l.pop(d)
        if d % 2 == 1:
            ls = d / 2
            rs = d / 2
        else:
            ls = d / 2
            rs = d / 2 - 1
        if not l.has_key(ls):
            l[ls] = 1
        else:
            l[ls] += 1
        if not l.has_key(rs):
            l[rs] = 1
        else:
            l[rs] += 1

    print "Case #" + str(i+1) + ": " + str(ls) + ' ' + str(rs)
