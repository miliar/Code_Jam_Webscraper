def printAns(filename):
    fin = open('A-%s.in' % filename, 'r')
    fout = open('A-%s.out' % filename, 'w')
    t = int(fin.readline().strip())
    for i in xrange(1, t + 1):
        n = int(fin.readline().strip())
        lines = []
        for j in xrange(n):
            wire = map(int, fin.readline().strip().split(' '))
            lines.append(wire)
        count = 0
        for j in xrange(n-1):
            for k in xrange(j+1, n):
                pred1 = lines[j][0] > lines[k][0] and lines[j][1] < lines[k][1]
                pred2 = lines[j][0] < lines[k][0] and lines[j][1] > lines[k][1]
                if pred1 or pred2:
                    count += 1
        fout.write("Case #%d: %d\n" % (i, count))
    fin.close()
    fout.close()

printAns('large')
