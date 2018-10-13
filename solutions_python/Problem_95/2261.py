'''
Created on 14 avr. 2012

@author: SsqualL
'''

alph="abcdefghijklmnopqrstuvwxyz"
enco="ynficwlbkuomxsevzpdrjgthaq"

f=open('A-small-attempt0.in','r')
f.readline()
r=f.readline()
res=open('output.txt',"w")
i=1
while r!="":
    resultat=""
    for j in range(0, len(r)):
        if r[j]==" ":
            resultat=resultat+" "
        else:
            for k in range(0,26):
                if r[j]==enco[k]:
                    resultat=resultat+alph[k]
    S="Case #"+str(i)+": "+resultat+"\n"
    res.write(S)
    r=f.readline()
    i=i+1