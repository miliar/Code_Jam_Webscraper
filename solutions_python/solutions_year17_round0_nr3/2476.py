from heapq import heappush, heappop


class Heap():

    def __init__(self, iterable):
        self._heap = []
        for it in iterable:
            self.push(it)

    def push(self, item):
        size, part = item
        heappush(self._heap, (-size, part))

    def pop(self):
        return heappop(self._heap)

    def most(self):
        return -min(self._heap)[0]

    def least(self):
        return -max(self._heap)[0]

    def __str__(self):
        return str(self._heap)


def part_size(part):
    return (part[1] - part[0] + 1)


def solve(partitions, k):
    n = partitions[0][0]
    positions = [0] * (n + 1)
    partitions = Heap(partitions)
    i = k
    while i:
        # print(k, partitions)
        _, best_part = partitions.pop()

        mid = (best_part[0] + best_part[1]) // 2
        # print(mid)
        positions[mid] = (k - i + 1)

        part1 = (best_part[0], mid - 1)
        part2 = (mid + 1, best_part[1])
        size1 = part_size(part1)
        size2 = part_size(part2)

        if size1 >= 0:
            partitions.push((size1, part1))
        if size2 >= 0:
            partitions.push((size2, part2))

        i -= 1
    r = n + 1
    for i in range(mid+1, n + 1):
        if positions[i]:
            r = i
            break
    l = 0
    for i in range(mid - 1, 0, -1):
        if positions[i]:
            l = i
            break
    ls = mid - l - 1
    rs = r - mid - 1
    # print(mid)
    return max(ls, rs), min(ls, rs)


def main():
    T = int(input())
    outputs = []
    for t in range(1, T+1):
        n, k = [int(i) for i in input().split()]

        out = solve([(n, (1, n))], k)

        outputs.append("Case #%d: %d %d" % (t, *out))
    print("\n".join(outputs))


if __name__ == '__main__':
    main()
