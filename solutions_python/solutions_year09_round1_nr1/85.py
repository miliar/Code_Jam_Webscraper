import sys

def isHappy(n, base):
    results = set()

    while 1:
        places = []
        while n>0:
            places.append(n % base)
            n /= base
        n = sum(map(lambda x: x**2, places))
        if n==1:
            return True
        elif n in results:
            return False
        results.add(n)

if __name__=='__main__':
    N = int(raw_input())
    for X in range(1, N+1):
        bases = map(lambda s:int(s), raw_input().split(' '))
        for i in xrange(2, sys.maxint):
            if all([isHappy(i, b) for b in bases]):
                print 'Case #%d: %d' % (X, i)
                break
        
