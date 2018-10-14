def printAns(filename):
    fin = open('A-%s.in' % filename, 'r')
    fout = open('A-%s.out' % filename, 'w')
    global temp
    global newTemp
    global n
    t = int(fin.readline().strip())
    for i in xrange(1, t+1):
        n, k = map(int, fin.readline().strip().split(' '))
        temp = []
        newTemp = []
        newTemp2 = []
        for j in xrange(n):
            temp.append(list(fin.readline().strip()))
            newTemp.append([])
            newTemp2.append([])
        #gravity
        for x in xrange(n):
            for y in xrange(n-1, -1, -1):
                if temp[x][y] != '.':
                    newTemp[x].insert(0, temp[x][y])
        for x in xrange(n):
            while len(newTemp[x]) < n:
                newTemp[x].insert(0, '.')
        #rotate
        for x in xrange(n):
            for y in xrange(n):
                newTemp2[y].insert(0, newTemp[x][y])

        #check k-in-a-row
        RWin = False
        BWin = False
        letter = ''
        for x in xrange(n):
            for y in xrange(n):
                if newTemp2[x][y] != '.':
                    letter = newTemp2[x][y] 
                    #check horizontal
                    xk = 1
                    yk = 1
                    while y + yk < n:
                        if newTemp2[x][y+yk] == letter:
                            yk += 1
                        else:
                            break
                        if yk > k - 1:
                            if letter == 'R':
                                RWin = True
                            else:
                                BWin = True
                            break
                    #check vertical
                    xk = 1
                    yk = 1
                    while x + xk < n:
                        if newTemp2[x+xk][y] == letter:
                            xk += 1
                        else:
                            break
                        if xk > k - 1:
                            if letter == 'R':
                                RWin = True
                            else:
                                BWin = True
                            break
                    #check left diagonal
                    xk = 1
                    yk = -1
                    while x + xk < n and y + yk > -1:
                        if newTemp2[x+xk][y+yk] == letter:
                            xk += 1
                            yk -= 1
                        else:
                            break
                        if xk > k - 1:
                            if letter == 'R':
                                RWin = True
                            else:
                                BWin = True
                            break
                    #check right diagonal
                    xk = 1
                    yk = 1
                    while x + xk < n and y + yk < n:
                        if newTemp2[x+xk][y+yk] == letter:
                            xk += 1
                            yk += 1
                        else:
                            break
                        if xk > k - 1:
                            if letter == 'R':
                                RWin = True
                            else:
                                BWin = True
                            break
        if RWin:
            if BWin:
                fout.write("Case #%d: Both\n" % i)
            else:
                fout.write("Case #%d: Red\n" % i)
        else:
            if BWin:
                fout.write("Case #%d: Blue\n" % i)
            else:
                fout.write("Case #%d: Neither\n" % i)
                    
    fin.close()
    fout.close()

printAns('large')
