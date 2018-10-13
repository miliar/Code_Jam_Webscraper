import math

def check(r, h):
    return (r * r + (2 * r * h), (2 * r * h))

def height_surface(r, h):
    return 2 * math.pi * r * h

def optimize(k, pancakes):
    rh = sorted(pancakes, key=lambda e: e[0] * e[1], reverse=True)
    return rh[:k]

def surface(sorted_cakes):
    r = sorted_cakes[0][0]
    horizontal = r * r
    vertical = 0
    for cake in sorted_cakes:
        vertical += cake[0] * cake[1]

    return math.pi * (horizontal + 2 * vertical)


def f(n, k, pancakes):
    pancakes = sorted(pancakes, key=lambda e: (e[0], e[1]), reverse=True)

    # print '===='
    # for r, h in pancakes:
    #     print check(r, h), (r, h)
    # print '===='

    opt = optimize(k, pancakes)
    best_by_rh = sorted(opt, key=lambda e: e[0], reverse=True)

    # print best_by_rh

    baser, baseh = best_by_rh[0]
    worstr, worsth = opt[-1]
    worst_marg = worstr * worsth * 2

    i = 0
    best_idx = -1
    best_marg_gain = -1
    while pancakes[i][0] > baser: #while there are bigger R pancakes to consider..
        # see if it's better to use the bigger R
        br, bh = pancakes[i]
        marg_gain = ((br * br) - (baser * baser)) + (2 * br * bh) #marginal gain from adding this one
        if marg_gain > worst_marg and marg_gain > best_marg_gain:
            best_idx = i
            best_marg_gain = marg_gain
        i += 1

    if best_idx != -1:

        opt = [pancakes[best_idx]] + opt[:-1]
        # print 'replace', pancakes[best_idx], sorted(opt, key=lambda e: e[0], reverse=True)
    # print opt

    return surface(sorted(opt, key=lambda e: e[0], reverse=True))







# print f(2, 1, [(200, 10), (100, 20)])

t = int(raw_input())
for i in xrange(1, t+1):
    n, k = [int(x) for x in raw_input().split(' ')]
    pancakes = []
    for j in xrange(n):
        r, h = [int(x) for x in raw_input().split(' ')]
        pancakes.append((r, h))
    print 'Case #{}: {}'.format(i, f(n, k, pancakes))
