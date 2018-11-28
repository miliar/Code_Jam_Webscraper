
def read_ints():
    return map(int, raw_input().split(" "))

def test(p, D, t):
    pre = 0
    for i in range(len(p)):        
        if i == 0:
            pre = float(p[i]) - t
            continue
        apart = pre + D
        left = float(p[i]) - t
        right = float(p[i]) + t
        if apart <= left:
            pre = left
        elif apart <= right:
            pre = apart
        else:
            return False
    return True

def solve(p, D):
    if len(p) == 1:
        return 0.0
    mi = 0.0
    mx = float(len(p) - 1) / 2.0 * D
    mid = (mi + mx) / 2
    while mx - mi > 1e-6:
        mid = (mi + mx) / 2
        #print 'mx = %f, mi = %f, mid = %f' % (mx, mi, mid)
        flag = test(p, D, mid)
        #print flag
        if flag is True:
            mx = mid  
        else:
            mi = mid
    return mid

def main():
    T, = read_ints()
    for cas in xrange(T):
        C, D = read_ints()
        p = []
        for i in range(C):
            pi, vi = read_ints()
            p += [pi] * vi
        p.sort() 
        #print p
        ans = solve(p, D)
        print "Case #%d: %f" % (cas+1, ans)

if __name__ == '__main__':
    main()
