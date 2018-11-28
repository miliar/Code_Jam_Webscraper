#/usr/python3


def is_done(S):
    return len(list(filter(None, S))) == len(S)

def do_flip(S, K, I):
    for i in range(I, I+K):
        S[i] = not S[i]

def do_flips(S, K, flips):
    S = S[:]
    for i in range(len(flips)):
        if flips[i]:
            do_flip(S, K, i)
    return S

def get_flips(N, X):
    if X == N:
        yield [True]*X
        return
    if N == 0:
        yield [False]*X
        return
    for x in range(X-N+1):
        base = [False]*x+[True]
        for flips in get_flips(N-1, X-x-1):
            yield base + flips


T = int(input())

for t in range(T):
    
    S, K = input().split()
    S = [x == "+" for x in S]
    K = int(K)
    
    for x in range(0, len(S)-K+2):
        for flip in get_flips(x, len(S)-K+1):
            if is_done(do_flips(S, K, flip)):
                print("Case #{0}: {1}".format(t+1, x))
                break
        else:
            continue
        break
    else:
        print("Case #{0}: IMPOSSIBLE".format(t+1))


