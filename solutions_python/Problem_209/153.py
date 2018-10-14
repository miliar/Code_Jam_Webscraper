import sys
import math


def solve(pancakes, k, test_case):
    
    radii = set(r for r, h in pancakes)
    
    side_areas = [(r * h, r, h) for r, h in pancakes]
    side_areas.sort(reverse = True)
    
    possible_solutions = []
    for max_r in radii:
        sub_side_areas = [sa for sa, r, h in side_areas if r < max_r]
        radius_side_areas = [sa for sa, r, h in side_areas if r == max_r]
        if len(sub_side_areas) + len(radius_side_areas) >= k:
            num_smaller = min(len(sub_side_areas), k - 1)
            num_equal = k - num_smaller
            possible_solutions.append(max_r * max_r + 2 * (sum(sub_side_areas[:num_smaller]) + sum(radius_side_areas[:num_equal])))
    
    solution = math.pi * max(possible_solutions)
    
    print('Case #{}: {}'.format(test_case, solution))


def solve_all(fn):
    
    with open(fn) as f:
        T = int(f.readline().strip())
        for tc in range(1, T+1):
            N, K = [int(x) for x in f.readline().strip().split()]
            pancakes = []
            for n in range(N):
                r, h = [int(x) for x in f.readline().strip().split()]
                pancakes.append((r, h))
            solve(pancakes, K, tc)


if __name__ == '__main__':
    solve_all(sys.argv[1])