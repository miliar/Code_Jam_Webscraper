import heapq as h
import math

n = int(input())

i = 0
while i < n:
    i += 1

    heap = []

    num, k = [int(x) for x in input().split(' ')]

    h.heappush(heap, (-1)*num)

    while k > 0:
        k -= 1

        akt = (-1)*h.heappop(heap)

        a1 = math.floor(akt / 2)
        b = akt % 2

        a2 = a1 - 1 + b

        if a1 > 0:
            h.heappush(heap, (-1)*a1)
        if a2 > 0:
            h.heappush(heap, (-1)*a2)

    print("Case #" + str(i) + ": " + str(a1) + " " + str(a2))