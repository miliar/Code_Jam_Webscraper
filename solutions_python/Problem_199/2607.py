with open('input.in', 'r') as fin:
    with open('output.out', 'w') as fout:
        T = int(fin.readline())
        for i in range(T):
            S, K = fin.readline().split()
            S = list(S)
            K = int(K)
            flips = 0
            for j in range(len(S) - K + 1):
                if S[j] == '-':
                    for k in range(j, j + K):
                        if S[k] == '-':
                            S[k] = '+'
                        else:
                            S[k] = '-'
                    flips += 1
            if S != list('+' * len(S)):
                fout.write('Case #%d: IMPOSSIBLE\n' % (i + 1))
            else:
                fout.write('Case #%d: %d\n' % (i + 1, flips))
