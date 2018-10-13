def checkDecreasing(n):
    prev = 10
    while n > 0:
        d = n % 10
        if d > prev:
            return False
        prev = d
        n/=10
    return True

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    while not checkDecreasing(n) and n>0:
        n-=1
    print "Case #{}: {} ".format(i,n)
