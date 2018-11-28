# -*- coding: utf-8 -*-

import sys
import re


def invoke(invokation):
    invoklist=re.findall('\d+\s?[^\d]*',invokation)
    invoklist=[x.strip() for x in invoklist]
    #print'###'
    #print invokation
    #print invoklist
    combos=re.findall('[^\d\s]+',invoklist[0])
    oppos=re.findall('[^\d\s]+',invoklist[1])
    seq=re.findall('[^\d\s]+',invoklist[2])[0]
    #print seq
    
    fseq=[]
    for element in seq:
        if len(fseq)<1:
            fseq.append(element)
        elif [x[:-1] for x in combos].count(fseq[-1]+element)>0:
            fseq.append(combos[[x[:-1] for x in combos].index(fseq[-1]+element)][-1])
            fseq.pop(-2)
        elif [x[:-1] for x in combos].count(element+fseq[-1])>0:
            fseq.append(combos[[x[:-1] for x in combos].index(element+fseq[-1])][-1])
            fseq.pop(-2)
        elif len(set([x+element for x in fseq]) & set(oppos))+len(set([element+x for x in fseq]) & set(oppos))>0:
            fseq=[]
        else:
            fseq.append(element)
    return fseq
    
fin = sys.stdin
#fin=open('Blocal.txt')
for case in range(int(fin.readline())):
    tc=fin.readline()
    print ('Case #%d: %r' % (case+1,invoke(tc))).replace('\'','')
