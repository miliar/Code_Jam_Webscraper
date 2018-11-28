def printAns(filename):
    fin = open('A-%s.in' % filename, 'r')
    fout = open('A-%s.out' % filename, 'w')
    t = int(fin.readline().strip())
    for i in xrange(1, t + 1):
        n, m = map(int, fin.readline().strip().split(' '))
        folderSet = set()
        mkdirList = []
        for j in xrange(n):
            folderSet.add(fin.readline().strip()[1:])
        for j in xrange(m):
            mkdirList.append(fin.readline().strip()[1:].split('/'))
        count = 0
        for folder in mkdirList:
            for k in xrange(len(folder)):
                directory = '/'.join(folder[:k+1])
                if directory not in folderSet:
                    folderSet.add(directory)
                    count += 1
        #print count
        fout.write("Case #%d: %d\n" % (i, count))
    fin.close()
    fout.close()

printAns('large')
