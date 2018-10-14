import sys
from operator import xor

cases = int(sys.stdin.readline())

for case in range(cases):
    n = int(sys.stdin.readline().strip())
    nums = map(long, 
               filter(lambda x: x != '',
                      map(lambda x: x.strip(), 
                          sys.stdin.readline().split(" "))))
    xxor = reduce(xor, nums)
    if xxor != 0:
        print 'Case #%d: NO' % (case + 1)
    else:
        print 'Case #%d:' % (case + 1), sum(nums) - min(nums)


