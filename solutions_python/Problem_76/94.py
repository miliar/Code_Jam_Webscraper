import sys
from itertools import *
cin = sys.stdin.readline

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def brute_force(nums):
    ret = -1
    for tup in powerset(range(len(nums))):
        if len(tup) == 0 or len(tup) == len(nums):
            continue
        se = set(tup)
        #print se
        a, b = 0, 0
        su = 0
        for i in xrange(len(nums)):
            if i in se:
                a ^= nums[i]
                su += nums[i]
            else:
                b ^= nums[i]
        if a == b:
            ret = max(ret, su)
    #print ret, sum(nums) - min(nums)
    return ret
                    
                
    
    

def solve(nums):
    if reduce(lambda x,y: x^y, nums) != 0:
        return "NO"
    #return brute_force(nums)
    return sum(nums) - min(nums)
    memo = {}
    def dp(at, cur, did):
        if at == N:
            if cur == 0 and did:
                return 0
            else:
                return -100000000000000L
        tup = (at, cur, did)
        if tup in memo:
            return memo[tup]
        
        memo[tup] = out = max(dp(at+1, cur, True),
                              nums[at] + dp(at+1, cur ^ nums[at], did))
        return out
    return dp(0, 0, False)
    

if __name__ == '__main__':
    T = int(cin())
    for i in xrange(T):
        N = int(cin())
        q = list(int(j) for j in cin().strip().split())
        print "Case #{0}: {1}".format(i+1, solve(q[:N]))
                    
            
        
    
