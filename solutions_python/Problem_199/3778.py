import sys


T = int(raw_input())

for testCase in range(T):
    (S, K) = raw_input().split()
    K=int(K)

    lineup = [(i=='+') for i in S]
    flipped = 0
    for i in range(len(lineup) - K + 1):
        if all(lineup):
            break
        if not lineup[i]:
            flipped += 1
            for j in range(K):
                lineup[i+j] = not lineup[i+j]

    print "Case #{}: ".format(testCase + 1),
    if all(lineup):
        print flipped
    else:
        print "IMPOSSIBLE"
