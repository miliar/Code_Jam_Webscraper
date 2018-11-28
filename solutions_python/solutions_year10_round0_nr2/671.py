'''An algebraic version of B'''

import sys

cerr = lambda what: sys.stderr.write(repr(what)+'\n')

f = open('B-small.in')
lines = f.read().splitlines()
f.close()

T = int(lines.pop(0))

def gcd(a,b):
    a,b=max(a,b),min(a,b)
    while a%b != 0:
        a, b = b,a%b
    return b

Gcd = lambda seq: reduce(gcd, seq)

def factors(n):
    for k in xrange(1, int(n**0.5)+1):
        if n%k == 0:
            yield n/k
            yield k

f = open('B-small.out','w')
            
for t in xrange(T):
    nums = [int(x) for x in lines.pop(0).split()]
    N = nums.pop(0)
    nums = list(set(nums))
    N = len(nums)
    nums.sort(reverse=True)

    fs = set(factors(nums[0]-nums[1]))
    
    for i in xrange(2,len(nums)):
        diff = nums[i-1] - nums[i]
        facts = set(factors(diff))
        fs = fs.intersection(facts)

    xs = list(sorted(fs,reverse=True))
    if x[0] == 1:
        y = 0
    else:
        x = xs[0]
        mult = (nums[-1]/x)
        if (nums[-1]%x):
            mult+=1
        x = x*mult
        y = x - nums[-1]
    '''
    y = 0
    for x in xs:
        good = True
        for num in nums:
            if (num+x-1) % x != 0:
                good = False
                break
        if good:
            y = x-1
            break'''
    f.write("Case #%d: %d\n" % (t+1,(y)))
f.close()
