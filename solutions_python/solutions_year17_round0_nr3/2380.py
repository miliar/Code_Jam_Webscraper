def compareTup(t1, t2):
    (n1, l1, r1) = t1
    (n2, l2, r2) = t2
    if (n1 > n2):
        return True
    elif (n1 == n2):
        if l1 <= l2:
            return True
    return False

def insertTup(myArr, myAdd, myComp):
    if len(myArr) == 0:
        myArr.append(myAdd)
        return
    l = 0
    r = len(myArr) - 1
    while ((r - l) > 1):
        mid = int((l + r)/2)
        if (compareTup(myAdd, myArr[mid])):
            r = mid
        else:
            l = mid
    c1 = compareTup(myAdd, myArr[l])
    c2 = compareTup(myAdd, myArr[r])
    if (c1):
        myArr.insert(l, myAdd)
    elif (c2):
        myArr.insert(r, myAdd)
    else:
        myArr.insert(r+1, myAdd)

def solveBathroom(N, K):
    myParts = []
    myParts.append((N, 0, N-1))

    for i in range(K-1):
        biggestP = myParts.pop(0)
        (myLen, myL, myR) = biggestP
        if (myLen % 2 == 0):
            newTup1 = (int(myLen/2), int((myL + myR)/2) + 1, myR)
            newTup2 = (int(myLen/2) - 1, myL, int((myL + myR)/2) - 1)
            insertTup(myParts, newTup1, compareTup)
            insertTup(myParts, newTup2, compareTup)
        else:
            newTup1 = (int(myLen/2), myL, int((myL + myR)/2) - 1)
            newTup2 = (int(myLen/2), int((myL + myR)/2)+1, myR)
            insertTup(myParts, newTup1, compareTup)
            insertTup(myParts, newTup2, compareTup)
    remP = myParts.pop(0)
    (finalLen, finalL, finalR) = remP
    if (finalLen % 2 == 0):
        a = int(finalLen / 2)
        return (a, a-1)
    else:
        a = int((finalLen - 1) / 2)
        return (a, a)

myTxt = ''
with open('C-small-1-attempt0.in', 'r') as f:
    lineCount = 0
    for line in f:
        if lineCount == 0:
            lineCount += 1
            continue
        else:
            myVars = line.strip().split()
            n = int(myVars[0])
            k = int(myVars[1])
            (m1, m2) = solveBathroom(n, k)
            myTxt += 'Case #' + str(lineCount) + ': ' + str(m1) + ' ' + str(m2) + '\n'
            # print('Case #{}: {}'.format(lineCount, lastTidy(n)))
            lineCount += 1
with open('bathroom_small_out.txt', 'w') as f:
    f.write(myTxt)
