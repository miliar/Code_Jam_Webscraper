#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    n = int(raw_input())
    for i in range(n):
        a1 = int(raw_input())
        m1 = [set([int(x) for x in raw_input().split()]) for j in range(4)]
        a2 = int(raw_input())
        m2 = [set([int(x) for x in raw_input().split()]) for j in range(4)]
        #~ print '*'
        #~ print m1
        #~ print m2
        #~ print '*'
        ans = m1[a1-1].intersection(m2[a2-1])
        #~ print ans
        if len(ans) == 0:
            print 'Case #%d: Volunteer cheated!'%(i+1)
        elif len(ans) == 1:
            print 'Case #%d: %d'%(i+1, ans.pop())
        elif len(ans) > 1:
            print 'Case #%d: Bad magician!'%(i+1)
    return 0

if __name__ == '__main__':
    main()

