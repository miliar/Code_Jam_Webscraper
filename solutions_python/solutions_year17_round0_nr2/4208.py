def isStare(N):
    if N==0:
        return True
    a = (N/10)%10
    b = N%10
    if a>b:
        return False
    else:
        return isStare(N/10)
T = input()
result = []
pre = 10
for i in range(T):
    N = input()
    k = N
    for j in range(k,-1,-1):
        if (N%10)==0:
            N=N-1
        if isStare(N) is True:
            result.append(N)
            break
        else:
            N=N-1
for i in range(len(result)):
    print 'Case #%d: %d' %(i+1,result[i])
