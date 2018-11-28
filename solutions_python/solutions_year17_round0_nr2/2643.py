def checkTidy(stringN):
    for i in range(len(stringN)-1):
        if stringN[i] > stringN[i+1]:
            return False
    return True


def changeNumber(stringN, i):
    stringN[i] = str(9)
    if int(stringN[i-1]) == 0:
        changeNumber(stringN, i-1)
    else:
        stringN[i-1] = str(int(stringN[i-1]) - 1)

    

def largestTidy(N):
    if N<10:
        return N
    else:
        stringN = list(str(N))

        i = len(stringN)-1
        while i >= 0:
            if not checkTidy(stringN):
                if stringN[i] != 9:
                    changeNumber(stringN, i)
                    
                i -= 1
            else:
                if int(stringN[0]) == 0:
                    return int(''.join(stringN[1:]))
                else:
                    return int(''.join(stringN))

T = int(raw_input())
for i in xrange(1, T+1):
    N = int(raw_input())
    print "Case #{}: {}".format(i, largestTidy(N))
