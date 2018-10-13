# Written in Python 3.x

import math
import sys

def convertnums(s):

    a = []
    for i in range(len(s)):
        a.append(int(s[i]))
    return a


# fidi = open('test.in','r')
# fidi = open('A-small-attempt0.in','r')
fidi = open('A-large.in','r')

fido = open('test.out','w')

T = fidi.readline()
T = int(T)

for t in range(T):
    line = fidi.readline()
    s = line.split()
    smax = int(s[0])
    people = convertnums(s[1])
    psum = 0
    friends_needed = 0
    for i in range(0,smax+1,1):
        if (i > psum):
            friends_needed += (i - psum)
            psum += (i - psum)
        psum += people[i]
    print('Case #%d: ' % (t+1),'%d' % friends_needed)
    fido.write('Case #%d: ' % (t+1) + '%d' % friends_needed + '\n')

fidi.close()
fido.close()
