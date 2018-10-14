from sys import stdin, stdout
import math

def min(S, K):
    if len(S) <= K:
        cnt = 0
        for i in range(len(S)):
            letter = S[i]
            if letter == '-':
                cnt += 1


        if cnt == 0:
            return 0
        elif cnt == K:
            return 1
        else:
            return float('-inf')

    if S[0] == '+':
        return min(S[1:], K)
    else:
        for i in range((K)):
            S[i] = '+' if S[i] == '-' else '-'

        return 1 + min(S[1:], K)




T = stdin.readline()
T = int(T)

lines = stdin.readlines()

cnt = 1
for line in lines:
    S, K = line.rstrip().split()
    K = int(K)
    S = list(S)

    result = min(S, K)
    answer = 'IMPOSSIBLE' if result < 0 else result
    print 'Case #' + str(cnt) + ': ' + str(answer)
    cnt += 1
