#!/usr/bin/python

import sys,re

strin = list("ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y e q z")

strout = list("our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a o z q")

keymap= {}
for i in xrange(len(strin)):
    keymap[strin[i]] = strout[i]

print keymap
blank = re.compile("^\s+$")

fin = file(sys.argv[1])
keys = keymap.keys()
linecount = int(fin.readline().strip())

f = open('output.txt', 'w')
for i in xrange(0,linecount):
    line = fin.readline().strip() 
    a = "".join(keymap[x] if x in keys else x for x in line)
    if i+1 == linecount:
        f.write('Case #'+str(i+1)+': '+a)
    else: 
        f.write('Case #'+str(i+1)+': '+a+"\n")
f.close()    
