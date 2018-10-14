def calc(K):
    S = [int(k) for k in str(K)]
    for i in range(len(S) - 1):
        if S[i] > S[i+1]:
            if S[i] == 1:
                return '9'*(len(S)-1)
            else:
                first, dig = i, S[i]
                if i > 0:
                    for j in range(i-1, -1, -1):
                        if S[j] != dig:
                            break
                        first = j
                S[first]-= 1
                l = len(S[first+1:])
                S[first + 1:] = [9]*l
                return ''.join(map(str,S))
    return K

def inp(infile, outfile):
    with open(infile) as f, open(outfile, 'w') as g:
        T = int(f.readline())

        for i, _ in enumerate(range(T)):
            K = int(f.readline())
            result = calc(K)
            print('Case #{}: {}'.format(i+1, result), file=g)

inp('/Users/Shmu/PycharmProjects/codejam_17/b_large.txt',
    '/Users/Shmu/PycharmProjects/codejam_17/b_large3.txt')