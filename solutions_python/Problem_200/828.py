def lastTidy(N):
    if N<10: return N
    pow10= 10**(len(str(N))-1)

    nextTidy= lastTidy(N%pow10)

    if N//pow10 <= nextTidy//(pow10//10):
        return N-(N%pow10)+ nextTidy
    else: return N-(N%pow10)-1

T= int(input())
for case in range(T):
    l= int(input())

    print("Case #"+str(case+1)+":", lastTidy(l))
