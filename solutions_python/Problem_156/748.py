from sys import setrecursionlimit

setrecursionlimit(10**8)

from functools import lru_cache

@lru_cache(maxsize=None)
def calculate(lst):
    if not lst:
        return 0
    cans = calculate(tuple(sorted(list(filter((lambda x: x > 0), map((lambda x: x-1), lst))))))
    if True:
        i = len(lst) - 1
        for j in range(1, lst[i] // 2 + 1):
            nlst = tuple(sorted(lst[:i] + (j, lst[i] - j) + lst[i+1:]))
            cans = min(cans, calculate(nlst))
    return cans + 1

@lru_cache(maxsize=None)
def stress(lst):
    if not lst:
        return 0
    cans = stress(tuple(sorted(list(filter((lambda x: x > 0), map((lambda x: x-1), lst))))))
    for i in range(len(lst)):
        if lst[i] <= 3:
            continue
        if i and lst[i] == lst[i-1]:
            continue
        i = len(lst) - 1
        for j in range(1, lst[i] // 2 + 1):
            nlst = tuple(sorted(lst[:i] + (j, lst[i] - j) + lst[i+1:]))
            cans = min(cans, stress(nlst))
    return cans + 1

#for t in (
#    (9,),
#    (9,9,9,9,9,9),
#    (1,2,3,4,5,6),
#    (9,8,7,7,7,7),
#):
#    print(calculate(t))

#exit() 
t = int(input())
for test in range(t):
    d = int(input())
    inp = tuple(sorted(list(map(int, input().split()))))
    print("Case #%d: %d" % (test+1, calculate(inp)))
