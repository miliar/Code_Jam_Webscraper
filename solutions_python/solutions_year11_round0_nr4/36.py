def solve(arr):
    nums = [int(c) for c in arr]
    return len(nums) - sum([1 for i in range(len(nums)) if nums[i] - 1 == i])

with open ('D-large.in') as f:
    t = int(f.readline())
    for i in range(t):
        f.readline()
        arr = f.readline().split(' ')
        print 'Case #{0}: {1}.000000'.format(i+1 ,solve(arr))
