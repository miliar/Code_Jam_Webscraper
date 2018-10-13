import heapq
import sys

def get_max_min(n, k):
    """Get max(Ls, Rs) and min(Ls, Rs) after k people come."""

    counts = {n: 1}
    queue = [-n]
    curr = None

    while k > 0:

        # Pop one smallest size.
        size = -heapq.heappop(queue)
        count = counts.pop(size)

        quotient, rem = divmod(size, 2)
        curr = (
            quotient,
            quotient if rem == 1 else quotient - 1
        )

        # Push in the new sizes.
        for i in curr:
            if i in counts:
                counts[i] += count
            else:
                counts[i] = count
                heapq.heappush(queue, -i)

        k -= count

        continue

    assert curr is not None
    return curr
            

def main():
    """The main driver."""
    fp = open(sys.argv[1], 'r')
    for i, v in enumerate(fp):
        if i == 0:
            continue

        res = get_max_min(*[int(i) for i in v.split()])
        print('Case #{}: {} {}'.format(i, *res))
        continue

    return 0


if __name__ == '__main__':
    main()
