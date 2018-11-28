from bitarray import bitarray
import heapq


def flip(b, k=1, offset=0):
    for i in range(offset, offset + k):
        b[i] = not b[i]
    return b


def to_bitarray(s):
    return bitarray([c == "+" for c in s])

def solve(s, k):
    b = to_bitarray(s)
    queue = [(b.count(), 0, b)]
    seen  = set()
    while(queue):
        count, steps, current = heapq.heappop(queue)
        if current.all():
            return (steps,)
        for i in range(0, len(b) - k + 1):
            candidate = flip(current.copy(), k, i)
            if candidate.tobytes() not in seen:
                seen.add(candidate.tobytes())
                heapq.heappush(queue, (-candidate.count(), steps + 1, candidate))
    return ("IMPOSSIBLE",)


def read_input():
    t = int(input())
    for _ in range(t):
        s, k = input().split()
        k = int(k)
        yield(s, k)

def main():
    results = [solve(*test_case) for test_case in read_input()]
    for i, result in enumerate(results):
        print (
            "Case #{}: {}".format(
                i + 1,
                ' '.join(str(x) for x in result)
            )
        )
if __name__ == '__main__':
    main()