import sys
import numpy as np

def greedy(Sin):
    S = map(int, list(Sin))
    #print("S=", S)
    i = 0
    while i < len(S)-1 and S[i+1] >= S[i]:
        i+=1
    if i == len(S)-1:
        return Sin
    for j in range(i+1, len(S)):
        S[j] = 9
    S[i] -= 1
    while i > 0 and S[i-1] > S[i]:
        S[i-1] -= 1
        S[i] = 9
        i -= 1
    if i == 0 and S[i] == 0:
        S.pop(0)
    return "".join(map(str, S))

T=int(sys.stdin.readline())
for t in range(1, T+1):
    S=sys.stdin.readline().strip()
    res = greedy(S)
    print "Case #"+str(t)+": "+res
