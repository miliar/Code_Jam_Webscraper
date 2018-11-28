def show_float(x):
    print "%.9f" % x

def equal(a, b):
    return abs(a - b) < 1e-12

def solve():
    (n, v, x) = raw_input().split()
    n = int(n)
    v = float(v)
    x = float(x)
    
    temp = []
    r = []
    
    for i in xrange(n):
        (rr, cc) = map(float, raw_input().split())
        r.append(rr)
        temp.append(cc)
        
    if n == 1:
        if equal(x, temp[0]):
            show_float(v / r[0])
        else:
            print 'IMPOSSIBLE'
        return
    elif n == 2:
        if equal(temp[1], temp[0]):
            if equal(temp[1], x):
                show_float(min(v / r[0], v / r[1]))
            else:
                print 'IMPOSSIBLE'
            return
        if equal(temp[0], x) and not equal(temp[1], x):
            show_float(v / r[0])
            return
        if equal(temp[1], x) and not equal(temp[0], x):
            show_float(v / r[1])
            return
        if temp[0] > x and temp[1] > x:
            print 'IMPOSSIBLE'
            return
        if temp[0] < x and temp[1] < x:
            print 'IMPOSSIBLE'
            return

        v1 = (x * v - v * temp[0]) / (temp[1] - temp[0])
        v0 = (x * v - v * temp[1]) / (temp[0] - temp[1])
    

        show_float(max(v1 / r[1], v0 / r[0]))
        


T = int(raw_input())
for cas in xrange(T):
    print 'Case #%d:' % (cas + 1),
    solve()
