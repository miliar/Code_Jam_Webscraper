def solve(nums: list):
    small = int(nums[-1])
    for i in range(len(nums) - 2, -1, -1):
        num = int(nums[i])
        if num > small:
            nums[i] = str(num - 1)
            for j in range(i+1, len(nums)):
                nums[j] = "9"
        small = int(nums[i])

    return int("".join(nums))


for _ in range(int(input())):
    print("Case #%d: %d" % (_ + 1, solve(list(input()))))
