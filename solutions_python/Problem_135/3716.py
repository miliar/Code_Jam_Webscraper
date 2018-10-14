import sys

fi = open(sys.argv[1],'r')
N = int(fi.readline())
for i in xrange(N):
    row1 = int(fi.readline())
    for j in xrange(4):
        line = fi.readline()
        if j==row1-1:
            content1 = line.strip().split(' ')
    row2 = int(fi.readline())
    for j in xrange(4):
        line = fi.readline()
        if j==row2-1:
            content2 = line.strip().split(' ')

    intersection = list(set(content1).intersection(set(content2)))
    if len(intersection)==1:
        print 'Case #%d: %s'%(i+1,intersection[0])
    if len(intersection)>1:
        print 'Case #%d: Bad magician!'%(i+1)
    if len(intersection)==0:
        print 'Case #%d: Volunteer cheated!'%(i+1)
