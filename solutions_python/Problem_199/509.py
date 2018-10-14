import sys
from collections import defaultdict

def run(S, K):
    count = 0

    S = [-1 if s == '-' else 1 for s in S]

    for i in range(len(S)-K+1):
        if S[i] == -1:
            for j in range(i,i+K):
                S[j] *= -1
            count += 1
    for i in range(len(S)-K, len(S)):
        if S[i] == -1:
            return 'IMPOSSIBLE'
    return count


f = file(sys.argv[1],'r')
T = int(f.readline().strip())
for case in range(1,T+1):
    S,K = f.readline().strip().split()
    ans = run(list(S),int(K))
    print 'Case #%d: %s' % (case, ans)
