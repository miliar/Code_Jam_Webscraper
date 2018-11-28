#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''f = open('B-large.in','r')
g = open('B-large.ou','w')'''

f = open('B-small-attempt1.in','r')
g = open('B-small-attempt1.ou','w')


def solution(num):
    string = str(num)
    res = "0"
    back_track = False
    for k in range(len(string)):
        if not back_track:
            if int(string[k])>= int(res[-1]):
                res += string[k]
            else:
                back_track = True
                res = res[:-1]+str(int(res[-1])-1)
                i = 1
                while int(res[-i]) < int(res[-i-1]):
                    res = res[:-i-1]+str(int(res[-i-1])-1)+res[-i:]
                    i += 1
                if i == 1:
                    res += '9'*(len(string)-len(res)+1)
                else:
                    res = res[:-i+1] + '9'*(len(res))
                    res = res[:len(string)+1]
    return int(res)



n = int(f.readline()[:-1])
for k in range(n):
    num = int(f.readline()[:-1])
    g.write('Case #'+str(k+1)+': '+str(solution(num))+'\n')



f.close()
g.close()
