
T = int(raw_input())  
for K in xrange (T):
    n, m = [int(g) for g in raw_input().split(" ")]
    
    plusMap = [['.'] * n for i in xrange(n)]
    xMap = [['.'] * n for i in xrange(n)]
    
    plusMark, xMark = [], []
    xRow, xCol = set(range(n)), set(range(n))

    ans = 0

    for i in xrange(m):
        s, r, c = [g for g in raw_input().split(" ")]
        r, c = int(r), int(c)
        if (s in ['+', 'o']):
            plusMark.append([r, c])
            ans += 1
        if (s in ['x', 'o']):
            xMark.append([r, c])
            xRow.remove(r - 1)
            xCol.remove(c - 1)
            #xMap[r - 1][c - 1] = 'x'
            ans += 1

    leftToRight = lambda left: min(left - 1, n) * 2 - left
    rightToLeft = []
    for i in xrange(n):
        rightToLeft.append(set([i + 2, 2 * n - i]))
    if (len(rightToLeft) > 1):
        rightToLeft[0].pop()
    #print rightToLeft

    rightCount = set([])
    for plus in plusMark:
        [r, c] = plus
        #plusMap[r - 1][c - 1] = '+'
        left, right = r + c, abs(r - c)
        rightCount.add(r - c)
        if leftToRight(left) > right:
            rightToLeft[right].pop()
        #print(n, m, left, leftToRight(left))
        right = leftToRight(left)
        if (right == 0):
            rightToLeft[0].pop()
        else:
            rightToLeft[leftToRight(left)].remove(left)

    for i in xrange(n):
        right = rightToLeft[i]
        if (len(right) == 2):
            l = right.pop()
            r = i
            plusMap[(l + r) / 2 - 1][(l - r) / 2 - 1] = '+'
            ans += 1
            l = right.pop()
            r = -i
            plusMap[(l + r) / 2 - 1][(l - r) / 2 - 1] = '+'
            ans += 1
        elif (len(right) == 1):
            l = right.pop()
            if i in rightCount:
                r = -i
            else:
                r = i
            plusMap[(l + r) / 2 - 1][(l - r) / 2 - 1] = '+'
            ans += 1
    #print plusMap


    xMap = [['.'] * n for i in xrange(n)]
    while (len(xRow) > 0):
        xMap[xRow.pop()][xCol.pop()] = 'x'
        ans += 1
    #print xMap

    count = 0
    s = ""
    for i in xrange(n):
        for j in xrange(n):
            if (plusMap[i][j] == '+') and (xMap[i][j] == 'x'):
                count += 1
                s += "\no " + str(i + 1) + ' ' + str(j + 1)
            elif (plusMap[i][j] == '+'):
                if ([i + 1, j + 1] in xMark):
                    s += "\no "
                else:
                    s += "\n+ "
                count += 1
                s += str(i + 1) + ' ' + str(j + 1)
            elif (xMap[i][j] == 'x'):
                if ([i + 1, j + 1] in plusMark):
                    s += "\no "
                else:
                    s += "\nx "
                count += 1
                s += str(i + 1) + ' ' + str(j + 1)
    
    print "Case #{}: {} {}".format(K+1, ans, count)
    if count > 0:
        print s.strip("\n")





