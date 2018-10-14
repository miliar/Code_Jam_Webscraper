import heapq
record = {}


def choose(n):
    if n == 1:
        return 1
    if n % 2 == 1:
        return n // 2 + 1
    return n // 2


def answer(inp):
    inp = inp.split(' ')
    N = int(inp[0])
    K = int(inp[1])
    if N == K:
        return "0 0"
    result = {N: [1]}
    for i in range(K):
        length = max(result.keys())
        stall = choose(length)
        candidate = heapq.heappop(result[length]) if len(
            result[length]) > 1 else result.pop(length)[0]
        left = stall - 1
        right = length - stall
        if i == K - 1:
            return "{} {}".format(max(left, right), min(left, right))
        if left in result:
            heapq.heappush(result[left], candidate)
        elif left != 0:
            result[left] = [candidate]
        if right in result:
            heapq.heappush(result[right], stall + 1)
        elif right != 0:
            result[right] = [stall + 1]


def main():
    numCases = int(input())
    for i in range(numCases):
        print("Case #{}: {}".format(i + 1, answer(input())))


if __name__ == "__main__":
    main()
