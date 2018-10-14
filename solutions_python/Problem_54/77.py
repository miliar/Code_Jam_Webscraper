def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a
    
def listGCD(ls):
    if len(ls) == 1:
        return ls[0]
    else:
        temp = ls[0]
        for i in ls[1:]:
            temp = gcd(temp, i)
            if temp == 1:
                return 1
        return temp
    
def printAns(filename):
    fin = open('002%s.in' % filename, 'r').read().split('\n')[:-1]
    fout = open('002%s.out' % filename, 'w')
    n = int(fin[0])
    for i in xrange(1, n+1):
        temp = map(int, fin[i].split(' '))
        times = sorted(set(temp[1:]))
        m = len(times)
        temp2 = []
        for j in xrange(m-1):
            for k in xrange(j+1, m):
                temp2.append(times[k] - times[j])
        temp2 = sorted(set(temp2))
        G = listGCD(temp2)
        if times[0] % G == 0 or G == 1:
            fout.write("Case #%d: 0\n" % i)
        else:
            fout.write("Case #%d: %d\n" % (i, G - (times[0] % G)))
    fout.close()
    
printAns('large')
