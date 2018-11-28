T = int(input())
for loopC in range(T):
    S, K = input().split()
    K = int(K)
    def change(a):
        if a == '+':
            return 1
        else:
            return 0
    S = list(map(change,list(S)))
    
    result = 0

    for x in range(len(S)):
        try:
            if S[x] == 0:
                result = result+1
                for y in range(K):
                    S[x+y] ^= 1
        except Exception:
            result = "IMPOSSIBLE"

    print("Case #{}: {}".format(loopC+1,result))
    

