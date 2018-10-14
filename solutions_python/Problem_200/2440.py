# second problem about 2017 google code jam

def PRINT(case, value):
    print("Case #%d: %d" %(case+1, value))

def makeint(LN):
    stt1=''
    for i in range(len(LN)):
        stt1 += str(LN[i])

    itt = int(stt1)
    return itt


def makelist(N):
    stt=str(N)
    ML=[]
    for i in range(len(stt)):
        ML.append(int(stt[i]))
        #ML.append(stt[i])

    return ML

def isok(li):
    judge=False
    for i in range(len(li)-1):
        if li[i+1] < li[i]:
            return False
        else:
            judge=True
    return judge    
    
def search(num):
    listnum=makelist(num)
    while True:
        for i in range(1, len(listnum), 1):
            if listnum[i] < listnum[i-1]:
                listnum[i-1] = listnum[i-1]-1
                for j in range(i, len(listnum), 1):
                    listnum[j]=9
                break
        ok=isok(listnum)
        if ok==True:
            return listnum
 


def solve():
    Num = int(input())

    if Num < 10:
        return Num
    else:
        result = search(Num)
        intresult = makeint(result)
        
        return intresult
    


testcase = int(input())

for i in range(testcase):
    PR=solve()
    #for i in range(len(PR)):
    #    strRR =+ PR(i)
    #RR = int(strRR)
    PRINT(i, PR)
