import sys
sys.stdout = open('a_big.out', 'w')
sys.stdin  = open("a_big.in", 'r')
sys.setrecursionlimit(1500)
T = int(raw_input())

flip = {'+': '-', '-': '+'}

def good(S):
    for c in S:
        if c == '-':
            return False
    return True

def algorithm(S, K):
    if K > len(S):
        if good(S):
            return 0
        else:
            return -9999
    if S[0] == '+':
        return algorithm(S[1:], K)
    else:
        for i in range(K):
            S[i] = flip[S[i]]
        return 1 + algorithm(S[1:], K)


def solve():
    S, K = raw_input().split()
    K = int(K)

    ans = algorithm(list(S), K)
    if ans < 0:
        return "IMPOSSIBLE"
    return str(ans)

for i in range(1, T + 1):
    ans = solve()
    print "Case #" + str(i) + ": " + str(ans)