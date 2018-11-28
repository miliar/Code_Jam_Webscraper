from queue import PriorityQueue

T = int(input())

for i in range(1, T+1):
    S, K = input().split()
    S = list(S)
    K = int(K)

    count = 0

    for j in range(len(S)-K+1):
        if S[j] == '-':
            count += 1
            for k in range(K):
                if S[j+k] == '-':
                    S[j+k] = '+'
                else:
                    S[j+k] = '-'

    print('Case #%d: ' % i, end='')
    if '-' in S:
        print('IMPOSSIBLE')
    else:
        print(count)
