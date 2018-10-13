def solve(n, k):
    stalls = list(i == 0 or i == n + 1 for i in xrange(n + 2))
    l_s = 0
    r_s = 0
    for i in xrange(k):
        best = -1
        longest_near = -1
        longest_far = -1
        l_s = 0
        r_s = 0
        for s in xrange(1, n + 1):
            if stalls[s]:
                continue
            l = 0
            while not stalls[s - l - 1]:
                l += 1
            r = 0
            while not stalls[s + r + 1]:
                r += 1
            if min(l, r) > longest_near:
                best = s
                longest_near = min(l, r)
                longest_far = max(l, r)
                l_s, r_s = l, r
            elif min(l, r) == longest_near and max(l, r) > longest_far:
                best = s
                longest_far = max(l, r)
                l_s, r_s = l, r
        stalls[best] = True
    return max(l_s, r_s), min(l_s, r_s)

t = int(raw_input())
for i in xrange(1, t + 1):
    n, k = (int(s) for s in raw_input().split())
    max_s, min_s = solve(n, k)
    print 'Case #{}: {} {}'.format(i, max_s, min_s)