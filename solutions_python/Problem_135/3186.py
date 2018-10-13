# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 22:00:35 2014

@author: Βίκυ!
"""
#%%
f = open('C:/Users/Βίκυ!/Desktop/GoogleCodeJam/MagicTrick/RealData/input.txt', 'r')
fout = open('C:/Users/Βίκυ!/Desktop/GoogleCodeJam/MagicTrick/RealData/output.txt','w')
cases = int(f.readline())
def skiplines(f,lines):
    for j in range(lines):
        next(f)
for i in range(cases):
    firstnum = int(f.readline())
    skiplines(f,firstnum-1)
    firstrow = f.readline().strip().split()
    skiplines(f,4-firstnum)
    secondnum = int(f.readline())
    skiplines(f,secondnum-1)
    secondrow = f.readline().strip().split()
    skiplines(f,4-secondnum)
    hits = 0
    firsthit = -1
    for j in firstrow:
        if j in secondrow:
            hits = hits + 1
            firsthit = j
    else:
        if hits == 0:
            fout.write('Case #{}: Volunteer cheated!\n'.format(i+1))
        elif hits == 1:
            fout.write('Case #{}: {}\n'.format(i+1,firsthit))
        else:
            fout.write('Case #{}: Bad magician!\n'.format(i+1))
