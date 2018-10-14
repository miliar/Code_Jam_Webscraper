def printAns(filename):
    fin = open('003%s.in' % filename, 'r').read().split('\n')[:-1]
    fout = open('003%s.out' % filename, 'w')
    t = int(fin[0])
    i = 1
    while i < 2*t:
        r, k, n = map(int, fin[i].split(' '))
        groups = map(int, fin[i+1].split(' '))
        money = 0
        queue = []
        for j in xrange(n):
            total = 0
            m = j
            l = 0
            while total + groups[m] <= k:
                total += groups[m]
                m = (m + 1) % n
                l += 1
                if l % n == 0:
                    break
            queue.append([total, m])
        m = 0
        for j in xrange(r):
            money += queue[m][0]
            m = queue[m][1]
        fout.write("Case #%d: %d\n" % ((i+1)/2, money))
        i += 2
    fout.close()
    
printAns('large')
