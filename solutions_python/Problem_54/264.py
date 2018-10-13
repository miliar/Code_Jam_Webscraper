import sys
import string

def gcd(a,b):
    if (a > b):
        return gcd(b,a)
    if (a == 0):
        return b;
    return gcd(b % a, a);


line = string.split(sys.stdin.readline())
for x in range(int(line[0])):
    nums = string.split(sys.stdin.readline());
    for i in range(len(nums)):
        nums[i] = long(nums[i])

    nums = nums[1:]
    nums.sort()

    
    dif = []
    for i in range(len(nums)-1):
        dif.append(nums[i+1] - nums[i])
    dif = filter(lambda x: x > 0, dif)
    dif.sort()

   
    
    mul = dif[0]
    for f in dif:
        mul = gcd(mul,f)       


    g = nums[0]
    for o in nums:
        g = gcd(g,o)
        
    k = long(0)
    found = 0
    for n in nums:
        thisk = mul - (n%mul)

        
        if found:
            if thisk != k:
                k = 0
                break;
        else:
            k = thisk
            found = 1
    gk = nums[0] + k
    for o in nums:
        gk = gcd(gk, o + k)

    if g >= gk:
        print "Case #{0}: {1}".format(x+1,0)
    else:
        print "Case #{0}: {1}".format(x+1,k)

