











def main():
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        X = map(int,raw_input().split())
        Y = map(int,raw_input().split())
        
        X.sort()
        Y.sort()
        
        r = 0
        
        for i in xrange(N):
            r += X[i] * Y[-i-1]
        
        print 'Case #%d: %d' % (t+1, r)
        
        
if __name__ == '__main__':
    main()
    