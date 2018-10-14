import fractions

if __name__ == '__main__':
    fin = 'B-large.in'
    fon = 'B-large.out'
    
    fi = open(fin, 'r')
    fo = open(fon, 'w')
    
    c = int(fi.readline())
    for i in xrange(c):
        ts = [int(x) for x in fi.readline().split(' ')][1:]
        m = min(ts)
        tns = [x - m for x in ts]
        unit = reduce(lambda x,y: fractions.gcd(x,y), tns)
        r = m % unit
        ans = unit - r if r else 0 
        fo.write("Case #%d: %d\n" % (i + 1, ans))
    
    print "Done!"
    fi.close()
    fo.close()

