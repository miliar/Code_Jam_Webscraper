def flipHelper(S, K, n):
    pass

def happy(S):
    return S == len(S) * '+'

def numFlips(S, K):
    if happy(S):
        return 0
    elif len(S) < K:
        return 'IMPOSSIBLE'
    else:
        if S[0] == '+':
            return numFlips(S[1:], K)
        flipN = numFlips(flip(S, K, 0)[1:], K)
        if flipN == 'IMPOSSIBLE':
            return flipN
        return 1 + flipN
        #flips = [numFlips(flip(S, K, x)[1:], K) for x in range(0, len(S)-K)]
        #if flips == len(flips)*['IMPOSSIBLE']:
        #    return 'IMPOSSIBLE'
        #return 1 + min(flips)

def flip(S, K, index):
    return S[0:index] + ''.join(['-' if x == '+' else '+' for x in S[index:K]]) + S[index+K:]


if __name__ == "__main__":
    fname = 'A-small-attempt0.in'
    with open(fname) as f:
        content = f.readlines()
        numTests = int(content[0])
        i = 1
        for test in content[1:]:
            s, k = test.split()
            result = numFlips(s, int(k))
            print 'Case #%d: %s' % (i, result)
            i += 1
