
def flipOne(c):
    if c == '+':
        return '-'
    if c == '-':
        return '+'
    raise Exception(c)


def flip(a, st, en):
    res = a[:st]
    for i in xrange(st, en):
        res = res + flipOne(a[i])
    if en != len(a):
        res += a[en:]
    return res

def solve(s, k):
    L = len(s)
    flip_count = 0
    for i in xrange(L-k+1):
        if s[i] == '-':
            s = flip(s, i, i+k)
            flip_count += 1
    if s.count('-') > 0:
        return 'IMPOSSIBLE'
    return flip_count


def main():
    T = int(raw_input())
    for i in xrange(1, T+1):
        s, t = raw_input().split()
        k = int(t)
        print('Case #{0}: {1}'.format(i, solve(s, k)))

main()
