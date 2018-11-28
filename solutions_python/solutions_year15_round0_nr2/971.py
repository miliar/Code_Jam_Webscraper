from functools import lru_cache

@lru_cache(maxsize=None)
def compute(a):
    result = a[0]
    if result == 1:
        return 1
    b = list(a)[1:]
    for i in range(1, a[0]-1):
        result = min(result, compute(tuple(reversed(sorted(b+[i, a[0]-i]))))+1)
    return result

q = int(input())
for case in range(q):
    _ = input()
    a = [int(x) for x in input().split()]
    res = compute(tuple(reversed(sorted(a))))
    print('Case #{0}: {1}'.format(case+1, res))