
T = int(raw_input())
for t in range(T):
    (A, B, K) = raw_input().strip().split()
    k = long(K)
    resp = sum([sum([(a & b) < k for b in range(long(B))]) for a in
        range(long(A))])
    print("Case #%d: %d" % ((t+1), resp))
