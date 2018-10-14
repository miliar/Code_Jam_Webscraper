import sys
import psyco

psyco.full()

def main(ifile):
    N = int(ifile.readline())
    for i in range(N):
        foo(i+1, ifile)

def foo(idx, ifile):
    s = ifile.readline().strip()
    k = 'welcome to code jam'
    m = len(s)
    n = len(k)
    a = [[0]*(n+2) for i in range(m+2)]
    for i in range(m):
        a[i][0] = 1

    for i in range(m):
        for j in range(n):
            if s[i] == k[j]:
                a[i+1][j+1] += a[i][j]
                a[i+1][j+1] %= 10000
            a[i+2][j+1] += a[i+1][j+1]

    res = 0
    for i in range(m+1):
        res += a[i][n]
    res %= 10000

    print 'Case #%d: %04d' % (idx, a[m][n])


    






main(sys.stdin)
