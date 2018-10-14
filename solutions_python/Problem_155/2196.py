#!/usr/bin/python


def getCase(l, k):
    s=c=si=0
    for i in list(l.split(" ")[1]):
        if (s+c)<si:
            c+=1
        si+=1
        s+=int(i)
                
    return "Case #%d: %d\n" % (k, c)

f=open("A-large.in", "r")
fo=open("output.out", "w+")
n=f.readlines()
k=0
for l in n[1:]:
    k+=1
    fo.write(getCase(l.strip(), k))
    
f.close()
fo.close()
    

