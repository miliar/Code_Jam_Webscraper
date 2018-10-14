import sys
name = "C-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")
testCases = int(input())

def iteration_num(k):
    ans=0
    n=1
    while True:
        k=k-n
        if k<=0:
            break
        else:
            ans+=1
            n=n*2
    return ans

def counts(n, iter_num):
    ans={}
    ans['odd']=(0, 0)
    ans['even']=(0, 0)

    if iter_num==0:
        if n%2==1:
            ans['odd']=(n, 1)
        else:
            ans['even']=(n, 1)
    else:
        x=counts(n, iter_num-1)
        amax=(max(0, (x['odd'][0]-1)//2), x['odd'][1])
        amin=(max(0, (x['odd'][0]-1)//2), x['odd'][1])
        bmax=((x['even'][0])//2, x['even'][1])
        bmin=(max(0, x['even'][0]//2-1), x['even'][1])

        odds=[]
        evens=[]

        for i in [amax, amin, bmax, bmin]:
            if i[0]%2==1:
                odds.append(i)
            elif i[0]==0:
                continue
            else:
                evens.append(i)
        totodds=0
        totevens=0
        for i in odds:
            totodds+=i[1]
        for i in evens:
            totevens+=i[1]
        if totodds>0:
            ans['odd']=(odds[0][0], totodds)
        if totevens>0:
            ans['even']=(evens[0][0], totevens)
    return ans

for testCase in range(1, testCases + 1):
    N, K = map(int, input().strip().split())
    k=iteration_num(K)
    rem=K-2**k+1
    val=counts(N, k)
    if val['odd'][0] >= val['even'][0]:
        maxset=val['odd']
        minset=val['even']
    else:
        maxset=val['even']
        minset=val['odd']
    if maxset[1]>=rem:
        n=maxset[0]
        if n%2==1:
            amax = max(0, (n - 1) // 2)
            amin = max(0, (n - 1) // 2)
            print('Case #%s: %s %s' % (testCase, amax, amin))
        else:
            bmax=n//2
            bmin=max(0, n//2-1)
            print('Case #%s: %s %s' % (testCase, bmax, bmin))
    else:
        n=minset[0]
        if n%2==1:
            amax = max(0, (n - 1) // 2)
            amin = max(0, (n - 1) // 2)
            print('Case #%s: %s %s' % (testCase, amax, amin))
        else:
            bmax=n//2
            bmin=max(0, n//2-1)
            print('Case #%s: %s %s' % (testCase, bmax, bmin))
