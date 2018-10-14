def resolve(nums):

    num, *rest = nums
    if not rest:

        return nums

    if num <= rest[0]:

        return [num] + resolve(rest)

    else:

        return [num - 1] + [9] * len(rest)


def logic(x):

    nums = list(map(int, str(x)))
    while True:

        nums = resolve(nums)
        if nums == sorted(nums):

            return int(str.join("", map(str, nums)))


def brute(x):

    while True:

        nums = list(map(int, str(x)))
        if nums == sorted(nums):

            return x

        else:

            x -= 1


for case in range(int(input())):

    x = int(input())
    print(str.format("Case #{}: {}", case + 1, logic(x)))

