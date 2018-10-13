
def tidy(N):
    nums = list(N)
    nums = [int(i) for i in nums]

    for i in range(len(nums)-2, -1, -1):
        if nums[i] > nums[i+1]:
            nums[i] = nums[i] - 1
            for j in range(i+1, len(nums)):
                nums[j] = 9

    nums = [n for n in nums if n != 0]
    return ''.join(str(n) for n in nums)

t = int(input())

for i in range(t):
    N = input()
    print('Case #' + str(i+1) + ': ' + str(tidy(N)))
