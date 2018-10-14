#!/usr/bin/env python

from fractions import gcd

def int_list(s):
    return map(lambda x: int(x), s.split())

def lcm(x, y):
    return x * y / gcd(x, y)

def main():
    cases = int(raw_input())
    for case in xrange(cases):
        n, l, h = int_list(raw_input())
        line = int_list(raw_input())
        
        #g = line[0]
        #for i in line[1:]:
        #    g = lcm(g, i)
        
        ans = "NO"
        for i in xrange(l, h+1):
            count = 0
            for j in line:
                g = gcd(i, j)
                if g == i or g == j:
                    count += 1
                    
            if count == n:
                ans = i
                break
        print 'Case #%d: %s' % (case + 1, ans)
    
if __name__ == '__main__':
    main()