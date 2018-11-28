'''
Created on Apr 14, 2012

@author: tfranovic
'''
import sys
trans={}
trans['a']='y'
trans['o']='e'
trans['z']='q'
in1='ejp mysljylc kd kxveddknmc re jsicpdrysi'
out1='our language is impossible to understand'
in2='rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
out2='there are twenty six factorial possibilities'
in3='de kr kd eoya kw aej tysr re ujdr lkgc jv'
out3='so it is okay if you want to just give up'
for i in range(0,len(in1)):
    trans[in1[i]]=out1[i]
for i in range(0,len(in2)):
    trans[in2[i]]=out2[i]
for i in range(0,len(in3)):
    trans[in3[i]]=out3[i]
alph='abcdefghijklmnopqrstuvwxyz'
missing_1=''
missing_2=''
for c in alph:
    if not c in trans:
        missing_1=c
    if not c in trans.values():
        missing_2=c
trans[missing_1]=missing_2

inName=sys.argv[1]
outName=inName.replace('.in', '.out')
f1=open(inName, 'r')
out=''
T=int(f1.readline())
for k in range(1,T+1):
    s=f1.readline().rstrip()
    s2=''
    for c in s:
        s2=s2+trans[c]
    out+='Case #' + str(k)+': ' + s2 +'\n'
f1.close()
f2=open(outName,'w+')
f2.write(out.rstrip("\n"))
f2.close()