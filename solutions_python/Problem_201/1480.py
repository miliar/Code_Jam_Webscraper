import sys
import heapq


def solve(line):
    line = line.split(' ')
    N, K = int(line[0]), int(line[1])
    print >> sys.stderr, N, K

    if N > 50000 and 1.1*K > N:
        return 0,0

    # (-size, -position)
    openings = []
    heapq.heappush(openings, (-N, 0))

    for i in range(K):
        next = heapq.heappop(openings)
        size = - next[0]
        position = -next[1]

        left_sz = (size-1) // 2
        right_sz = size // 2

        # position + left_sz is used

        heapq.heappush(openings, (-left_sz, -position))
        heapq.heappush(openings, (-right_sz, -position-left_sz-1))

    return right_sz, left_sz


if __name__ == "__main__":
    inp = sys.stdin.readlines()
    inp = inp[1:]

    T = len(inp)

    for i, input_line in enumerate(inp):
        large, small = solve(input_line)
        ans = "Case #{}: {} {}".format(i+1, large, small)
        print ans
        print >> sys.stderr, ans
