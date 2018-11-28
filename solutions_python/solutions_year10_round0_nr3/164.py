def readint(): return int(raw_input())
def readarray(f): return map(f,raw_input().split())

def solve(R,k,N,groups):
    ncache = {} # key:N , value: (earn,nextN)
    loop = None # (startN,num,sum_earn)
    initk = k
    curN = 0
    totalEuro = 0
    while R > 0:
        if ncache.has_key(curN):
            (startN,num,sum) = loop
            if curN == startN and R > num:
                totalEuro += sum
                R -= num
                continue
            else:
                (euro,nextN) = ncache[curN]
                totalEuro += euro
                curN = nextN
        else:
            k = initk
            euro = 0
            prevN = curN
            while k >= groups[curN%N]:
                k -= groups[curN%N]
                euro += groups[curN%N]
                curN = (curN+1)%N
                if curN == prevN: break
            ncache[prevN] = (euro,curN)
            if loop == None:
                loop = (prevN,1,euro)
            else:
                (startN,num,sum) = loop
                loop = (startN,num+1,sum+euro)
            totalEuro += euro
        R -= 1
    return totalEuro


T = readint()
for t in xrange(T):
    R,k,N = readarray(int)
    groups = readarray(int)
    ans = solve(R,k,N,groups)
    print "Case #%d: %d" % (t+1,ans)
                
