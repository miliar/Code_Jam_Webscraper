import sys

def main(n, k):
    assert(k <= n and k > 0)
    if k == 1: return (n // 2, (n - 1) // 2)
    else:
        if k % 2 == 1: return main((n - 1) // 2, k // 2)
        else: return main(n // 2, k // 2)

t = int(input())
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    y, z = main(n, k)
    print("Case #{}: {} {}".format(i, y, z))

