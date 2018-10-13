result = {}

rev = {'-': '+', '+': '-'}


def check(s):
    return all([c == '+' for c in s])


with open('A-large.in') as infile:
    t = int(infile.readline())

    for i in xrange(1, t + 1):
        S, k = infile.readline().split(' ')
        S = list(S)
        k = int(k)

        flip = 0

        if check(S):
            result[i] = 0
        else:
            for s in xrange(len(S) - k + 1):
                if S[s] == '-':
                    for j in xrange(k):
                        S[s + j] = rev[S[s + j]]
                    flip += 1
            if check(S):
                result[i] = flip
            else:
                result[i] = 'IMPOSSIBLE'

with open('A-large.out', 'w') as outFile:
    for i in result:
        outFile.write("Case #{}: {}\n".format(i, result[i]))
