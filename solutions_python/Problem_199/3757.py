# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 06:12:37 2017

@author: thinus
"""


f = open('/Google 2017/A-large.in','r+')
fo = open('/Google 2017/out.txt','w')
t = int(f.readline())

for m in range ( 0, t):
    case = f.readline().split()
    k = int(case[1])
    s = case[0]
    answer = 0
    for i in range ( 0, len(s)):
        if ( s[i] == "+"):
            #print ('unchanged  ',s)
            continue
        else:
            if ( len(s) - i - k >= 0):
                for j in range (i, i + k):
                    if ( s[j] == "+"):
                        s = s[:j] + '-' + s[j + 1:]
                    else:
                        s = s[:j] + '+' + s[j + 1:]
                answer += 1
                #print ('flipped  ',s,'  count k  ',k)
            else: 
                answer = -1
                #print ('cannot do ',s,'  count k  ',k)
                break
            
    if ( answer >= 0):
        res = "Case #{}: {} ".format(m + 1, answer)+'\n'      
        #print(res)
        fo.write(res)
    else:
        res = 'Case #{}:'.format(m + 1) + ' IMPOSSIBLE' + '\n'
        #print(res)
        fo.write(res)
fo.close()
f.close()
        