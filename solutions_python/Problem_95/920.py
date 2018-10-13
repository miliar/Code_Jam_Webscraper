#!/usr/bin/env python

import sys
import string

fname=sys.argv[1]

i=open(fname,'r')
o=open(fname+'.out','w')

'''readline Split'''
def rls(i):
    out=map(int, string.split(i.readline()))
    return out[0] if len(out)==1 else out

'''Output Case#...'''
def wout(o, i, arg):
    out="Case #"+ str(i)+":"
    out+=" "+''.join(arg)
    o.write(out)

tran={
    ' ':' ',
    '\n':'\n',
    'q':'q',
    'z':'z'
        }
mapto=list('abcdefghijklmnopqrstuvwxyz')
def translate(a):
    try:
        return tran[a]
    except KeyError:
        print "can't find: ", a
        return a

N=rls(i)

ii=["ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
oo=["our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up"]

for y in range(len(ii)):
    for z in range(len(ii[y])):
        tran[ii[y][z]]=oo[y][z]
        try:
            mapto.remove(oo[y][z])
        except:
            pass



print tran
print mapto

for x in range(N):
    temp=i.readline()
    z=map(translate,temp) 
    wout(o, x+1, z)

