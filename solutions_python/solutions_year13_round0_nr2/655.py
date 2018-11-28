def main():
    t = int(raw_input())
    for _t in xrange(t):
        n, m = map(int, raw_input().split())
        a = [[0 for i in xrange(m)] for i in xrange(n)]
        
        for i in xrange(n):
            a[i] = map(int, raw_input().split())
        b = [[a[i][j] for i in xrange(n)] for j in xrange(m)]
        #print a, b

        amax = [max(k) for k in a]
        bmax = [max(k) for k in b]
        #print amax, bmax
        
        ans = True
        for i in xrange(n):
            for j in xrange(m):
                if a[i][j] == 1:
                    if amax[i] == 2 and bmax[j] == 2:
                        ans = False
                if ans == False: break
            if ans == False: break
        
        print "Case #%d:" %(_t + 1),
        print ("YES" if ans else "NO")

if __name__ == "__main__":
    main()
