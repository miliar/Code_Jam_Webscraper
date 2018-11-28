from __future__ import division

def ride (dist, num):
    best = 0
    for i in range(num):
        k, s = [int(x) for x in raw_input().split(" ")]
        time = (dist - k)/s
        if(time > best):
            best = time
    return dist/best




# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
#t = int(input())  # read a line with a single integer
#for i in range(1, t + 1):
#    n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
#    print("Case #{}: {} {}".format(i, n + m, n * m))
    # check out .format's specification for more formatting options

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    d, n = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}: {}".format(i, ride(d,n))
    # check out .format's specification for more formatting options