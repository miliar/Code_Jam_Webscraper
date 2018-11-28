import itertools


def solve():
    nums = [int(x) for x in input()][::-1]
    last_ind = 0
    last = 9
    for i in range(len(nums)):
        if nums[i] > last:
            nums[i] -= 1
            nums[last_ind:i] = itertools.repeat(9, i - last_ind)
            last_ind = i
        last = nums[i]
    while nums[-1] == 0:
        nums.pop()
    return ''.join(map(str, nums[::-1]))


def main():
    t = int(input())
    for i in range(t):
        print('Case #{}: {}'.format(i + 1, solve()))


if __name__ == '__main__':
    main()
