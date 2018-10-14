#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    t = int(raw_input())
    for j in range(t):
        n = int(raw_input())
        
        a = raw_input()
        b = raw_input()
        
        a = a.split(' ')
        b = b.split(' ')

        for i in range(len(a)):
            a[i] = int(a[i])
        for i in range(len(b)):
            b[i] = int(b[i])

        a.sort()
        b.sort()
        b.reverse()

        ans = 0
        for i in range(n):
            ans = ans + a[i]*b[i]
        
        print 'Case #%d: %d' % (j+1, ans)

if __name__ == '__main__':
    main()