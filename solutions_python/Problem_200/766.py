import sys

def solve(n):
    nums = [int(x) for x in n]
    ans = []
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i+1:] = [9]*(len(nums)-i-1)
            # nums[i]
            for j in range(i, -1, -1):
                nums[j] -= 1
                if j > 0:
                    if nums[j] >= nums[j-1]:
                        break
                    else:
                        nums[j] = 9
            break
    if nums[0] <= 0:
        nums = nums[1:]
    return ''.join(str(x) for x in nums)

if __name__ == '__main__':
    lines = sys.stdin.readlines()[1:]
    for t, l in enumerate(lines):
        print('Case #{}: {}'.format(t+1,solve(l.strip())))
