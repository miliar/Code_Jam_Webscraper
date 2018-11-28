N = input()

def solve():
    s = [int(c=="+") for c in S]
    p = 0
    cnt = 0
    while (p<=len(s)-K):
        while p<len(s) and s[p]:
            p+=1
        if (p>len(s)-K):
            break

        for i in range(K):
            s[p+i] ^= 1
        cnt+=1

    print "Case #%d: %s"%(n+1,str(cnt) if reduce(lambda a,b:a and b,s) else  "IMPOSSIBLE")
        
for n in range(N):
    S,K = raw_input().split(" ")
    K = int(K)
    solve()
