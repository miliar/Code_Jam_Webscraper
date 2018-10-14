import sys
import math

if __name__=='__main__':
    f=open('dancing.txt','r')
    g=open('output.txt','w')
    T=int(f.readline())
    for i in range(T):
        allvalues=f.readline().split()
        N=int(allvalues[0])
        S=int(allvalues[1])
        p=int(allvalues[2])
        scores=allvalues[3:]
        answer=0
        for j in range(N):
            sc=int(scores[j])
            if sc-p>=(p-1)*2 and sc-p>=0:
                answer=answer+1
            elif int(scores[j])-p< (p-2)*2:
                continue
            elif S>0 and int(scores[j])-p>=(p-2)*2 and sc-p>=0:
                answer=answer+1
                S=S-1
        output='Case #'+str(i+1)+': '+str(answer)+'\n'
        g.write(output)
    f.close()
    g.close()
