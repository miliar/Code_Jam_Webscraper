# Bathroom Stalls


# x is the amount of stalls and n is the amount of people searching for a stall
# return a list with max stalls left in the first index and min min stalls left in the second
def bathroom(x, n):
    if x % 2 == 1:
        l = x / 2
        r = x / 2
    else:
        l = x / 2
        r = (x-1)/2
    if n == 1:
        return [l, r]
    if n == 2:
        return bathroom(l, 1)
    if n%2 == 1:
        ln = n/2
        rn = n/2
        return bathroom(r, rn)
    else:
        ln = n/2
        rn = (n-1)/2
        return bathroom(l, ln)

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    inp = raw_input().split(" ")
    N = int(inp[0])
    K = int(inp[1])

    ls = bathroom(N, K)
    maxx = ls[0]
    minn = ls[1]

    print "Case #{}: {} {}".format(i, maxx, minn)
