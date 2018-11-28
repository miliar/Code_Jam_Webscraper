import heapq


def main():
    n = int(raw_input().strip())

    for case_num in range(n):
        empty_num, person_num = map(int, raw_input().strip().split(' '))
        heap = []
        heapq.heappush(heap, (-1 * empty_num, 0, empty_num + 1))
        for i in range(person_num):
            empty_num, start, end = heapq.heappop(heap)
            next_stall = (start + end) / 2
            ls = (next_stall-start-1)
            rs = (end-next_stall-1)
            # left
            heapq.heappush(heap, (-1 * ls, start, next_stall))
            # right
            heapq.heappush(heap, (-1 * rs, next_stall, end))

        print 'Case #{}: {} {}'.format(case_num+1, max(ls, rs), min(ls, rs))


if __name__ == '__main__':
    main()
