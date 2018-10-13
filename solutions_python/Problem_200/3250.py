#!/usr/bin/python3

import sys

def solve(testCase):
    #Convert to number array
    nums = []
    for n in str(testCase):
        nums.append(int(n))

    #Short circuit if only 1 number
    if(len(nums) < 2):
        return nums[0]
    
    for i in range(len(nums)-1, 0, -1):
        if(nums[i] < nums[i-1]):
            nums[i-1] -= 1
            for j in range(i, len(nums)):
                nums[j] = 9
    
    nums = [str(n) for n in nums]
    nums = ''.join(nums)
    nums = nums.lstrip('0')
    return nums

def main():
    filename = sys.argv[1]
    lines = []
    numTests = 0

    with open(filename) as f:
        lines = f.readlines()

    numTests = int(lines[0])
    lines.pop(0)

    for i in range(numTests):
        lines[i] = lines[i].strip('\n')
        solve(lines[i])
    
    #----------------
    count = 1
    for testCase in lines:
        print("Case #" + str(count) + ": " + str(solve(testCase)))
        count += 1


if __name__ == '__main__':
    main()
