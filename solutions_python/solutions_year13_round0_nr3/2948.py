import sys
import itertools
import math
rl = lambda: sys.stdin.readline().strip()

def is_palindrome(i):
    return str(i) == str(i)[::-1]
def palindromes(k):
    """
    assumes k>=3. Will add a case for k=1,2
    """
    
    _0to9=xrange(10);
    _1to9=xrange(1,10)

    if k<5:
        l1 = []
        for i in range(1,100):
            if is_palindrome(i):
                l1.append(i)
        return l1
    

def compute():    
    ns = rl()
    a,b = ns.split()
    k = int(math.ceil(math.log(int(b), 10)))
    
    filtered  = filter(lambda x: x >= math.sqrt(int(a)) and x <= math.sqrt(int(b)), palindromes(k))
    powered    = map(lambda x: int(math.pow(x,2)), filtered)
    square    = map(is_palindrome, powered)
    
    return sum(square)
if __name__ == '__main__':
    for i in range(int(rl())):
        print "Case #%d: %d" % (i+1, compute())