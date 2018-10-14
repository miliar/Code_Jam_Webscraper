import math
fd = file('B-large.in')
totalTestCase = int(fd.readline())
def genTestCase(fd):
    global totalTestCase
    while totalTestCase > 0:
        lawn = []
        (totalRow, totalCol) = [int(x) for x in fd.readline().strip().split()]
        for i in xrange(totalRow):
            lawn.append( [int(x) for x in fd.readline().strip().split()] )
        totalTestCase -= 1
        yield (lawn, totalRow, totalCol)
    fd.close()
tc_seq = 1
for (lawn, totalRow, totalCol) in genTestCase(fd):
    possible = True
    ##min height requirement to operate on each row
    row_hmin_list = [max(x) for x in lawn] 
    ##min height requirement to operate on each col
    col_hmin_list = [max( [row[i] for row in lawn] ) for i in xrange(totalCol)]
    for row_idx in xrange(totalRow):
        for col_idx in xrange(totalCol):
            if lawn[row_idx][col_idx] < row_hmin_list[row_idx] and \
                    lawn[row_idx][col_idx] < col_hmin_list[col_idx]:
                possible = False
                break
        if not possible:
            break
    if possible:
        print 'Case #%d: YES'%tc_seq
    else:
        print 'Case #%d: NO'%tc_seq
    tc_seq += 1
