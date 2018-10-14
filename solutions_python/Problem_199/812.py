with open('in', 'r') as f:
    T = int(f.readline().strip())
    result = list()
    for n in range(T):
        S, K = f.readline().strip().split()
        K = int(K)
        S = list(S)
        l = len(S)
        i = 0
        moves = 0
        while i<l:
            if S[i] == '-':
                if i+K<=l:
                    for j in range(i,i+K):
                        if S[j] == '-':
                            S[j] = '+'
                        else:
                            S[j] = '-'
                    moves += 1
                else:
                    break
            i += 1
        if i==l:
            result.append('Case #' + str(n+1)+': '+str(moves)+'\n')
        else:
            result.append('Case #' + str(n+1)+': IMPOSSIBLE\n')

with open('out', 'w') as f:
    for case in result:
        f.write(case)
