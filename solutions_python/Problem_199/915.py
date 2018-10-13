def index_of_last_minus(s):
    return s.rfind("-")


def flip(s, k, last_index):
    s = list(s)
    for i in xrange(last_index - k + 1, last_index + 1):
        if '+' == s[i]:
            s[i] = '-'
        elif '-' == s[i]:
            s[i] = '+'
    return "".join(s)


def solve(s, k, res):
    k = int(k)
    i = index_of_last_minus(s)
    if -1 == i:
        return res
    if i + 1 < k:
        return "IMPOSSIBLE"
    s = flip(s, k, i)
    return solve(s, k, res + 1)

t = int(raw_input())

for i in xrange(1, t+1):
    s, k = raw_input().split()
    print "Case #{}: {}".format(i, solve(s, k, 0))