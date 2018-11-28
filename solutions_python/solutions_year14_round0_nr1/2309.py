#!/usr/bin/env python

N = input()

for _ in range(N):
        a = input()
        s = []
        for i in range(4):
                s.append(raw_input())

        b = input()
        t = []
        for i in range(4):
                t.append(raw_input())

        n = filter(lambda x: x in map(int, s[a - 1].split()) and x in map(int, t[b - 1].split()), range(1, 17))
        if len(n) == 0:
                print 'Case #%d: Volunteer cheated!' % (_ + 1)
        elif len(n) == 1:
                print 'Case #%d: %d' % (_ + 1, n[0])
        else:
                print 'Case #%d: Bad magician!' % (_ + 1)