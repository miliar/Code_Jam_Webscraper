def transpose(arr):
    r = len(arr)
    c = len(arr[0])
    narr = [[0]*r for i in xrange(c)]
    for i in xrange(r):
        for j in xrange(c):
            narr[j][i] = arr[i][j]
    return narr
keis = int(raw_input())
for kei in xrange(keis):
    r,c,m = [int(x) for x in raw_input().split()]
    print('Case #%d:' % (kei+1,))
    if r*c == m+1:
        for i in xrange(r-1):
            print '*'*c
        print '*'*(c-1) + 'c'
    elif m == 0:
        for i in xrange(r-1):
            print '.'*c
        print '.'*(c-1) + 'c'
    elif r == 1:
        print '*'*m + '.'*(c-m-1) + 'c'
    elif c == 1:
        for i in xrange(m):
            print '*'
        for i in xrange(r-m-1):
            print '.'
        print 'c'
    elif (r,c) == (2,2):
        print 'Impossible'
    elif (r,c) == (2,3):
        if m == 2:
            print '*..\n*.c'
        else:
            print 'Impossible'
    elif (r,c) == (3,2):
        if m == 2:
            print '**\n..\n.c'
        else:
            print 'Impossible'
    elif (r,c) == (2,4):
        if m == 2:
            print '*...\n*..c'
        elif m == 4:
            print '**..\n**.c'
        else:
            print 'Impossible'
    elif (r,c) == (4,2):
        if m == 2:
            print '**\n..\n..\n.c'
        elif m == 4:
            print '**\n**\n..\n.c'
        else:
            print 'Impossible'
    elif (r,c) == (2,5):
        if m == 2:
            print '*....\n*...c'
        elif m == 4:
            print '**...\n**..c'
        elif m == 6:
            print '***..\n***.c'
        else:
            print 'Impossible'
    elif (r,c) == (5,2):
        if m == 2:
            print '**\n..\n..\n..\n.c'
        elif m == 4:
            print '**\n**\n..\n..\n.c'
        elif m == 6:
            print '**\n**\n**\n..\n.c'
        else:
            print 'Impossible'
    elif (r,c) == (3,3):
        if m == 1:
            print '*..\n...\n..c'
        elif m == 3:
            print '***\n...\n..c'
        elif m == 5:
            print '***\n*..\n*.c'
        else:
            print 'Impossible'
    elif (r,c) == (3,4):
        if m == 1:
            print '*...\n....\n...c'
        elif m == 2:
            print '**..\n....\n...c'
        elif m == 3:
            print '*...\n*...\n*..c'
        elif m == 4:
            print '****\n....\n...c'
        elif m == 6:
            print '**..\n**..\n**.c'
        elif m == 8:
            print '****\n**..\n**.c'
        else:
            print 'Impossible'
    elif (r,c) == (4,3):
        if m == 1:
            print '*..\n...\n...\n..c'
        elif m == 2:
            print '*..\n*..\n...\n..c'
        elif m == 3:
            print '***\n...\n...\n..c'
        elif m == 4:
            print '*..\n*..\n*..\n*.c'
        elif m == 6:
            print '***\n***\n...\n..c'
        elif m == 8:
            print '***\n***\n*..\n*.c'
        else:
            print 'Impossible'
    elif (r,c) == (3,5):
        arr = [['.']*5 for i in xrange(3)]
        if 1 <= m <= 3:
            arr[0][0] = '*'
            if m >= 2:
                arr[0][1] = '*'
            if m >= 3:
                arr[0][2] = '*'
            arr[2][4] = 'c'
            for row in arr:
                print ''.join(row)
        elif m in [4,5]:
            for i in xrange(3):
                arr[i][0] = '*'
            arr[0][1] = '*'
            if m >= 5:
                arr[0][2] = '*'
            arr[2][4] = 'c'
            for row in arr:
                print ''.join(row)
        elif m in [6,7]:
            for i in xrange(3):
                for j in xrange(2):
                    arr[i][j] = '*'
            if m >= 7:
                arr[0][2] = '*'
            arr[2][4] = 'c'
            for row in arr:
                print ''.join(row)
        elif m in [9,11]:
            for i in xrange(5):
                arr[0][i] = '*'
            for i in xrange(3):
                for j in xrange(2):
                    arr[i][j] = '*'
            if m == 11:
                arr[1][2] = arr[2][2] = '*'
            arr[2][4] = 'c'
            for row in arr:
                print ''.join(row)
        else:
            print 'Impossible'
    elif (r,c) == (5,3):
        arr = [['.']*5 for i in xrange(3)]
        if 1 <= m <= 3:
            arr[0][0] = '*'
            if m >= 2:
                arr[0][1] = '*'
            if m >= 3:
                arr[0][2] = '*'
            arr[2][4] = 'c'
            arr = transpose(arr)
            for row in arr:
                print ''.join(row)
        elif m in [4,5]:
            for i in xrange(3):
                arr[i][0] = '*'
            arr[0][1] = '*'
            if m >= 5:
                arr[0][2] = '*'
            arr[2][4] = 'c'
            arr = transpose(arr)
            for row in arr:
                print ''.join(row)
        elif m in [6,7]:
            for i in xrange(3):
                for j in xrange(2):
                    arr[i][j] = '*'
            if m >= 7:
                arr[0][2] = '*'
            arr[2][4] = 'c'
            arr = transpose(arr)
            for row in arr:
                print ''.join(row)
        elif m in [9,11]:
            for i in xrange(5):
                arr[0][i] = '*'
            for i in xrange(3):
                for j in xrange(2):
                    arr[i][j] = '*'
            if m == 11:
                arr[1][2] = arr[2][2] = '*'
            arr[2][4] = 'c'
            arr = transpose(arr)
            for row in arr:
                print ''.join(row)
        else:
            print 'Impossible'
    elif (r,c) == (4,4):
        arr = [['.']*4 for i in xrange(4)]
        if 1 <= m <= 4:
            arr[0][0] = '*'
            if m >= 2:
                arr[0][1] = '*'
            if m >= 3:
                arr[1][0] = '*'
            if m >= 4:
                arr[1][1] = '*'
            arr[3][3] = 'c'
            for row in arr:
                print ''.join(row)
        elif 5 <= m <= 6:
            arr[0] = ['*']*4
            arr[1][0] = '*'
            if m >= 6:
                arr[1][1] = '*'
            arr[3][3] = 'c'
            for row in arr:
                print ''.join(row)
        elif 7 <= m <= 8:
            arr[0] = ['*']*4
            for i in xrange(1,4):
                arr[i][0] = '*'
            if m == 8:
                arr[1][1] = '*'
            arr[3][3] = 'c'
            for row in arr:
                print ''.join(row)
        elif m in [10, 12]:
            arr[0] = ['*']*4
            arr[1] = ['*']*4
            arr[2][0] = arr[3][0] = '*'
            if m == 12:
                arr[2][1] = arr[3][1] = '*'
            arr[3][3] = 'c'
            for row in arr:
                print ''.join(row)
        else:
            print 'Impossible'
    elif (r,c) == (4,5):
        arr = [['.']*5 for i in xrange(4)]
        if 1 <= m <= 6:
            arr[0][0] = '*'
            if m >= 2:
                arr[0][1] = '*'
            if m >= 3:
                arr[0][2] = '*'
            if m >= 4:
                arr[1][0] = '*'
            if m >= 5:
                arr[1][1] = '*'
            if m >= 6:
                arr[1][2] = '*'
            arr[3][4] = 'c'
            for row in arr:
                print ''.join(row)
        elif 7 <= m <= 8:
            for i in xrange(4):
                arr[i][0] = '*'
            for i in xrange(2):
                arr[i][1] = '*'
            arr[0][2] = '*'
            if m == 8:
                arr[1][2] = '*'
            arr[3][4] = 'c'
            for row in arr:
                print ''.join(row)
        elif 9 <= m <= 10:
            for i in xrange(4):
                arr[i][0] = '*'
            for i in xrange(4):
                arr[i][1] = '*'
            arr[0][2] = '*'
            if m == 10:
                arr[1][2] = '*'
            arr[3][4] = 'c'
            for row in arr:
                print ''.join(row)
        elif 11 <= m <= 12:
            for i in xrange(5):
                arr[0][i] = '*'
            for i in xrange(4):
                for j in xrange(2):
                    arr[i][j] = '*'
            if m == 12:
                arr[1][2] = '*'
            arr[3][4] = 'c'
            for row in arr:
                print ''.join(row)
        elif m in [14,16]:
            for i in xrange(2):
                for j in xrange(5):
                    arr[i][j] = '*'
            for i in xrange(4):
                for j in xrange(2):
                    arr[i][j] = '*'
            if m == 16:
                arr[2][2] = arr[3][2] = '*'
            arr[3][4] = 'c'
            for row in arr:
                print ''.join(row)
        else:
            print 'Impossible'
    elif (r,c) == (5,4):
        arr = [['.']*5 for i in xrange(4)]
        if 1 <= m <= 6:
            arr[0][0] = '*'
            if m >= 2:
                arr[0][1] = '*'
            if m >= 3:
                arr[0][2] = '*'
            if m >= 4:
                arr[1][0] = '*'
            if m >= 5:
                arr[1][1] = '*'
            if m >= 6:
                arr[1][2] = '*'
            arr[3][4] = 'c'
            arr = transpose(arr)
            for row in arr:
                print ''.join(row)
        elif 7 <= m <= 8:
            for i in xrange(4):
                arr[i][0] = '*'
            for i in xrange(2):
                arr[i][1] = '*'
            arr[0][2] = '*'
            if m == 8:
                arr[1][2] = '*'
            arr[3][4] = 'c'
            arr = transpose(arr)
            for row in arr:
                print ''.join(row)
        elif 9 <= m <= 10:
            for i in xrange(4):
                arr[i][0] = '*'
            for i in xrange(4):
                arr[i][1] = '*'
            arr[0][2] = '*'
            if m == 10:
                arr[1][2] = '*'
            arr[3][4] = 'c'
            arr = transpose(arr)
            for row in arr:
                print ''.join(row)
        elif 11 <= m <= 12:
            for i in xrange(5):
                arr[0][i] = '*'
            for i in xrange(4):
                for j in xrange(2):
                    arr[i][j] = '*'
            if m == 12:
                arr[1][2] = '*'
            arr[3][4] = 'c'
            arr = transpose(arr)
            for row in arr:
                print ''.join(row)
        elif m in [14,16]:
            for i in xrange(2):
                for j in xrange(5):
                    arr[i][j] = '*'
            for i in xrange(4):
                for j in xrange(2):
                    arr[i][j] = '*'
            if m == 16:
                arr[2][2] = arr[3][2] = '*'
            arr[3][4] = 'c'
            arr = transpose(arr)
            for row in arr:
                print ''.join(row)
        else:
            print 'Impossible'
    elif (r,c) == (5,5,):
        arr = [['.']*5 for i in xrange(5)]
        if 1 <= m <= 9:
            arr[0][0] = '*'
            if m >= 2:
                arr[0][1] = '*'
            if m >= 3:
                arr[0][2] = '*'
            if m >= 4:
                arr[1][0] = '*'
            if m >= 5:
                arr[1][1] = '*'
            if m >= 6:
                arr[1][2] = '*'
            if m >= 7:
                arr[2][0] = '*'
            if m >= 8:
                arr[2][1] = '*'
            if m >= 9:
                arr[2][2] = '*'
            arr[4][4] = 'c'
            for row in arr:
                print ''.join(row)
        elif 10 <= m <= 13:
            for i in xrange(2):
                for j in xrange(5):
                    arr[i][j] = '*'
            if m >= 11:
                arr[2][0] = '*'
            if m >= 12:
                arr[2][1] = '*'
            if m >= 13:
                arr[2][2] = '*'
            arr[4][4] = 'c'
            for row in arr:
                print ''.join(row)
        elif 14 <= m <= 15:
            for i in xrange(5):
                arr[0][i] = '*'
            for i in xrange(5):
                for j in xrange(2):
                    arr[i][j] = '*'
            arr[1][2] = '*'
            if m >= 15:
                arr[2][2] = '*'
            arr[4][4] = 'c'
            for row in arr:
                print ''.join(row)
        elif 16 <= m <= 17:
            for i in xrange(2):
                for j in xrange(5):
                    arr[i][j] = '*'
            for i in xrange(5):
                for j in xrange(2):
                    arr[i][j] = '*'
            if m >= 17:
                arr[2][2] = '*'
            arr[4][4] = 'c'
            for row in arr:
                print ''.join(row)
        elif m in [19,21]:
            for i in xrange(3):
                for j in xrange(5):
                    arr[i][j] = '*'
            for i in xrange(5):
                for j in xrange(2):
                    arr[i][j] = '*'
            if m >= 21:
                arr[3][2] = arr[4][2] = '*'
            arr[4][4] = 'c'
            for row in arr:
                print ''.join(row)
        else:
            print 'Impossible'

