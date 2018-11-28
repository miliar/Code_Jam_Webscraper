#!/usr/bin/env python

d = {'y':'a', 'e':'o', 'q':'z', 'z':'q'}
strs = [('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand'),
        ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities'),
        ('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up')]



for a,b in strs:
    for x,y in zip(a,b):
        d[x] = y


t = int(input())
for case in range(1,t+1):
    s = input().strip().lower()
    print('Case #{}:'.format(case), end=' ')
    for i in s:
        if i not in d:
            print(i, end='')
        else:
            print(d[i], end='')
    print()
