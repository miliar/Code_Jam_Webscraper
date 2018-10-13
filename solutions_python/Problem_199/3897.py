def rank(s):
    return sum([2 ** i for (i, j) in enumerate(s) if j == '+'])


def flip(o, s, k):
    for i in xrange(k):
        s[o + i] = {'+': '-', '-': '+'}[s[o + i]]


def solv(s, k):
    memo = [None] * (rank(['+'] * len(s)) + 1)

    def rec(s, f):
        r = rank(s)
        if memo[r] is None or memo[r] > f:
            memo[r] = f
            for i in xrange(len(s) - k + 1):
                flip(i, s, k)
                rec(s, f + 1)
                flip(i, s, k)
    rec(s, 0)
    return memo

# def main():
t = int(raw_input())
for i in xrange(1, t + 1):
    line = raw_input().split(' ')
    k = int(line[1])
    s = list(line[0])
    res = solv(s, k)[-1]
    print "Case #%d: %s"%(i, str(res) if res > -1 else 'IMPOSSIBLE')

# print solv(list('---+'), 3)[15]
# print solv(list('---+-++-'), 3)[255]
# print solv(list('+++++'), 4)[31]
# print solv(list('-+-+-'), 4)[31]
# print solv(list('-+-+-'), 3)[31]
# print solv(list('+'), 1)[1]
