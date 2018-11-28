def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a
#print gcd(180, 48)

def gcdli(li):
    n = len(li)
    i=0
    while i < n - 1:
        #caluculate GCD between X[i] and X[i+1] using your function
        li[i+1]=gcd(li[i], li[i+1]) 
        i=i+1
    return li[n-1]

def find(inp):
    inp.sort(cmp=None, key=None, reverse=True)
    #print inp
    inp2 = []
    #vazzeg = True
    for n in inp[1:]:
        inp2.append(inp[0] - n)
    #print inp2
    g = gcdli(inp2)
    #print g
    if g < 2:
        res = 0
    else:
        r = inp[len(inp)-1] % g
        #print r
        if r == 0:
            return 0, 0
        else:
            res = (g - (r));
    #print "res."+str(res)
    return g, res

import sys
f = open(sys.argv[1], 'r')

t = int(f.readline())
for i in range(1,t+1):
    nums = map(int,f.readline().split())[1:]
    #print nums
    nums2 = list(set(nums))
    #print nums2
    g, res = find(nums2)
    #nums2 = map(lambda x : x + res, nums)
    #print nums2
    #g2 = gcdli(nums2)
    #if g2 != g:
    #    print "........FAAAAK.......", nums
    print "Case #%d: %s" % ( i, res )
