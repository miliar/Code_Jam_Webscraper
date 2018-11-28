from math import ceil, floor

cases = int(input())

for case in range(0, cases):
    stalls, people = [int(x) for x in input().split(' ')]
    diff = stalls - people

    arr = [stalls]

    for x in range(people - 1):
        half = (max(arr) - 1) / 2
        arr.append(ceil(half))
        arr.append(floor(half))
        arr.remove(max(arr))
    L = ceil((max(arr) - 1) / 2)
    R = floor((max(arr) - 1) / 2)
    print('Case #{}: {} {} '.format(case + 1, L, R))