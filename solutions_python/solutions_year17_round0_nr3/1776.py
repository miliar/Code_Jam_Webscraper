import sys
import heapq


def solve(line, test_case):
    
    n, k = [int(x) for x in line.split()]
    
    queue = []
    heapq.heappush(queue, (-(n // 2), -((n-1) // 2)))
    
    for p in range(k - 1):
        free_max, free_min = heapq.heappop(queue)
        if free_max != 0:
            heapq.heappush(queue, (-(free_max // -2), -((free_max + 1) // -2)))
            if free_min != 0:
                heapq.heappush(queue, (-(free_min // -2), -((free_min + 1) // -2)))
    
    print('Case #{}: {} {}'.format(test_case, -1 * queue[0][0], -1 * queue[0][1]))


def solve_all(input_file):
    
    with open(input_file) as f:
        for t, l in enumerate(f):
            if (t > 0) and (l.strip() != ''):
                solve(l.strip(), t)


if __name__ == '__main__':
    solve_all(sys.argv[1])