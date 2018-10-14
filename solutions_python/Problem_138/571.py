import sys
import Queue
sys.stdin = open('input', 'r')

def war(n, k, N):
    score = 0
    for i in range(N):
        found = False
        for j in range(N):
            if k[j] > n[i]:
                k[j] = 0
                found = True
                break
        if not found:
            score+=1
    return score

def deceitfulWar(n, k, N):
    score = 0
    #for i in range(N):
    #    if n[i] < min(k):
    #        k[k.index(max(k))] = 0
    #    else:
    #        break
    for i in range(N):
        for j in range(N):
            if n[j] > k[i]:
                n[j] = 0
                score+=1
                break
    return score

def solve():
    N = int(sys.stdin.readline())
    naomi = [float(n) for n in sys.stdin.readline().split()]
    ken = [float(n) for n in sys.stdin.readline().split()]
    naomi.sort()
    ken.sort()
    sw = war(naomi[:], ken[:], N)
    sdw = deceitfulWar(naomi[:], ken[:], N)
    return repr(sdw) + ' ' + repr(sw)

numcases = int(sys.stdin.readline())
for casenum in range(1, numcases + 1):
    print 'Case #' + repr(casenum) + ': ' + solve()
