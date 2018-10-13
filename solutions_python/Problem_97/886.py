T = int(input())
for t in range(T):
    A, B = map(int,input().split())
    N = len(str(A))
    res = 0
    for n in range(A,B):
        ns = str(n)
        for m in set(int(ns[i:]+ns[:i]) for i in range(N)):
            if n < m <= B:
                res += 1
    print ("Case #%d: %d" % (t+1, res))
