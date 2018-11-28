def timecalc(c, f, x):
        allTimes=[]
        rate=2
        timeElapsed=0
        i=0
        while True:
            timewin=x/rate + timeElapsed
            timeElapsed=timeElapsed+c/rate
            allTimes.append(timewin)
            rate+=f
            if i>0:
                if allTimes[i-1]<=allTimes[i]:
                    return allTimes[i-1]
            i+=1
        return min(allTimes)

t=int(input())
for i in range(t):
    inp=list(map(float, input().split()))
    ans=timecalc(inp[0], inp[1], inp[2])
    print('Case #{0}: {1:7f}'.format(i+1, round(ans, 7)))