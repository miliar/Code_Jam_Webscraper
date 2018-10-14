
def solve():
    import math
    f=open("A-large.in")
    f2=open("output.txt",'w')
    lines=f.readlines()
    t=int(lines[0])
    current=1
    # t=input()
    for test in xrange(1,t+1):
        n,k=map(int,lines[current].split())
        current+=1
        # n,k=map(int,raw_input().split())
        pancakes=[]
        for x in xrange(n):
            # ri,hi=map(int,raw_input().split())
            ri,hi=map(int,lines[current].split())
            current+=1
            pancakes.append((math.pi*(ri**2),2*math.pi*ri*hi))
        pancakes.sort(key= lambda x:x[0],reverse=True)
        # print pancakes
        dp=[]
        for x in xrange(n-1):
            p=[]
            for y in xrange(n+1):
                p.append([0,0])
            dp.append(p)
        dp.append([[0,0],[pancakes[-1   ][-1],pancakes[-1][-1]]]+[[0,0]]*(n-1))
        for x in xrange(n-2,-1,-1):
            for y in xrange(1,n-x+1):
                dp[x][y][0]=dp[x+1][y-1][1]+pancakes[x][1]
                dp[x][y][1]=max(dp[x+1][y][1],dp[x][y][0])
        # print dp
        ans=0
        for i in xrange(n):
            ans=max(dp[i][k][0]+pancakes[i][0],ans)
        # print "%.7f"%ans
        f2.write("Case #{}: {}\n".format(test,"%.7f"%ans))
    f2.close()
    f.close()
solve()
