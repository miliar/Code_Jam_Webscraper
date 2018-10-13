def t3(N, K):
    assert N >= K
    def inner(K):
        k_half = K // 2
        if K % 2 == 1:
            return {k_half: 2}
        else:
            return {k_half: 1, k_half - 1: 1}

    run_map = {N: 1}

    while K > 0:
        k = max(run_map.keys())
        old_mult = run_map[k]
        for new_width, mult in inner(k).items():
            if (new_width != 0):
                if (new_width in run_map):
                    run_map[new_width] += old_mult * mult
                else:
                    run_map[new_width] = old_mult * mult
        del run_map[k]
        K -= old_mult
    return inner(k)


def solve2(N, K):
    d = t3(N, K)
    keys = sorted(d.keys(), reverse=True)
    if len(keys) == 1:
        return keys[0], keys[0]
    else:
        return keys

if __name__ == '__main__':
    for qq in xrange(1, int(raw_input())+1):
        N, K = map(int, raw_input().split())
        h, l = solve2(N, K)
        print 'Case #{}: {} {}'.format(qq, h, l)
