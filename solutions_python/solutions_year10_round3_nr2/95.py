def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return f(n/2) + 1
    else:
        return f((n-1)/2) + 1

def printAns(filename):
    fin = open('B-%s.in' % filename, 'r')
    fout = open('B-%s.out' % filename, 'w')
    t = int(fin.readline().strip())
    for i in xrange(1, t + 1):
        l, p, c = map(int, fin.readline().strip().split(' '))
        j = 1
        while l * pow(c, j) < p:
            j += 1
        j -= 1
        fout.write("Case #%d: %d\n" % (i, f(j)))
    fin.close()
    fout.close()

printAns('large')

