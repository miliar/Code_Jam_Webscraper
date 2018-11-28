import sys
from collections import defaultdict

cache = {}
def bestvalue(nums, val1, val2, i, lxor, rxor):
    key = (i, val1, val2, lxor, rxor)
    if key not in cache:
        if i >= len(nums):
            if (lxor == rxor) and (val1 > 0) and (val2 > 0):
                cache[key] = max(val1, val2)
            else:
                cache[key] = 0
        else:
            cache[key] = max(
              bestvalue(nums, val1 + nums[i], val2, i+1, lxor ^ nums[i], rxor),
              bestvalue(nums, val1, val2 + nums[i], i+1, lxor, rxor ^ nums[i])
            )
    return cache[key]
        

n = int(input())
for case in range(1, n+1):
    best = "NO"

    N = int(input())
    numbers = list(map(int, input().split()))

    cache = {}
    best = bestvalue(numbers, 0, 0, 0, 0, 0) 
    if best <= 0:
        best = "NO"

    print("Case #" + str(case) + ": " + str(best))
