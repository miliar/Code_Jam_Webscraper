'''
Created on Apr 13, 2013

@author: santosh
'''
import math

if __name__ == '__main__':
    for t in xrange(int(raw_input())):
        cnt = 0
        (A, B) = ([int (i) for i in raw_input().split()])
        for i in xrange(A, B + 1, 1):
            isqrt = math.sqrt(i)
            str_i = str(i)
            str_isqrt = str(int(isqrt))
            if str_i == str_i[::-1] and isqrt == math.trunc(isqrt) and str_isqrt == str_isqrt[::-1]: cnt += 1
        print 'Case #%d: %d' % (t + 1, cnt)

        
