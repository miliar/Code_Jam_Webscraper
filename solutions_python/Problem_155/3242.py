T = int(input())
for t in range(T):
    Sm, S = input().split()

    pS = [int(S[0])]
    for k in S[1:]:
        pS += [pS[-1] + int(k)]
    res = 0
    for i in range(1,len(S)):
        if S[i]!=0:
            res += max(i-pS[i-1]-res,0)
    print("Case #%d:"%(t+1),res)

