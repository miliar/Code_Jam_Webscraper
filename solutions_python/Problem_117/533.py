def solveCase(a, n, m):
    a = [map(int, l.split()) for l in a]
    cmax = [0]*m
    rmax = [0]*n
    for i in xrange(n):
        for j in xrange(m):
            item = a[i][j]
            if item > cmax[j]:
                cmax[j] = item
            if item > rmax[i]:
                rmax[i] = item
    for i in xrange(n):
        for j in xrange(m):
            if a[i][j] < rmax[i] and a[i][j] < cmax[j]:
                return "NO"
    return "YES"

def main():
    import sys
    lines = open(sys.argv[1]).readlines()
    T = int(lines[0])
    current = 1
    for t in range(1, T+1):
        n, m = map(int, lines[current].split())
        current += 1
        print "Case #%d: %s" % (t, solveCase(lines[current:current+n], n, m))
        current += n
main()
    
