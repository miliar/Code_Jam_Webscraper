
if __name__ == '__main__':
    T = input()
    for tnum in range(1, T + 1):
        C, F, X = map(float, raw_input().strip().split())
        
        ans = X / 2.0
        
        time_for_farms = 0
        for farm in xrange(1, int(X/C) + 1):
            time_for_farms += C / ((farm - 1) * F + 2)
            t = time_for_farms + X / (farm * F + 2)
            if t < ans: ans = t
            
        print 'Case #%d: %.8f' % (tnum, ans)
