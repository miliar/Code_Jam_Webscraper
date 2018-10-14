#!/usr/bin/python
import sys

# build dictionary
cyp="""ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"""
dec="""our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"""
key={}
for i in range(len(cyp)):
    key[cyp[i]]=dec[i]
   
key['z']='q'
key['q']='z'

def convert(s):
    return ''.join([key[i] for i in s]) 

sys.stdin.readline()

i=1
for l in sys.stdin:
    print "Case #%d: %s" % (i, convert(l.strip()))
    i+=1