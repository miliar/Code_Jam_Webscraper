#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      particle.mania
#
# Created:     14-04-2012
# Copyright:   (c) particle.mania 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()



K=['y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q']

fil=open('C:\Users\particle.mania\Documents\Portable Python 2.7.2.1\inputjam.txt','r')
f = fil.readlines()

FS=f[1:]

def decode(c):
    if(c==' ' or c=='\n'):
        return c
    return K[ord(c)-ord('a')]

i=1
p=''

for l in FS:
    s=p.join(map(decode,list(l)))
    print 'Case #'+str(i)+': '+s,
    i=i+1