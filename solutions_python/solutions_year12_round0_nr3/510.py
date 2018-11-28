import sys

f = sys.stdin
T = int(f.readline())

for i in range(T):
    a,b = map(lambda x: int(x), f.readline().split() )
    total = 0
    for j in range(a,b+1) :
        s = str(j)
        l = [ int(s[i2:] + s[:i2]) for i2 in range(len(s))]
        l = [i1 for i1 in l if i1 >= a and i1 <= b]
        m = min(l)
        n = len(set(l))
        if j == m :
            total += n * (n-1) / 2
#            print '....', j, n
    print 'Case #{}:'.format(i+1),total
