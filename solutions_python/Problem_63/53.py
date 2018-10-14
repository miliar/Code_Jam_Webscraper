from math import sqrt

def calc(L, P, C):
        res = 0
        while L * C < P:
                L = int(sqrt(L*P)+0.5)
                res += 1
        return res

T = input()
for i in xrange(T):
        L, P, C = [int(n) for n in raw_input().split()]
	print "Case #%i: %s" % (i+1, calc(L, P, C))

