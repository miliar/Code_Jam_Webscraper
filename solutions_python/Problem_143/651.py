def solve():
    [a, b, k] = [int(j) for j in raw_input().split()]
    return sum(sum(i&j<k for j in range(b)) for i in range(a))

for i in range(input()):
    print "Case #{0}: {1}".format(i+1, solve())
