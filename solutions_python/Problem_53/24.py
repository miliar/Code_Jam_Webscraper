
if __name__ == '__main__':
    fin = 'A-small.in'
    fon = 'A-small.out'
    
    fi = open(fin, 'r')
    fo = open(fon, 'w')
    
    c = int(fi.readline())
    for i in xrange(c):
        n, k = [int(x) for x in fi.readline().split(' ')]
        ans = (k % 2 ** n) == 2 ** n - 1
        fo.write("Case #%d: %s\n" % (i + 1, 'ON' if ans else 'OFF'))
    
    print "Done!"
    fi.close()
    fo.close()

