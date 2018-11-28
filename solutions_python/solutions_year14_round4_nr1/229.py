#!/usr/bin/env python3

def solve(xs, D):
    #print(D, ':', sorted(xs))
    disks = 0
    singles = []
    for x in sorted(xs, reverse=True):
        if singles and x + singles[-1] <= D:
            #print(x, "and", singles[-1], "go together")
            singles.pop()
            disks += 1
        else:
            singles.append(x)
    #print("remaining:", singles)
    assert all(x+y > D
               for x,y in __import__("itertools").combinations(singles, 2))
    return disks + len(singles)

tests = int(input())
for test in range(tests):
    N, D = map(int, input().split())
    S = list(map(int, input().split()))
    result = solve(S, D)
    print("Case #{}: {}".format(1+test, result))
