# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 14:09:48 2017

@author: Suganya
"""


f = open('B-small-attempt1.in')
f1 = open('out.txt', 'wb')
lines = f.read().split("\n")
num_lines = len(lines)
k = int(lines[0])
for j in range(1,k+1):
    N = int(lines[j])
    for i in xrange(N,0,-1):
        if(i <= N):
            list1 = [int(d) for d in str(i)]
            if(sorted(list1) == list1):
                x = list1
                s = 'Case #' + str(j) + ': ' + ''.join(map(str, x))
                print s
                f1.write(s)
                f1.write('\n')
                break
f.close()
f1.close()


