#! /usr/bin/env python3
import sys
import typing


def solve(n: int) -> int:

    nums = [int(i) for i in str(n)]
    last_set = len(nums)

    for i in reversed(range(len(nums))):

        if i == 0:
            break

        if nums[i] >= nums[i - 1]:
            continue

        for j in range(i, last_set):
            nums[j] = 9

        last_set = i
        nums[i-1] -= 1

    return int(''.join((str(i) for i in nums)))


def main():
    f = open(sys.argv[1], 'r')

    for i, line in enumerate(f):

        if i == 0:
            continue

        num = int(line)
        res = solve(num)
        print('Case #{}: {}'.format(i, res))
        # print(line.strip())

if __name__ == '__main__':
    main()
