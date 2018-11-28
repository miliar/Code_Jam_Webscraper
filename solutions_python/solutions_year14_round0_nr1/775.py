import sys
line = sys.stdin.readline()
numTests = int(line)
for test in xrange(1, numTests+1):
    choice1 = int(sys.stdin.readline())
    grid1 = {}
    for i in xrange(1, 5):
        row1 = sys.stdin.readline().split(' ')
        row1 = set([int(item) for item in row1])
        grid1[i] = row1

    choice2 = int(sys.stdin.readline())
    grid2 = {}
    for i in xrange(1 ,5):
        row2 = sys.stdin.readline().split(' ')
        row2 = set([int(item) for item in row2])    
        grid2[i] = row2
    
    intersection = (grid1[choice1] & grid2[choice2])
    if (len(intersection) == 0):
        print 'Case #%d: Volunteer cheated!' %(test)
    if (len(intersection) == 1):
        print 'Case #%d: %d' %(test, intersection.pop())
    if (len(intersection) > 1):
        print 'Case #%d: Bad magician!' %(test)
