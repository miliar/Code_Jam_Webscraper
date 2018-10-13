T = int(input())
for case in range(1,T+1):
    N,X = (int(x) for x in input().split())
    ms = [int(x) for x in input().split()]
    ms.sort()
    i,j = 0,N-1
    ans = 0
    while len(ms)>1:
        x = ms.pop()
        y = ms[0]
        if x+y <= X:
            del ms[0:1]
        ans+= 1
    if ms:
        ans += 1
            
            

    print("Case #",case,": ",ans,sep = '')
