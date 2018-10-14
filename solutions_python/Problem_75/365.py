# !\usr\bin\python
import sys

n=int(sys.stdin.readline())
old=n
while n>0:
    n=n-1
    xs=sys.stdin.readline().split()
    i=0
    j=-1
    cmb=int(xs[i])
    cm=[]
    for j in range(cmb):
        cm.append(xs[i+j+1])
    i=i+j+2
    j=-1
    ops=int(xs[i])
    opp=[]
    for j in range(ops):
        opp.append(xs[i+j+1])
    i=i+j+2
    nb=int(xs[i])
    out=[]
    opout=[]
    for k in range(nb):
        out.append(xs[i+1][k])
        while 1:
            change=0
            for l in cm:
                if len(out)>1 and ((out[-2:][0]==l[0] and out[-2:][1]==l[1]) or (out[-2:][1]==l[0] and out[-2:][0]==l[1])):
                    out=out[:-2]
                    out.append(l[2])
                    change=1
            if change==0:
                break
        if len(out)>0 and (out[-1:][0] in opout):
            out=[]
        
        opout=[]
        for l in out:
            for m in opp:
                if l == m[0]:
                    opout.append(m[1])
                if l == m[1]:
                    opout.append(m[0])
    if out==[]:
        print "Case #" + str(old-n) + ": []"
    elif len(out)==1:
        print "Case #" + str(old-n) + ": [" + out[0] + "]"
    else:
        print "Case #" + str(old-n) + ": [" + out[0] + ",",
        for m in out[1:-1]:
            print m + ",",
        print out[-1:][0] + "]"
