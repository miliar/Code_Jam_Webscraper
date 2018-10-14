def steed(d, n, horses):
    return d/max([float(d-k)/s for k,s in horses])

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
    d, n = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    horses = [[int(s) for s in raw_input().split(" ")] for line in range(n)]
    # print d, n, horses
    print "Case #{}: {}".format(i, steed(d, n, horses))