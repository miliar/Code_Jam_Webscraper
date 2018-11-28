import sys
import math

import heapq
def solve():
    N, K = map(int, sys.stdin.readline().rstrip().split())

    Rs = []
    for i in range(N):
        Ri, Hi = map(int, sys.stdin.readline().rstrip().split())
        Rs.append((Ri, Hi))

    Rs = sorted(Rs)

    most_area = 0
    h = []
    heapq.heapify(h)

    for i in range(K-1):
        radius, height = Rs[i]
        heapq.heappush(h, 2*radius*height)

    side_area = sum(h)

    for i in range(K-1, N):
        # Get area if ith pancake is our max
        radius, height = Rs[i]

        area = side_area + radius**2 + 2*radius*height

        if area > most_area:
            most_area = area

        heapq.heappush(h, 2*radius*height)
        removed = heapq.heappop(h)
        side_area += 2*radius*height
        side_area -= removed

    return most_area * math.pi


def main():
    T = int(sys.stdin.readline().rstrip())
    for t in range(1, T+1):
        print 'Case #{}: {:.8f}'.format(t, solve())

if __name__ == "__main__":
    main()
