import sys

def dbg(s): sys.stderr.write(str(s) + "\n")
#def dbg(s): None
def reads(t): return list(map(t, input().split(" ")))
def read(t): return t(input())


T = read(int)

for t in range(1, T+1):
    [A, B, K] = reads(int)

    s = A * B 
    if A > K and B > K:
        s -= (A-K) * (B-K)

    for i in range(K, A):
        for j in range(K, B):
            if i & j < K:
                s += 1

    print("Case #%d: %s" % (t, s))
