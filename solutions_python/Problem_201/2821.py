# use a heap, keep track of max and min

import heapq


def solve(n, k):

    pq = []

    heapq.heappush(pq, -n)
    for i in range(0, k):
        spot = -heapq.heappop(pq)-1

        new1 = spot // 2
        new2 = spot-new1
        heapq.heappush(pq, -new1)
        heapq.heappush(pq, -new2)

    return new2, new1


def main():

    t = int(input())
    for i in range(0, t):
        n, k = input().split()
        n = int(n)
        k = int(k)

        max_space, min_space = solve(n, k)
        print("Case #{}: {} {}".format(i+1, max_space, min_space))


if __name__ == "__main__":
    main()
