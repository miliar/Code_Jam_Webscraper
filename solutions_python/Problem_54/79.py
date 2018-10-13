import os
import sys
from sys import argv

problem = 'B'
if len(argv) == 2:
    problem = argv[1]
    if problem.endswith('.in'):
        problem = problem[:-3]

input = problem + '.in'
output = problem + '.out'

def gcd(a,b):
    if b == 0: return a
    return gcd(b, a%b)

def bru(nums):
    x = max(nums)
    found = False
    while not found:
        x -= 1
        found = True
        m = nums[0] % x
        for num in nums:
            if num % x != m:
                found = False
                break
    return x

print 'doing ', input
print 'to    ', output

fp_in = open(input, 'r')
fp_out = open(output, 'w')

T = int(fp_in.readline())
for Ti in range(T):
    line = fp_in.readline()
    LLL = line.split()
    N = LLL[0]
    nums = [int(s) for s in LLL[1:]]
    # print nums
    nums.sort()
    tmp = [nums[0]]
    for num in nums:
        if num != tmp[-1]:
            tmp.append(num)
    nums = tmp

    diffs = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            diffs.append(nums[j] - nums[i])
    diffs.sort()

    x = diffs[0]
    for i in range(1, len(diffs)):
        if diffs[i] != diffs[i - 1]:
            if diffs[i] % x != 0:
                x = gcd(diffs[i], x)
                if x <= 1: break
    if x <= 0:
        print 'Error:', x
        break
    '''
    xx = bru(nums)
    if xx != x:
        print 'Error: x,xx = ', x, xx
        break
    '''
    ans = 0
    if x > 1 and nums[0] % x != 0:
        # for num in nums:
        #     print num, '%', x, '=', num % x
        ans = x - nums[0] % x;
    fp_out.write(('Case #%d: ' % (Ti + 1)) + str(ans) + '\n')
    # print ''

# print 'done'
