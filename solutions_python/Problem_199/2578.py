
import sys

def get_minimum_flip_time(S, K):
    if len(set(S)) == 1 and set(S).pop() == '+':
        return 0
    if len(S) < K:
        return "IMPOSSIBLE"
    if '-' in S and S.index('-') > 0:
        return get_minimum_flip_time(S[S.index('-'):], K)
    for i in xrange(K):
        S[i] = '-' if S[i] == '+' else '+'
    if '-' in S:
        flip_times = get_minimum_flip_time(S[S.index('-'):], K)
    else:
        flip_times = 0
    if flip_times == "IMPOSSIBLE":
        return "IMPOSSIBLE"
    else:
        return 1 + flip_times

sys.setrecursionlimit(1500)
T = int(raw_input()) # read a line with a single integer
for i in xrange(1, T + 1):
    S, K = raw_input().split(" ")
    S = list(S)
    K = int(K)
    print "Case #{}: {}".format(i, get_minimum_flip_time(S, K))