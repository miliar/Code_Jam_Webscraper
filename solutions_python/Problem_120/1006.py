
# this works for small case:

def rings(r,t):
    ans = 0
    while True:
        nextRing = (r+1)**2 - r**2
        #print ans, t, r, nextRing        
        if nextRing > t:
            break
        t -= nextRing
        ans += 1
        r += 2
    return ans
    

"""
paint used is sum of

(x+1)^2 - x^2 starting at   x = r

= x^2 + 2x + 1 - x^2 = 2x+1

sum of (2x+1)   for x from r to n=??  step by 2


if r is even:
  sum of   2x+1   for x=2k to 2n   x=2y
     =  sum of 4y+1 for y=k to n
     =   4*n*(n+1)/2 + n   -   4*(k-1)*k/2 - (k-1)
     =  2n^2 + 3n - 2k^2 + k +1     find n

if r is odd
   sum of  2x+1 for x=2k+1 to 2n+1   x=2y+1

   =   sum  2(2y+1) +1   y = k to n
=   sum 4y +3  y= k to n
=   4*n*(n+1)/2   - 4*k*(k-1)/2    + 3n - 3(k-1)
=   2 n^2 + 5n  - 2k^2  -k +3


"""
import math

##def fEven(n):
##    r = 1
##    return 2*n**2 + 3*n - 2*r**2 +r +1
##
##def fOdd(n):
##    r = 1
##    return 2*n**2 + 3*n - 2*r**2 +r +1

def solvePaint(r,t):
    if r % 2 == 0:
        k = r/2
        # 2n^2 + 3n - 2k^2 +k +1 -t < 0    largest n
        disc = 3**2 - 4*2*(-2*k**2+k+1-t)
        x = (-3 + math.sqrt(disc))/4.0

        n = int(x)
        n1 = n+1
        #print disc, x, n

        paint0 = 2*x**2 + 3*x - 2*k**2 +k +1
        #print x, paint0
        
        paint = 2*n**2 + 3*n - 2*k**2 +k +1
        paint1 = 2*n1**2 + 3*n1 - 2*k**2 +k +1
        #print n, paint, t, n1, paint1

        if paint > t:
            n -= 1
        elif paint1 <= t:
            n += 1
        
##        assert paint <= t
##        assert paint1 > t
        return n-k+1
    else:  # odd
        # 2 n^2 + 5n  - 2k^2  -k +3 -t <0   largest n
        k = r//2
        disc = 5**2 - 4*2*(-2*k**2 -k+3 -t)
        x = (-5 + math.sqrt(disc))/4.0
        n = int(x)
        n1 = n+1
        #print disc, x, n
        
        paint = 2*n**2 + 5*n - 2*k**2 -k +3       
        paint1 = 2*n1**2 + 5*n1 - 2*k**2 -k +3

        paint0 = 2*x**2 + 5*x - 2*k**2 -k + 3
        #print x, paint0
        
        #print n, paint, t, n1, paint1
        
##        assert paint <= t
##        assert paint1 > t
        if paint > t:
            n -= 1
        elif paint1 <= t:
            n += 1
            
        return n-k+1

##import random
##for testCase in range(100):
##    r = random.randint(1,1000)
##    t = random.randint(1,10000)
##    assert rings(r,t) == solvePaint(r,t)
##
##print "tests passed"

##assert False

nCases = int(raw_input())

for n in range(nCases):
    r,t = map(int, raw_input().split())
    ans = solvePaint(r,t)
    
##    if t<100:
##        bruteForce = rings(r,t)
##        print bruteForce, ans
##        assert bruteForce == ans
    print "Case #" + str(n+1) + ": " + str(ans)
    
