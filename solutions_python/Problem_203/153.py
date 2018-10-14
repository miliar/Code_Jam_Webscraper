from collections import defaultdict
import math

def fill_rect(cake, x1, y1, x2, y2, c):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            cake[y][x] = c

def check_rect(cake, x1, y1, x2, y2):
    if x2 >= len(cake[0]):
        return False
    # other overflow cases will never happen
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if cake[y][x] != '?':
                return False
    return True

def fill_same(cake):
    char_min_max = defaultdict(lambda: (math.inf, math.inf, -math.inf, -math.inf))
    for x in range(len(cake[0])):
        for y in range(len(cake)):
            if cake[y][x] == '?':
                continue
            mm = char_min_max[cake[y][x]]
            char_min_max[cake[y][x]] = (min(mm[0], x), min(mm[1], y),
                                        max(mm[2], x), max(mm[3], y))
    for c, (min_x, min_y, max_x, max_y) in char_min_max.items():
        fill_rect(cake, min_x, min_y, max_x, max_y, c)
    return char_min_max

def grow_left(cake, char_min_max):
    for c, (min_x, min_y, max_x, max_y) in char_min_max.items():
        for i in range(1, 999):
            if check_rect(cake, max_x + i, min_y, max_x + i, max_y):
                fill_rect(cake, max_x + i, min_y, max_x + i, max_y, c)
            else:
                break

def rotate(cake):
    return [list(t) for t in zip(*cake[::-1])]

def solve(cake):
    for i in range(4):
        char_min_max = fill_same(cake)
        grow_left(cake, char_min_max)
        cake = rotate(cake)
    return cake


def main():
    num_cases = int(input())
    for t in range(num_cases):
        h, w = map(int, input().split())
        cake = []
        for y in range(h):
            cake.append(list(input()))
        cake = solve(cake)
        print('Case #{}:\n{}'.format(
            t + 1, '\n'.join(''.join(line) for line in cake)))

main()
