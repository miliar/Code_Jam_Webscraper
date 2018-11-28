def lastTidy(a):
    n = len(a)
    for i in xrange(n-1,0,-1):
        if a[i-1] > a[i]:
            a[i-1] -= 1
            for j in xrange(i,n): a[j] = 9
    result = 0
    for i in xrange(n):
        result *= 10
        result += a[i]
    return result

if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(1, t+1):
        a = map(int, list(raw_input().strip()))
        print "Case #%d: %d" % (i, lastTidy(a))
