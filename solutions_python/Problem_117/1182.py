def solve(a):
    rowmax = map(max, a)
    colmax = map(max, zip(*a))
    for r, rm in zip(a, rowmax):
        for x, cm in zip(r, colmax):
            if x < min(rm, cm):
                return False
    return True

def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        N, M = (int(x) for x in raw_input().split())
        a = [list(int(x) for x in raw_input().split()) for x in xrange(N)] 
        if solve(a):
            r = "YES"
        else:
            r = "NO"
        print "Case #%d: %s" % (t, r)

if __name__ == '__main__':
    main()
