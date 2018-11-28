from functools import lru_cache
from collections import Counter

t = int(input())


def problem():
    inp = input().split()
    n = int(inp[0])
    k = int(inp[1])
    level = len(bin(k)[3:])
    values = get_values_on_level(n, level+1)
    keys = sorted(values.keys(), key=lambda v: v[1], reverse=True)
    remainder = k - ((2**level)-1)
    for key in keys:
        count = values[key]
        if count >= remainder:
            return key
        else:
            remainder -= count


@lru_cache(maxsize=None)
def get_values_on_level(size2, level):
    l = size2 // 2
    if size2 % 2 == 0 and size2 != 0:
        r = (size2 // 2) - 1
    else:
        r = size2 // 2
    if level == 1:
        return {(l, r): 1}
    else:
        return Counter(get_values_on_level(l, level - 1)) + Counter(get_values_on_level(r, level - 1))


for i in range(1, t + 1):
    stats = problem()
    print("Case #{}: {} {}".format(i, stats[0], stats[1]))
