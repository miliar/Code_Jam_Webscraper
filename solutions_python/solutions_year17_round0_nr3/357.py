#!/usr/bin/env python3

def split_stalls(n):
    furthest = n // 2
    closest = n - furthest - 1
    return (furthest, closest)

def high_low(high, last_h, last_l):
    new_high = high // 2

    # For the high ones
    (h, l) = (0, 0)
    if high == 2*new_high+1:
        h+= 2 * last_h
    elif high == 2*new_high:
        h += 1 * last_h 
        l += 1 * last_h
    elif high == 2*new_high-2+1:
        l += 2 * last_h
    elif high == new_high:
        l += 1 * last_h

    # For the low ones
    if high-1 == 2*new_high:
        h += 1 * last_l
        l += 1 * last_l
    elif high-1 == 2*new_high-2+1:
        l += 2 * last_l
    elif high-1 == new_high:
        l += 1 * last_l

    return (h, l)

def solve(n, k):
    high = n
    (h, l) = (1, 0)

    while high > 0:
        if k <= h:
            return split_stalls(high)
        elif k <= h+l:
            return split_stalls(high-1)
        else:
            k -= h+l
        (h, l) = high_low(high, h, l)
        high //= 2

    return ("danger", "panic")

for i in range(int(input().strip())):
    [n, k] = map(int, input().strip().split())
    print("Case #{}: {} {}".format(*((i+1,) + solve(n, k))))
