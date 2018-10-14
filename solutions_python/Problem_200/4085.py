def tidy(x):
    nums = []
    while x > 0:
        nums.append(x % 10)
        x //= 10
    nums = nums[::-1]

    changed = True
    while changed:
        i = 0
        changed = False
        while i < len(nums) - 1:
            if changed:
                nums[i] = 9
            elif nums[i] > nums[i+1]:
                nums[i] -= 1
                changed = True
            i += 1
        if changed:
            nums[i] = 9

    n = 0
    for i in nums:
        n = n * 10 + i
    return n

f = open('B-large.in')
T = int(f.readline().strip())
i = 1
#f = ['132', '1000', '7', '111111111111111110']
for line in f:
    n = int(line.strip())
    print('Case #%d: %d' % (i, tidy(n)))
    i += 1
