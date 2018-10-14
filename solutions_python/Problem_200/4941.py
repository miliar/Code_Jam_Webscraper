# Written by Nilushan Costa for Google Code Jam 2017 
# Problem B

T=int(input()) #Number of test cases
for testCaseNum in range (1,T+1):
    N=int(input()) # given N
    lastTidy=1
    for i in range (1,N+1):
        iStr=str(i)
        isTidy=True
        if (len(iStr)==1):
            lastTidy=i
            continue
        for index in range (0,len(iStr)-1):     #loop to check whether digits are in ascending order
            if (int(iStr[index])>int(iStr[index+1])):
                isTidy=False
                break
        if (isTidy):
            lastTidy=i
    print("Case #{}: {}".format(testCaseNum,lastTidy))
