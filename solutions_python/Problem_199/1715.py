# Daniel Balle 2017
#
# Oversized Pancake Flipper
# https://code.google.com/codejam/contest/3264486/dashboard


def greedy(s, k, i):
    # flip at position i if its not sunny

    if s[i] == '+': return False
    for j in range(k):
        s[i+j] = '+' if s[i+j] == '-' else '-'
    return True



T = int(raw_input().strip())
for t in range(1, T+1):

    _s, _k = raw_input().strip().split(' ')
    n, s, k = 0, list(_s), int(_k)

    for i in range(len(s) - k + 1):
        n += 1 if greedy(s, k, i) else 0

    fail = any( c == '-' for c in s )
    print "Case #{}: {}".format(t, "IMPOSSIBLE" if fail else n)
