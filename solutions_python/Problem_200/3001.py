def solve(n):
    l = 1
    while l < len(n) and n[l] >= n[l-1]:
        l += 1
    if l == len(n) or len(n) == 1:
        return n
    l -= 1
    while l > 0 and n[l] == n[l-1]:
        l -= 1
    m = int(n[l]) - 1 if len(n) > 1 else int(n[l])
    return "{}{}{}".format(
        n[:l],
        m if m > 0 else '',
        ''.join(['9']*(len(n) - l - 1))
    )
tests = int(raw_input())
for test in xrange(tests):
    n = raw_input()
    print "Case #{}: {}".format(test+1, solve(n))
