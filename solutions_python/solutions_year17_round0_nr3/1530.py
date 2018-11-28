import math

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    level = int(math.floor(math.log(k, 2)))
    occupied_until_this_level = 2**level - 1
    will_be_occupied_this_level = 2**level
    stalls_left = n - occupied_until_this_level
    mod = stalls_left % will_be_occupied_this_level
    tot = 0
    if 2**(level) - 1 + mod < k:
        tot = int(math.floor(stalls_left / will_be_occupied_this_level))
    else:
        tot = int(math.ceil(stalls_left / will_be_occupied_this_level))

    tot -= 1
    min_val = tot // 2
    max_val = tot - min_val
    print('Case #%d: %d %d' % (i + 1, max_val, min_val))
