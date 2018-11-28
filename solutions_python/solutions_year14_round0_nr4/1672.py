import bisect

lines = [line.strip() for line in open('input4.txt')]

testCase = lines[0]
testCase = int(testCase)

output = ""

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return i
    else:
        return 'f'

for x in range(0, int(testCase)):
    curStart = (x * 3) + 1
    
    p1 = lines[curStart + 1].split()
    p2 = lines[curStart + 2].split()

    p1 = list(map(float, p1))
    p2 = list(map(float, p2))

    p1.sort()
    p2.sort()

    #print("P1: " + str(p1))
    #print("P2: " + str(p2))

    #war
    warWin = 0
    warP1 = list(p1)
    warP2 = list(p2)

    while (len(warP1) > 0):
        popOut = warP1.pop(0)
        toPop = find_ge(warP2, popOut)
        #print(warP2)
        if toPop == 'f':
            toPop = 0
        popOut2 = warP2.pop(toPop)

        #print("P1 :" + str(popOut) + ", P2 :" + str(popOut2))

        if float(popOut2) < float(popOut):
            warWin = warWin + 1

    #dewar
    dewarWin = 0
    dewarP1 = list(p1)
    dewarP2 = list(p2)
    
    while (len(dewarP1) > 0):
        popOut = dewarP2.pop(0)
        toPop = find_ge(dewarP1, popOut)

        #print(warP2)
        if toPop == 'f':
            toPop = 0
        popOut2 = dewarP1.pop(toPop)

        #print("P1 :" + str(popOut) + ", P2 :" + str(popOut2))

        if float(popOut2) > float(popOut):
            dewarWin = dewarWin + 1
    

    print("Case #" + str(x + 1) + ": " + str(dewarWin) + " " + str(warWin))
