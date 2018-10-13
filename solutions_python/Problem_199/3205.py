#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import collections

fi = open("/sdcard/qpython/scripts/A-large.in","r")
fo = open("/sdcard/qpython/scripts/output","w")

num = int(fi.readline())

for j in range(num):
    inst = fi.readline().split()
    seq = inst[0]
    pstack = []
    for i in range(len(seq)):
        if seq[i]=='+':
            pstack = pstack+[1]
        else:
            pstack = pstack+[0]
    k = int(inst[1])
    print pstack
    
    lastflip = 0
    numflips = 0
    fail = False
    answer = ""

    while min(pstack)==0:
        nowflip = pstack.index(0)
        if nowflip < lastflip or nowflip > len(seq)-k:
            fail = True
            break
        else:
            pstack = pstack[:nowflip]+[1-i for i in pstack[nowflip:nowflip+k]]+pstack[nowflip+k:]
            numflips += 1
            lastflip = nowflip
        
    if fail:
        answer = "IMPOSSIBLE"
    else:
        answer = str(numflips)
    
    fo.write("Case #"+str(j+1)+": "+answer+"\n")
    print i
fo.close()
fi.close()