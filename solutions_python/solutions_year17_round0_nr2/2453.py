N = int(input())
for cnt in range(N):
    s = input()
    K = list(map(int,s))    
    while True:
        loop_end = True
        for i in range(len(K)-1):
            if K[i] > K[i+1]:
                loop_end = False
                K[i]-=1
                for j in range(i+1, len(K)):
                    K[j] = 9
                break
        if loop_end:break
    ans = 0
    for v in K: ans = ans * 10 + v
    print("Case #%d: %d"%(cnt+1,ans))
