

def solveCase(casenum):
    [price,rate,goal]=[float(e) for e in input().split()]
    return "Case #"+str(casenum)+": "+str(time(price,rate,goal))

def time(price,rate,goal):
    farms=0
    ans=0
    while(True):
        nofarm=goal/(2+farms*rate)
        farm=price/(2+farms*rate)+goal/(2+(farms+1)*rate)
        if nofarm<farm:
            return nofarm+ans
        else:
            ans=ans+price/(2+farms*rate)
            farms=farms+1




if __name__=="__main__":
    cases=int(input())
    for i in range(1,cases+1):
        print(solveCase(i))
