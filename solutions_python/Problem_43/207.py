n_cases = int(raw_input())

for i in xrange(n_cases):
    inp = raw_input()
    base = max([2, len(set(inp))])

    possible = range(base)

    digits = {
        inp[0]: 1,
    }
    if 1 in possible:
        possible.remove(1)
    value = base ** (len(inp) - 1)
    ans = 0
    for c in inp:
        if c not in digits:
            digits[c] = possible.pop(0)
        ans += digits[c] * value
        value /= base

    print "Case #%d: %d" % (i + 1, ans)

