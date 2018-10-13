def isTidy(n):
    l=list(map(int, str(n)) )
    if all(l[i] <= l[i+1] for i in range(len(l)-1)):
        return True
    else:
        return False
T=int(input())
for s in range(1,T+1):
    a=int(input())
    last=1
    for i in range(1,a+1):
        if isTidy(i):
            last=i
    print("Case #"+str(s)+": "+str(last))
