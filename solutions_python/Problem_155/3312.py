from __future__ import print_function
import sys

# 1,1,1,1,1     - 1,2,3,4,5
# 0,9           - 0,10
# 1,1,0,0,1,1   - 1,2,2+1,3+1,5,6

in_file = open(sys.argv[1], 'r')
out_file = open(sys.argv[2], 'w')

T = int(in_file.readline().strip())
for t in xrange(T):
    s = in_file.readline().split()[1]
    standing = 0
    guests = 0
    for i in xrange(len(s)):
        if standing < i:
            guests += i - standing
            standing = i
        d = int(s[i])
        standing += d
    print("Case #" + str(t+1) + ": " + str(guests), file=out_file)

in_file.close()
out_file.close()
