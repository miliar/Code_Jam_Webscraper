def check(nums):
    return sorted(nums) == nums


def decrease(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            nums[i] -= 1
            nums[i + 1:] = [9] * (len(nums) - i - 1)


def solve():
    n = input()
    nums = list(map(int, str(n)))
    while not check(nums):
        decrease(nums)

    return int(''.join(map(str, nums)))


if __name__ == '__main__':

    T = int(input())
    for tt in range(T):
        res = solve()
        print('Case #{}: {}'.format(tt + 1, res))
