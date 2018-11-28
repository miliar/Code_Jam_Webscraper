def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def calc(nums):
    n = nums.pop(0)
    nums.sort()
    gcds = gcd(nums[0], nums[1])
    for i in xrange(2, n):
        gcds = gcd(gcds, nums[i])
    nums2 = map(lambda x : x / gcds, nums)
    T =  nums2[1] - nums2[0]    
    for i in xrange(1, n-1):
        now = nums2[i+1] - nums2[i]
        T = gcd(T, now)
    if nums2[0] % T == 0:
        y = 0
    else:
        y = T - nums2[0] % T
    return y * gcds
    

def work(filename):
    f = open(filename + ".in")
    out = open(filename + ".out", 'w')
    case_max = int(f.readline().strip())
    for caseno in xrange(case_max):
        out.write("Case #%d: " % (caseno+1))
        nums = map(int, f.readline().split())
        res = calc(nums)
        out.write("%d\n" % res)        
    f.close()
    out.close()

if __name__ == "__main__":
    #work("2")
    #work("B-small-attempt0")
    work("B-large")
