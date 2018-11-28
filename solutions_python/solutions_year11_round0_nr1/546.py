# -*- coding: utf-8 -*-

def direction(curPos, nexPos):
    if curPos < nexPos:
        return 1
    return -1

def nextBlue(orders):
    for (r, k) in orders:

        if r == 'B':
            return k

def nextOrange(orders):
    for (r, k) in orders:
        if r == 'O':
            return k


data = open('A.in', 'r').read().split('\n')
output = open('A.out', 'w')

T = int(data.pop(0))

for t in range(T):

    orders = data.pop(0).split(' ')
    N = int(orders.pop(0))
    ordPairs = []
    for i in range(N):
        r = orders.pop(0)
        k = int(orders.pop(0))
        ordPairs.append((r, k))

    ans = 0
    bluePos = 1
    orangePos = 1
    blueChangedNext = True
    orangeChangedNext = True

    while ordPairs:
        bPressed = False
        if blueChangedNext:
            nb = nextBlue(ordPairs)
            blueChangedNext = False
        if orangeChangedNext:
            no = nextOrange(ordPairs)
            orangeChangedNext = False

        if nb == bluePos:
            if ordPairs[0][0] == 'B':
                bPressed = True
                blueChangedNext = True
        else:
            bluePos += direction(bluePos, nb)

        if no == orangePos:
            if ordPairs[0][0] == 'O':
                bPressed = True
                orangeChangedNext = True
        else:
            orangePos += direction(orangePos, no)

        if bPressed:
            ordPairs.pop(0)
        ans += 1

    print 'Case #' + str(t+1) + ': ' + str(ans)
    output.write('Case #' + str(t+1) + ': ' + str(ans) + '\n')
output.close()

