T = int(input())
for t in range(1,T+1):
    s, k = input().split()
    k = int(k)
    L = [0 if c == '-' else 1 for c in s]
    cnt = 0
    for i in range(len(L)-k+1):
        if not L[i]:
            for j in range(i, i+k):
                L[j] = (1,0)[L[j]]
            cnt += 1
    if all(L):
        print("Case #%d: %d" % (t,cnt))
    else:
        print("Case #%d: IMPOSSIBLE" % t)

        

