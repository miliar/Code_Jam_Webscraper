def calc(S,K):
    flips = 0
    for i in range(len(S)):
        if S[i] == '-' and len(S) - i >= K:
            flips += 1
            change = ''
            for j in range(i, i+K):
                if S[j] == '-':
                    change += '+'
                else:
                    change += '-'
            S = S[:i] + change + S[i+K:]
    if all(s == '+' for s in S):
        return flips
    else: return 'IMPOSSIBLE'

def inp(infile, outfile):
    with open(infile) as f, open(outfile, 'w') as g:
        T = int(f.readline())

        for i, _ in enumerate(range(T)):
            S, K = [x for x in f.readline().split()]
            K = int(K)

            result = calc(S, K)

            print('Case #{}: {}'.format(i+1, result), file=g)

inp('/Users/Shmu/PycharmProjects/codejam_17/a_large.txt',
    '/Users/Shmu/PycharmProjects/codejam_17/pan_tes2.txt')