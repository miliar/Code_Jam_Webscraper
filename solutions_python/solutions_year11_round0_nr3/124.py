import sys
def print_result(x, y):
    print 'Case #%d: %s' % (x, y)
lines = sys.stdin
case_num = int(lines.next())
for i in range(case_num):
    lines.next()
    nums = [int(x) for x in lines.next().strip().split()]
    xor_result = nums[0]
    for x in nums[1:]:
        xor_result ^= x
    if xor_result:
        print_result(i + 1, 'NO')
    else:
        result = sum(nums) - min(nums)
        print_result(i + 1, result)
