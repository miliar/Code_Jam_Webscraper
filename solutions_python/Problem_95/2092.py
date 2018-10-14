#!/usr/bin/env python
# -*- coding:utf-8 -*-
input = []
ans = []

before = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
          'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
          'de kr kd eoya kw aej tysr re ujdr lkgc jv']

after = ['our language is impossible to understand',
         'there are twenty six factorial possibilities',
         'so it is okay if you want to just give up']

dict = {}

for i in range(len(before)):
    for j in range(len(before[i])):
        if before[i][j] not in dict:
            dict[before[i][j]] = after[i][j]

#print sorted(dict.keys())
#print sorted(dict.values())

# 'z' is not in before and after...
#dict['z'] = 'q'
dict['q'] = 'z'
dict['z'] = 'q'

# print sorted(dict.keys())
# print sorted(dict.values())

# Dictionary was created

loop = raw_input()
for i in range(int(loop)):
    input = raw_input()
    ansStr = ''
    for c in input:
        ansStr += dict[c]
    ans.append(ansStr)

for i in range(int(loop)):
    print 'Case #%d: '%(i+1) + ans[i]
