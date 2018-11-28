import sys


def magician(ans1, ans2, x, y):
    # x and y -> two boards

    row1 = set(x[ans1-1])
    row2 = set(y[ans2-1])

    answer = row1.intersection(row2)

    if len(answer) == 0:
        return 'Volunteer cheated!'

    if len(answer) == 1:
        answer = answer.pop()
        
        return answer

    else:
        return 'Bad magician!'
    


T = int(sys.stdin.readline())
for casenum in xrange(T):
    ans1 = int(sys.stdin.readline())
    x = []
    y = []

    for i in xrange(4):
        b = map(int, sys.stdin.readline().strip().split(' '))
        x.append(b)

    ans2 = int(sys.stdin.readline())
    for i in xrange(4):
        b = map(int, sys.stdin.readline().strip().split(' '))
        y.append(b)

    print 'Case #%d: %s' % (casenum + 1, str(magician(ans1,ans2,x,y)))
    

