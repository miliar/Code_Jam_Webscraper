from sys import argv
lines = open(argv[1]).readlines()
casecount = int(lines.pop(0))
for i in xrange(casecount):
    rowindex1 = int(lines.pop(0))-1
    grid1 = [row.split() for row in [lines.pop(0).strip() for j in xrange(4)]]
    rowindex2 = int(lines.pop(0))-1
    grid2 = [row.split() for row in [lines.pop(0).strip() for j in xrange(4)]]
    doubles =[]
    for item in grid1[rowindex1]:
        if item in grid2[rowindex2]:
            doubles.append(item)
    #print doubles
    if len(doubles)==0:
        print 'Case #%i: Volunteer cheated!'%(i+1)
    elif len(doubles)==1:
        print 'Case #%i: %s' %(i+1, doubles[0])
    elif len(doubles)>1:
        print 'Case #%i: Bad magician!'%(i+1)