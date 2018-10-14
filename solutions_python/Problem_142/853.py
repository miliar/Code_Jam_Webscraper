"""
1a2b8c3d...

"""
import sys

def compute(rls):
    first = rls[0]
    moves = 0
    n = len(rls)
    moves = 0
    for i in range(len(first)):
        totalI = first[i][1]
        minI = first[i][1]
        for j in range(1, len(rls)):
            totalI += rls[j][i][1]
            if rls[j][i][1] < minI:
                minI = rls[j][i][1]
        remainder = totalI % n
        if remainder > n - remainder:
            optimalI = totalI + n - remainder
        else:
            optimalI = totalI - remainder
        mean = optimalI / n
        for j in range(len(rls)):
            moves += abs(mean - rls[j][i][1])

    return moves



def getRunLength(s):
    rl = []
    lastChar = s[0]
    lastCnt = 1
    i = 1
    while i < len(s):
        if s[i] == lastChar:
            lastCnt += 1
        else:
            rl.append((lastChar, lastCnt))
            lastChar = s[i]
            lastCnt = 1
        i += 1
    rl.append((lastChar, lastCnt))
    return rl

with sys.stdin as f:
    T = int(f.readline())
    for case in range(T):
        N = int(f.readline())
        rls = []
        for i in range(N):
            s = f.readline().strip()
            rl = getRunLength(s)
            rls.append(rl)
        first = [i[0] for i in rls[0]]
        feglaWon = False
        for rl in rls:
            if [i[0] for i in rl] != first:
                feglaWon = True
                break
        if feglaWon:
            print "Case #%d: Fegla Won" % (case + 1)
        else:
            print "Case #%d: %d" % (case + 1, compute(rls))
