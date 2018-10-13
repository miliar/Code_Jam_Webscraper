# python 3.4 !!

#from functools import lru_cache
#@lru_cache(maxsize = None)

num_trials = int(input())

def compute():
    S, K = input().split()
    K = int(K)
    S = list(map(lambda x: 1 if x == '+' else 0, S))

    count = 0
    for i in range(0, len(S) - K + 1):
        if S[i] == 0:
            count += 1
            for j in range(0, K):
                S[i + j] = S[i + j] ^ 1 

    for i in range(len(S)-K+1, len(S)):
        if S[i] == 0:
            return "IMPOSSIBLE"

    return str(count)

for i in range (0, num_trials):
    print("Case #" + str(i+1) + ": " + compute())
