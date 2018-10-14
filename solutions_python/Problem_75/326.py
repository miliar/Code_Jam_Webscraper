#!/usr/bin/env python3

t = int(input())
for i in range(t):
        a = input().split()
        c = int(a[0])
        dc = {}
        for j in range(c):
                s = a[1+j]
                ss = s[:2]
                dc[ss] = s[2:]
                dc[ss[::-1]] = s[2:]
        d = int(a[1+c])
        dd = {}
        for j in range(d):
                s = a[2+c+j]
                if not s[0] in dd: dd[s[0]] = set()
                if not s[1] in dd: dd[s[1]] = set()
                dd[s[0]].add(s[1])
                dd[s[1]].add(s[0])
        n = int(a[2+c+d])
        s = a[3+c+d]
        assert(len(s) == n)

        r = ""
        for e in s:
                if r:
                        cc = e + r[-1]
                        if cc in dc:
                                r = r[:-1] + dc[cc]
                        elif e in dd and any(rr in dd[e] for rr in r):
                                r = ""
                        else:
                                r += e
                else:
                        r = e
                                
        print("Case #{0}: {1}".format(i+1, '[' + ', '.join(r) + ']'))
