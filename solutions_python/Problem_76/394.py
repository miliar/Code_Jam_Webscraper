import math

def largest(a,b):
    x=a
    y=b
    if(x<y):
        x=b
        y=a
    g=[]
    for i in xrange(int(math.log(x,2)),-1,-1):
        if(y%(2**i)!=y and x%(2**i)!=x):
            y=y%(2**i)
            x=x%(2**i)
            g+=[2*(2**i)]
        if(y%(2**i)!=y):
            y=y%(2**i)
        if(x%(2**i)!=x):
            x=x%(2**i)   
    return g

def add(a,b):
    return a+b-sum(largest(a,b))

def maximum(nums,partition=1):
    if(partition==len(nums) or sum(nums[:partition])>sum(nums[partition:])):
        return "NO"
    #print nums[:partition],reduce(add,nums[:partition]),nums[partition:],reduce(add,nums[partition:])
    if reduce(add,nums[:partition])== reduce(add,nums[partition:]):
        return sum(nums[partition:])
    return maximum(nums,partition+1);


T=int(raw_input())
for l in range(T):
    N=int(raw_input())
    nums=sorted([int(x) for x in raw_input().split()])
    print "Case #%d:"%(l+1),maximum(nums)
    
