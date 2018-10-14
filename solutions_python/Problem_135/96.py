#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    t = input()
    for i in range(t):
        print "Case #%d:" % (1+i),

        a1 = input()
        s1 = []
        for j in range(4):
            r = frozenset(map(int, raw_input().split()))
            s1.append(r)

        a2 = input()
        s2 = []
        for j in range(4):
            r = frozenset(map(int, raw_input().split()))
            s2.append(r)

        #print a1, s1
        #print a2, s2

        #if a1 < 1 or 4 < a1 or a2 < 1 or 4 < a2:
        #    print "Volunteer cheated!"
        #    continue

        s = list(s1[a1-1].intersection(s2[a2-1]))

        if len(s) == 0:
            print "Volunteer cheated!"
        elif len(s) == 1:
            print s[0]
        else:
            print "Bad magician!"


if __name__ == '__main__':
    main()

