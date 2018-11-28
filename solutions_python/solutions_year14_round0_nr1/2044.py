import sys

f = open(sys.argv[1])

case = int(f.readline().strip())
for n in xrange(1, case + 1):
    c1 = int(f.readline().strip())
    grid1 = []
    for i in xrange(0,4):
        grid1.append(f.readline().strip().split())

    c2 = int(f.readline().strip())
    grid2 = []
    for i in xrange(0,4):
        grid2.append(f.readline().strip().split())

    row1 = grid1[c1-1] 
    row2 = grid2[c2-1] 

    count = 0
    ans = 'Volunteer cheated!'
    for i in row1:
        if i in row2:
            count += 1
            ans = i
            if count > 1:
                ans = 'Bad magician!'
                break

    print "Case #%d: %s"%(n, ans)
