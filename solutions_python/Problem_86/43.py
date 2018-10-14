from sys import stdin
T = int(stdin.readline())
for t in xrange(T):
    line = stdin.readline().split()
    N = int(line[0])
    L = int(line[1])
    H = int(line[2])
    line2 = stdin.readline().split()
    for i in xrange(L, H+1):
        j = 0
        found = 1
        while j < N:
            x = int(line2[j])
            rem1 = x%i
            rem2 = i%x
            if rem1 != 0 and rem2 != 0:
                found = 0
            j = j + 1
        if found == 1:
            best = i
            break
    if (found):
        print 'Case #%d: %s' % (t+1, str(best))
    else:
        print 'Case #%d: NO' % (t+1)
