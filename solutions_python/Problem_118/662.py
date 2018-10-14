import sys
from collections import defaultdict
import bisect

if __name__ == '__main__':
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)
    output = open('jamqual3.out', 'w')
    t = int(f.readline())
    nums = [1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,\
            4008004,100020001,102030201,104060401,121242121,123454321,125686521,\
            400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,\
            1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,\
            1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004]
    for test in xrange(1, t+1):
        str1 = "Case #%d: " %(test)
        output.write(str1)
        a, b = map(int, f.readline().split())
        ans = bisect.bisect_right(nums, b) - bisect.bisect_left(nums, a)
        output.write(str(ans)+'\n')
    output.close()
        
