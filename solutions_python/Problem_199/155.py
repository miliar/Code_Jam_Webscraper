def flip(s):
    if s == '+':
        return '-'
    else:
        return '+'

def solve():
    S, K = raw_input().strip().split()
    K = int(K)
    S = list(S)
    n = len(S)

    count = 0
    for i in xrange(n):
        if S[i] == '-':
            if i+K > n:
                return "IMPOSSIBLE"

            for j in xrange(i, i+K):
                S[j] = flip(S[j])
            count += 1

    return count

for case in xrange(int(input())):
    print 'Case #%d: %s' % (case+1, solve())
