import math
from decimal import *

getcontext().prec = 100

t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    arr = []
    for i in range(n):
        r, h = map(Decimal, input().split())
        arr.append([r, h])

    arr.sort(reverse=True)

    dpi = Decimal(math.pi)
    maxi = Decimal(0)
    for i in range(n):
        area = dpi * arr[i][0] * arr[i][0] + 2 * dpi * arr[i][0] * arr[i][1]
        arr2 = [2 * dpi * arr[j][0] * arr[j][1] for j in range(i + 1, n)]
        arr2.sort(reverse=True)
        area += sum(arr2[:k - 1])
        if maxi < area:
            maxi = area

    print("Case #{}: {}".format(tc + 1, maxi))