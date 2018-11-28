def f(S,K):
    S = list(S)
    K = int(K)
    r = 0
    for i in range(len(S)-K+1):
        if S[i] == '-':
            r += 1
            for j in range(i, i+K):
                if S[j] == '-':
                    S[j] = '+'
                else:
                    S[j] = '-'
    if '-' not in S:
        return str(r)
    else:
        return 'IMPOSSIBLE'

fin = open('a2.in')
fout = open('a2.out', 'w')

T = int(fin.readline())

for t in range(T):
    [S,K] = fin.readline().split()
    fout.write('Case #%s: %s\n' % (t+1, f(S,K)))