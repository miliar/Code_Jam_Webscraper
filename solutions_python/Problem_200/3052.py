def isSorted(l):
    return all(l[i] <= l[i+1] for i in xrange(len(l)-1))

def solve(num):
    for i in range(len(num) - 2, -1, -1):
        if isSorted(num):
            return num
        num[i] -= 1
        num[i+1] = 9
    return num

T = int(raw_input())
for t in range(T):
    num = [int(c) for c in raw_input()]
    ret = solve(num)

    res = 0
    for n in ret:
        res *= 10
        res += n

    print "Case #{}: {}".format(t+1, res)
