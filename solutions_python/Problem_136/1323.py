def solve():
    farm_cost, farm_revenue, goal = map(float, raw_input().split())

    res = goal / 2.0
    cur_sum = 0
    for k in xrange(0, int(goal) + 2):
        cur_sum += 1.0 / (2.0 + k * farm_revenue)
        res = min(res, farm_cost * cur_sum + goal / (2 + (k + 1) * farm_revenue ))
    return res

T = int(raw_input())
for t in xrange(0, T):
    print 'Case #%d: %.7f' % (t + 1, solve())
