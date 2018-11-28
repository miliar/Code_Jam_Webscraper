import sys

def walk(mem, case, val, n, K, M):
    k = K << n
    if k > M:
        return
    c1 = case ^ k
    if mem.get(c1, val+2) <= val + 1:
        return
    mem[c1] = val + 1
    walk(mem, c1, val+1, 0, K, M)
    walk(mem, case, val, n+1, K, M)


for C in range(1, int(sys.stdin.readline())+1):
    answer = "IMPOSSIBLE"
    b, K = sys.stdin.readline().strip().split()
    N = 0
    S = len(b)
    K = int(K)
    M = 2**S-1
    k = 2**K-1
    # print M, b, S, K
    for p in range(S):
        if b[p] == "+":
            N += 2**p
    c = 0
    # print b, K
    for p in range(S-K+1):
        if N & (2**p) == 0:
            N ^= k << p
            c += 1
            t = ""
            for o in range(S):
                t += "+" if N & (2**o) else "-"
            # print t
        if N == M:
            answer = c
            break
    """        
    mem = {M: 0}
    walk(mem, M, 0, 0, k, M)
    if N in mem:
        answer = mem[N]
    """
    print "Case #%s: %s" % (C, answer)
