from heapq import heappush, heappop


def solve(N, K):
    n = N
    spans = []
    while K > 0:
        left = n // 2 - 1 if n % 2 == 0 else n // 2
        right = n // 2
        if left == 0 and right == 0:
            break
        if len(spans) > 0:
            max_span = -spans[0]
        if len(spans) > 0 and max_span > right:
            n = max_span
            heappop(spans)
            heappush(spans, -right)
        else:
            n = right
        heappush(spans, -left)
        K -= 1
    return right, left


def main():
    T = int(input())
    for case in range(T):
        N, K = (int(x) for x in input().split())
        answer = solve(N, K)
        print("Case #{}: {} {}".format(case + 1, answer[0], answer[1]))


if __name__ == '__main__':
    main()
