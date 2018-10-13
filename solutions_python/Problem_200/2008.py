def solve(n):
    prev = 0
    i = 0
    while i < len(n):
        if n[i] < prev:
            # All digits after should be 9s.
            for j in xrange(i, len(n)): n[j] = 9
            # Subtract 1 from prev digit.
            n[i - 1] -= 1
            prev = n[i-2] if i-2 >= 0 else 0
            i -= 1
        else:
            prev, i = n[i], i + 1

    return reduce(lambda x,d: x * 10 + d, n, 0)


def tidy(n, last=9):
    if not n: return True
    if n[-1] > last: return False
    return tidy(n[:-1], n[-1])


if __name__ == '__main__':
    cases = int(raw_input())
    for case in xrange(cases):
        n = map(int, list(raw_input().strip()))
        soln = solve(n)

        print 'Case #%d: %s' % (case+1, soln)
