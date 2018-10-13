import math
import heapq

def solution():

    dbg = False

    #
    # N - number of stalls
    # K - people that enter
    N, K = input().split(" ")
    N, K = int(N), int(K)

    if dbg:
        print("***")
        print("***")
        print("N: " + str(N))
        print("K: " + str(K))

    h = [] # heap
    heapq.heappush(h, -1 * N)
    for i in range(K-1):
        n = -1 * heapq.heappop(h)
        if dbg: print("pop: " + str(n))

        if(n % 2 == 0):
            d = n // 2
            L = d-1
            H = d
            if(L > 0):
                heapq.heappush(h, -1 * L)
                if dbg: print(" L push: " + str(L))

            if(H > 0):
                heapq.heappush(h, -1 * H)
                if dbg: print(" H push: " + str(H))

        else:
            d = n // 2
            heapq.heappush(h, -1 * d)
            heapq.heappush(h, -1 * d)
            if dbg: print(" L push: " + str(d))
            if dbg: print(" H push: " + str(d))

    n = -1 * heapq.heappop(h)
    if dbg: print("pop: " + str(n))

    if(n % 2 == 0):
        d = n // 2
        L = d-1
        H = d
        if(L > 0):
            heapq.heappush(h, -1 * L)
            if dbg: print(" L push: " + str(L))

        if(H > 0):
            heapq.heappush(h, -1 * H)
            if dbg: print(" H push: " + str(H))

        return str(H) + " " + str(L)

    else:
        d = n // 2
        heapq.heappush(h, -1 * d)
        heapq.heappush(h, -1 * d)
        if dbg: print(" L push: " + str(d))
        if dbg: print(" H push: " + str(d))

        return str(d) + " " + str(d)

testcases = int(input())
for i in range(testcases):
    print("Case #" + str(i+1) + ": " + str(solution()))
