def printAns(filename):
    fin = open('001%s.in' % filename, 'r').read().split('\n')[:-1]
    fout = open('001%s.out' % filename, 'w')
    j = int(fin[0])
    for i in xrange(1, j+1):
        temp = map(int, fin[i].split(' '))
        n, k = temp
        # if k mod 2^n is 2^n - 1
        k = k % pow(2, n) - pow(2, n) + 1
        if k == 0:
            fout.write("Case #%d: ON\n" % i)
        else:
            fout.write("Case #%d: OFF\n" % i)
    fout.close()
    
printAns('large')
