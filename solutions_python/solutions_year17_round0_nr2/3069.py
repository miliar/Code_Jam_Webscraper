t = int(raw_input())

for i in xrange(1, t+1):
    n = int(raw_input())
    l = []
    for c in str(n):
        l.append(int(c))

    for j in xrange(len(l) - 1, 0, -1):
        #print l[j], j
        if (l[j] < l[j-1]):
            l[j-1] -= 1
            for k in xrange(j, len(l)):
                l[k] = 9

    r = 0
    for el in l:
        r = r*10
        r = r + el

    print('Case #{0}: {1}'.format(i, r))
