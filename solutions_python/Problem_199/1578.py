fin = open('A.in', 'r')
fout = open('A.out', 'w')


def compute(s, k):
    P = list(s)
    num_flips = 0
    for i in range(len(P) - k + 1):
        if P[i] == '-':
            num_flips += 1
            # flip k pancakes
            for j in range(k):
                P[i+j] = '+' if P[i+j] == '-' else '-'
    # check that all pancakes are happy
    for i in range(len(P)):
        if P[i] == '-':
            return 'IMPOSSIBLE'
    return str(num_flips)


T = int(fin.readline())
for t in range(1, T+1):
    S, K = fin.readline().split()
    ans = compute(S, int(K))
    fout.write('Case #' + str(t) + ': ' + ans + '\n')
