import heapq

t = int(input())

for i in range(1, t + 1):
    n, k = [int(x) for x in input().split(" ")]

    stall_heap = []
    heapq.heappush(stall_heap, -n)

    max = 0
    min = 0

    while k > 0:
        k -= 1
        largest = -heapq.heappop(stall_heap)
        if largest == 2:
            max = 1
            min = 0
            # heapq.heappush(stall_heap, -1)
        elif largest > 2:
            if largest % 2 == 0:
                # it is even
                max = largest // 2
                min = (largest // 2 )- 1
                #heapq.heappush(stall_heap, - (largest / 2))
                #heapq.heappush(stall_heap,  - (( largest / 2 )- 1))
            else:
                #if it is odd
                largest -= 1
                max = min = (largest // 2)
                #heapq.heappush(stall_heap, - (largest / 2))
                #heapq.heappush(stall_heap, - (largest / 2))
        else:
            # last spot
            max = min = 0

        heapq.heappush(stall_heap, -max)
        if min is not 0:
            heapq.heappush(stall_heap, -min)

    print("Case #" + str(i) + ": " + str(max) + " " + str(min))