#!/usr/bin/env python2
import collections
for t in xrange(1, 1 + int(raw_input())):
    print 'Case #%d:' % t,
    N, P = map(int, raw_input().split())
    G = map(int, raw_input().split())
    count = collections.Counter([Gi % P for Gi in G])
    leftover_groups = sum(count.values())
    divisible_blocks = 0

    # 0 mod P
    divisible_blocks += count[0]
    leftover_groups -= count[0]
    count[0] = 0

    if P == 2:
        divisible_blocks += count[1] / 2
        leftover_groups -= count[1] / 2 * 2
        assert leftover_groups == count[1] % 2
        count[1] = 0
    elif P == 3:
        paired = min(count[1], count[2])
        divisible_blocks += paired
        leftover_groups -= paired * 2
        count[1] -= paired
        count[2] -= paired

        tripled = count[1] + count[2]
        divisible_blocks += tripled / 3
        leftover_groups -= tripled / 3 * 3
        assert leftover_groups == tripled % 3
        count[1] = count[2] = 0
    elif P == 4:
        paired = min(count[1], count[3])
        divisible_blocks += paired
        leftover_groups -= paired * 2
        count[1] -= paired
        count[3] -= paired

        remaining = count[1] + count[3]
        count[2] += remaining / 2
        count[1] %= 2
        count[3] %= 2
        leftover_groups -= remaining / 2 * 2
        leftover_groups += remaining / 2
        _leftover_from_pairing = remaining % 2
        count[1] = count[3] = 0

        divisible_blocks += count[2] / 2
        leftover_groups -= count[2] / 2 * 2
        count[2] %= 2
        assert leftover_groups == count[2] + _leftover_from_pairing
    else:
        assert False # XXX
    #assert sum(count.values()) == 0
    ans = divisible_blocks + (1 if leftover_groups > 0 else 0)
    print ans
