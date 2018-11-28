def flip(S, K, i):
    if i + K > len(S):
        return False
    for j in xrange(i, i + K):
        if S[j] == '-':
            S[j] = '+'
        else:
            S[j] = '-'
    return True


def sol(S, K):
    count = 0
    for i in xrange(0, len(S)):
        if S[i] == '+':
            continue
        else:
            if flip(S, K, i):
                count += 1
                continue
            else:
                return "IMPOSSIBLE"
    return str(count)


t = long(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    line = raw_input()
    S, K = line.split()
    S = map(lambda x: x, S)
    K = int(K)
    print "Case #{}: {}".format(i, sol(S, K))
