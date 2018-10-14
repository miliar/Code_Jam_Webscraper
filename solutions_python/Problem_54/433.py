import sys


def gcd(A, B):
    # gcd(a,b)=gcd(b, a mod b)
    while B != 0:
        R = A % B
        A = B
        B = R
    return A

def mgcd(nums):
    # gcd(a, b, c) = gcd(gcd(a, b), c)
    g = nums[0]
    for i in range(1, len(nums)):
        g = gcd(g, nums[i])
    return g

def findx(nums):
    nums.sort(reverse=True)
    diff = []
    for i in range(len(nums)-1):
        diff.append(nums[i] - nums[i+1])
    m0 = mgcd(nums)
    m = mgcd(diff)
    if m == 1 or m0 == m:
        return 0
    b = nums[-1]
    x = m * (b/m+1) - b
    return x

def main(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    T = int(lines[0])
    for i in range(1, T+1):
        terms = lines[i].split()
        N = int(terms[0])
        num = []
        for j in range(N):
            num.append(long(terms[j+1]))
        res = findx(num)
        print "Case #%d: %s" % (i, res)

if __name__ == '__main__':
    main(sys.argv[1])