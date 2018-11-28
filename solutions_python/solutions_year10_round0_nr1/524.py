'''
Created on May 8, 2010

@author: user1
'''
file = 'A-small-attempt0.in'
file2 = 'A-large.in'
out = 'A-out.txt'
from operator import mod

def onoff(n, k):
    p = pow(2, n)
    snaps = k+1 
    if mod(snaps, p) == 0: return 'ON'
    else: return 'OFF'

def run():
    foo = open(file2, 'r+')
    bar = open(out, 'w')
    n = int(foo.readline())
    for i in range(n):
        info = foo.readline()
        info = info.split(' ')
        ans = onoff(int(info[0]), int(info[1]))
        o ='Case #'+str((i+1))+': '+ans
        print o
        bar.write(o)
        bar.write('\n')
    bar.close()

if __name__ == '__main__':
    run()