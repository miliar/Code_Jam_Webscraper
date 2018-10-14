n = input()
for iii in xrange(n):
    firstRow = input()
    firstData = []
    for i in xrange(4):
        if i+1 == firstRow:
            firstData = map(int, raw_input().split())
        else:
            temp = raw_input()
    secondRow = input()
    secondData = []
    for i in xrange(4):
        if i+1 == secondRow:
            secondData = map(int, raw_input().split())
        else:
            temp = raw_input()
    ans = []
    for i in firstData:
        if i in secondData:
            ans.append(i)
    if len(ans) == 1:
        print 'Case #' + str(iii+1) + ': ' + str(ans[0])
    elif len(ans) == 0:
        print 'Case #' + str(iii+1) + ': Volunteer cheated!'
    else:
        print 'Case #' + str(iii+1) + ': Bad magician!'
