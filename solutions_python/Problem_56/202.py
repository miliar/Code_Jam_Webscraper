def gravity(a):
    ans = []
    for x in a:
        tp = []
        cnt = 0
        for y in x[::-1]:
            if y != '.':
                tp += y
                cnt += 1
        for z in xrange(len(a) - cnt):
            tp += ['.']
        ans += [tp[::-1]]
    return ans

def in_row(a, c, k):
    ans = False
    # Right
    for x in xrange(len(a)):
        for y in xrange(len(a) - k + 1):
            if a[x][y] == c:
                ans = True
                for i in xrange(k):
                    if a[x][y+i] != c:
                        ans = False
                if ans == True:
                    return ans
    # Down
    for x in xrange(len(a) - k + 1):
        for y in xrange(len(a)):
            if a[x][y] == c:
                ans = True
                for i in xrange(k):
                    if a[x+i][y] != c:
                        ans = False
                if ans == True:
                    return ans
    #Right-down
    for x in xrange(len(a) - k + 1):
        for y in xrange(len(a) - k + 1):
            if a[x][y] == c:
                ans = True
                for i in xrange(k):
                    if a[x+i][y+i] != c:
                        ans = False
                if ans == True:
                    return ans
    # Right-up
    for x in xrange(k - 1, len(a)):
        for y in xrange(len(a) - k + 1):
            if a[x][y] == c:
                ans = True
                for i in xrange(k):
                    if a[x-i][y+i] != c:
                        ans = False
    return ans

def rotate(a):
    ans = []
    for x in xrange(len(a)):
        tp = []
        for y in xrange(len(a) - 1, -1, -1):
            tp += a[y][x]
        ans += [tp]
    return ans

fin = open('small.in')
fout = open('result.out', 'w')
data = fin.readlines()
for x in xrange(len(data)):
    data[x] = data[x][:-1]
case = int(data[0])
cnt = 1
for x in xrange(1, case + 1):
    temp = (data[cnt]).split(' ')
    n = int(temp[0])
    k = int(temp[1])
    cnt += 1
    trans = []
    for y in xrange(n):
        trans += [data[y + cnt]]
    cnt += n
    #print trans
    trans = gravity(trans)
    #print trans
    trans = rotate(trans)
    #print trans
    ans = []
    ans += [in_row(trans, 'R', k)]
    ans += [in_row(trans, 'B', k)]
    #print ans
    anss = ''
    if ans == [False, False]:
        anss = 'Neither'
    elif ans == [True, True]:
        anss = 'Both'
    elif ans == [True, False]:
        anss = 'Red'
    else:
        anss = 'Blue'
    print >>fout, 'Case #' + str(x) + ':', anss
fin.close()
fout.close()
