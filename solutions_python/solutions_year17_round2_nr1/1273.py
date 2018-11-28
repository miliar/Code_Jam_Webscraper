#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def solve():
    D,N = map(int,fin.readline().split())
    K,S = [],[]
    for i in range(N):
        k,s = map(int,fin.readline().split())
        K.append(k)
        S.append(s)
    A=[]
    for i in range(N):
        A.append((D-K[i])/S[i])
    ans = D/max(A)
    return ans

import time
start = time.time()
print("Started!")
fin = open('A-large.in', 'rt')
fout= open("large.txt", 'wt')
T = int(fin.readline())
for i in range(T):
    print('Now Case {}'.format(i+1))
    fout.write('Case #{}: {}\r\n'.format(i+1, solve()))
fout.close()
print (("Finished!:{0}".format(time.time() - start)) + "[sec]")

