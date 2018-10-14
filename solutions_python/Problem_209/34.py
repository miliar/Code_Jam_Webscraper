from math import pi

def pancake(dims, k):
    n = len(dims)
    tests = []
    for i in range(n):
        tests.append([ 2*dims[i][0]*dims[i][1], dims[i][0]**2 ])
    ham = list(reversed(sorted(tests, key = lambda x: x[0])))
    widest = max(ham, key = lambda x: x[1])
    instack = False
    curr = 0
    currmax = 0
    for i in range(k-1):
        curr += ham[i][0]
        currmax = max(currmax,ham[i][1])
    bop = ham[k-1][0] + max(ham[k-1][1],currmax)
    for i in range(k,n):
        if ham[i][1] > currmax:
            bop = max(bop,ham[i][0]+ham[i][1])
    a = str((curr + bop)*pi)
    ans = []
    for i in a:
        if i != '+':
            ans.append(i)
    return ''.join(ans)


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
    n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    dims = [[int(s) for s in raw_input().split(" ")] for line in range(n)]
    print "Case #{}: {}".format(i, pancake(dims, k))