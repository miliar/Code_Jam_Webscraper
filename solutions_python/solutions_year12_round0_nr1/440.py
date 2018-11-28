#! /usr/bin/env python

import sys

first = lambda (x, y) : x
second = lambda (x, y) : y

class GError(Exception) :
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


s1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
t1 = 'our language is impossible to understand'

s2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
t2 = 'there are twenty six factorial possibilities'

s3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv' 
t3 = 'so it is okay if you want to just give up'

gmap = ['' for i in range(26)]

s = s1 + s2 + s3
t = t1 + t2 + t3

base = ord('a') 
gmap[ord('y')-base] = 'a'
gmap[ord('e')-base] = 'o'
gmap[ord('q')-base] = 'z'

for i in range(len(s)) : 
    if s[i] == ' ' : continue 
    idx = ord(s[i]) - base
    if gmap[idx] == '' : 
        gmap[idx] = t[i]
    elif gmap[idx] != t[i] :
        raise GError("Gmap is not one-to-one!")
    else : 
        continue 

alph = 'abcdefghijklmnopqrstuvwxyz'
gset = frozenset(gmap) 
rest =  filter(lambda x : not (x in gset), alph)
if len(rest) == 1: 
    for i in range(len(gmap)) :
        if gmap[i] != '' : continue 
        gmap[i] = rest
        break
else: 
    raise GError("Cannot construct gmap.")

def gmfunc(x) :
    if x == ' ' : return x
    else : return gmap[ord(x)-base]
    
if len(sys.argv) <= 0 : sys.exit()

fname = sys.argv[1] 
fh = open (fname) 

case_count = int(fh.readline().strip())

for i in range(1, case_count+1) :
    line = fh.readline().strip()
    print "Case #%d: %s" % (i, ''.join(map(gmfunc, line)))
    
fh.close()
