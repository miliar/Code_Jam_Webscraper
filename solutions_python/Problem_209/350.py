from __future__ import absolute_import, division, print_function
import math
from collections import defaultdict


def solve(pancakes, k):
    areas = {}
    tops = {}
    highs = {}
    biggest_top = -1
    biggest_top_key = -1
    for i, p in enumerate(pancakes):

        top = math.pi * p[0] * p[0]
        high = p[0] * p[1] * 2 * math.pi
        area = top + high
        areas[i] = area
        tops[i] = top
        highs[i] = high
        if top > biggest_top:
            biggest_top = top
            biggest_top_key = i

    count = 0
    ps_to_use = []
    # what if same area?
    inv_high = defaultdict(list)
    for key, value in highs.items():
        inv_high[value].append(key)

    for ia in sorted(inv_high, reverse=True):
        if len(inv_high[ia]) + count <= k:
            for key in inv_high[ia]:
                ps_to_use.append(key)
            count += len(inv_high[ia])
            if k == count:
                break
        else:
            #shit several same area

            # check while loop is ok
            while count < k:
                biggest_top2 = -1
                biggest_top_key2 = -1
                # top -> highs
                for key in inv_high[ia]:
                    top2 = tops[key]
                    if top2 > biggest_top2 and key not in ps_to_use:
                        biggest_top2 = top2
                        biggest_top_key2 = key

                ps_to_use.append(biggest_top_key2)
                count += 1
            break

    total = 0

    for key in ps_to_use:
        total += highs[key]

    biggest = -1
    big_index = -1
    for key in ps_to_use:
        if tops[key] > biggest:
            biggest = tops[key]
            big_index = key

    total += tops[big_index]
    # Now we have the area with the most surface area.

    # but we must still swap the smallest with the widest to see if we can improve total volume
    if biggest_top_key not in ps_to_use:
        shortest_pancake_in_stack = ps_to_use[0]
        shortest_height = highs[ps_to_use[0]]
        for p in ps_to_use:
            if shortest_height > highs[p]:
                shortest_height = highs[p]
                shortest_pancake_in_stack = p

        total2 = total
        total2 -= tops[big_index]
        total2 += tops[biggest_top_key]
        total2 += highs[biggest_top_key]
        total2 -= highs[shortest_pancake_in_stack]

        total = max(total, total2)

    return total




#with open('sample.in') as f:
#with open('A-small-attempt2.in') as f:
with open('A-large.in') as f:
    T = int(f.readline())

    for puzzle_count in range(T):
        n, k = map(int, f.readline().strip().split(' '))
        slowest = 0

        pancakes = []
        for i in range(0, n):
            raw = f.readline().strip().split(' ')
            r, h = map(int, raw)
            pancakes.append((r, h))

        ans = solve(pancakes, k)

        print('Case #%s: %f' % (str(puzzle_count + 1), ans))

