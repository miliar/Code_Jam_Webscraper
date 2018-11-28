def solve():
    c,f,x = map(float, raw_input().split())
    cps = 2.0
    res = x/cps
    elapsed = 0.0
    while True:
        new = c/cps+x/(cps+f)
        if new + elapsed < res:
            res = elapsed + new
        else:
            break
        elapsed += c/cps
        cps += f

    return res

def main():
    T = int(raw_input())
    for t in xrange(1, T+1):
        ret = solve()
        print 'Case #%d: %.7f' % (t, ret)
if __name__ == '__main__':
    main()
