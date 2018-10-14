def findmax(n):
    return n//2

def findmin(n):
    return n//2 - (n % 2 + 1)%2

def getresult(n, k):
    if k == 1:
        return findmax(n), findmin(n)
    if k == 2:
        return findmax(findmax(n)), findmin(findmax(n))
    summ = n - 1
    maxx = findmax(n)
    minn = findmin(n)
    pow2 = 0
    step = 1
    while step < k:
        prevsumm = summ
        prevmaxx = maxx
        prevminn = minn
        prevpow2 = pow2
        prevstep = step
        step += 2**(pow2 + 1)
        summ -= 2**(pow2 + 1)
        pow2 += 1
        minn = findmin(prevminn)
        maxx = findmax(prevmaxx)
    if k == prevstep:
        return findmax(prevmaxx), findmin(prevmaxx)
    if k > prevstep:
        if prevmaxx == prevminn:
            return findmax(prevmaxx), findmin(prevmaxx)
        else:
            p = prevsumm + (2**(prevpow2 + 1))*(1 - prevmaxx)
            if prevstep  + p >= k:
                return findmax(prevmaxx), findmin(prevmaxx)
            else:
                return findmax(prevminn), findmin(prevminn)

t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    answer = getresult(n,k)
    print("Case #"+str(i + 1)+": "+str(answer[0]) + " "+str(answer[1]))
