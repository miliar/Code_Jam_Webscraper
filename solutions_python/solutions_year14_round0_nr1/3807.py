import numpy
from StringIO import StringIO

test_cases = int(raw_input())


for i in range(0,test_cases):
    foundColumn = []
    for k in range(0,2):
        col = int(raw_input())
        matrix = ''
        for j in range(0,4):
            matrix+=raw_input()+'\n'
        mat = numpy.loadtxt(StringIO(matrix),dtype=numpy.int32)
        foundColumn.append(mat[col-1].tolist())
    common = []
    for x in foundColumn[0]:
        for y in foundColumn[1]:
            if x == y:
                common.append(x)
    print "Case #"+str(i+1)+": ",
    if len(common) == 1:
        print str(common[0])
    elif len(common) == 0:
        print "Volunteer cheated!"
    else:
        print "Bad magician!"

