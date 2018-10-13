import sys

def flip(s):
    return s.replace('+', '*').replace('-', '+').replace('*', '-')

T = int(sys.stdin.readline())

for t in range(0, T):
    tokens = sys.stdin.readline().split()
    S = tokens[0]
    K = int(tokens[1])
    count = 0
    while len(S) >= K:
        if S[0] == '-':
            count += 1
            S = flip(S[:K]) + S[K:]
        S = S[1:]
#        print('%d %s' % (count, S))
    if '-' in S:
        print('Case #%d: IMPOSSIBLE' % (t+1))
    else:
        print('Case #%d: %d' % (t+1, count))

