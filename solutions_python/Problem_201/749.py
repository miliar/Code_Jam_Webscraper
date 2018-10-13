import heapq


def readint(stream):
    return int(stream.next()[:-1])


def readpair(stream):
    line = stream.next()[:-1]
    pair = line.split(' ')
    return int(pair[0]), int(pair[1])


def main():
    nums = []

    with open('input.txt', 'r') as f:
        count = readint(f)
        with open('output.txt', 'w') as o:
            for i in range(count):
                n, k = readpair(f)
                result = solve(n, k)
                o.write("Case #{}: {} {}\n".format(i + 1, result[0], result[1]))


def _add_counter(counters, heap, key, value):
    if key in counters:
        counters[key] += value
    else:
        counters[key] = value
        heapq.heappush(heap, -key)


def solve(n, k):
    heap = [-n]
    counters = {n : 1}
    
    while len(heap) > 0:
        top = -heapq.heappop(heap)
        top2 = top / 2
        if k <= counters[top]:
            return (top2, top2 - 1) if top % 2 == 0 else (top2, top2)

        k -= counters[top]
        if top % 2:
            _add_counter(counters, heap, top2, counters[top] * 2)
        else:
            _add_counter(counters, heap, top2, counters[top])
            _add_counter(counters, heap, top2 - 1, counters[top])

        del counters[top]
    
    return 0, 0


if __name__=='__main__':
    main()