import math
PI = math.acos(-1.0)

T = int(raw_input())
for t in xrange(T):
    n, k = map(int, raw_input().split())
    l = [tuple(map(int, raw_input().split()) + [i]) for i in xrange(n)]  # (r, h)
    max_ans = 0
    for r_bottom, h_bottom, i in l:
        ll = sorted(filter(lambda x: x[0] <= r_bottom and x[2] != i, l), key=lambda x: -(x[0]*x[1]))
        ans = r_bottom ** 2 + 2 * sum(r * h for r, h, _ in ll[:k-1]) + 2 * r_bottom * h_bottom
        if max_ans < ans:
            max_ans = ans
    print 'Case #%s: %.9f' % (t+1, max_ans * PI)
