from itertools import combinations_with_replacement
import sys

file = sys.stdin
# file = open('b.in', "r")

T = int(file.readline())


def num(nums):
    tot = 0
    for num in nums:
        tot *= 10
        tot += num
    return tot


for i, t in enumerate(range(T), 1):
    N = list(map(int, list(file.readline().strip())))
    prev = None
    for x in combinations_with_replacement(range(0, 10), len(N)):
        if num(x) == num(N):
            print('Case #{}: {}'.format(i, ''.join(map(str, x))))
            break
        elif num(x) > num(N):
            if prev[0] == 0:
                prev = prev[1:]
            print('Case #{}: {}'.format(i, ''.join(map(str, prev))))
            break
        prev = x
