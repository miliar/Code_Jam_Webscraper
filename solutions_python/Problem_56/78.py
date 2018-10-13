
if __name__ == '__main__':
    fin = 'A-small.in'
    fon = 'A-small.out'
    
    fi = open(fin, 'r')
    fo = open(fon, 'w')
    
    c = int(fi.readline())
    for i in xrange(c):
        n, k = [int(x) for x in fi.readline().split(' ')]
        m = []
        print n
        for _ in xrange(n):
            line = fi.readline().strip()
            line = filter(lambda x: x != '.', line)
            line = '.'*(n - len(line)) + line
            print line
            m = m + [line]
        
        red = 0
        blue = 0
        
        for p in xrange(n):
            rc = 0
            bc = 0
            for q in xrange(n):
                if m[p][q] == 'R':
                    rc += 1
                else:
                    rc = 0
                if m[p][q] == 'B':
                    bc += 1
                else:
                    bc = 0
                    
                if rc >= k:
                    red = 1
                if bc >= k:
                    blue = 1
                    
        for q in xrange(n):
            rc = 0
            bc = 0
            for p in xrange(n):
                if m[p][q] == 'R':
                    rc += 1
                else:
                    rc = 0
                if m[p][q] == 'B':
                    bc += 1
                else:
                    bc = 0
                    
                if rc >= k:
                    red = 1
                if bc >= k:
                    blue = 1
        
        for p in xrange(n):
            q = 0
            rc = 0
            bc = 0
            while p < n and q < n:
                if m[p][q] == 'R':
                    rc += 1
                else:
                    rc = 0
                if m[p][q] == 'B':
                    bc += 1
                else:
                    bc = 0
                    
                if rc >= k:
                    red = 1
                if bc >= k:
                    blue = 1
                    
                p += 1; q += 1
                
                
        
        for q in xrange(n):
            p = 0
            rc = 0
            bc = 0
            while p < n and q < n:
                if m[p][q] == 'R':
                    rc += 1
                else:
                    rc = 0
                if m[p][q] == 'B':
                    bc += 1
                else:
                    bc = 0
                
                if rc >= k:
                    red = 1
                if bc >= k:
                    blue = 1
                    
                p += 1; q += 1
        
        for q in xrange(n):
            p = 0
            rc = 0
            bc = 0
            while p < n and q >= 0:
                if m[p][q] == 'R':
                    rc += 1
                else:
                    rc = 0
                if m[p][q] == 'B':
                    bc += 1
                else:
                    bc = 0
                
                if rc >= k:
                    red = 1
                if bc >= k:
                    blue = 1
                    
                p += 1; q -= 1
                
        for p in xrange(n):
            q = n-1
            rc = 0
            bc = 0
            while p < n and q >= 0:
                if m[p][q] == 'R':
                    rc += 1
                else:
                    rc = 0
                if m[p][q] == 'B':
                    bc += 1
                else:
                    bc = 0
                    
                if rc >= k:
                    red = 1
                if bc >= k:
                    blue = 1
                    
                p += 1; q -= 1
                
        fo.write("Case #%d: %s\n" % (i + 1, 'Both' if red + blue == 2 else 'Red' if red == 1 else 'Blue' if blue == 1 else 'Neither'))
    
    print "Done!"
    fi.close()
    fo.close()

