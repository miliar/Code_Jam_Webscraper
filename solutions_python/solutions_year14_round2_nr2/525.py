T = int(raw_input())

template = "Case #{}: {}"


for i in xrange(1, T+1):
    A, B, K = map(int, raw_input().split())

    res = 0
    for a in xrange(A):
        for b in xrange(B):
            if a&b < K: res += 1

    print template.format(i, res)