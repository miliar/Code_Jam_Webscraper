def executeProgram():
    [d,n] = input().split()
    d = int(d)  #dist to house
    n = int(n)  #n other horses
    i=0
    horsearr = []
    while(i<n):
        [k, s] = input().split()
        k = int(k)  #initial pos
        s = int(s)  #speed
        horsearr.append([k,s])
        i+=1
    i=0
    maxTime = 0
    while i<n:
        time = (d-horsearr[i][0])/horsearr[i][1]
        if(time > maxTime):
            maxTime = time
        i+=1
    ans = d/maxTime
    return ans

t = int(input())
i = 1
while t > 0:
    ans = executeProgram()
    print('Case #' + str(i) + ': ' + '{0:.6f}'.format(ans))
    i+=1
    t-=1
