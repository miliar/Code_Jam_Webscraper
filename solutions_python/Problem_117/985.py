from sys import stdin as st

t = int(st.readline())

def check(y, x, n, m, desk):
    c = desk[y][x]        
    
    vr = True 
    for i in xrange(m):
        if desk[y][i] > c:
            vr = False
            break

    hr = True
    for i in xrange(n):
        if desk[i][x] > c:
            hr = False
            break

    return vr | hr

for case in xrange(1, t + 1):

    n, m = [ int(x) for x in st.readline().split() ]

    desk = []
    for j in xrange(n):
        desk.append([ int(x) for x in st.readline().split() ])

    r = True
    for y in xrange(n):
        for x in xrange(m):
            r &= check(y, x, n, m, desk)

    s = "YES" if r else "NO"

    print "Case #%d: %s" % (case, s)
