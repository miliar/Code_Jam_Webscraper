'''
Created on Apr 28, 2012

@author: tfranovic
'''
import sys
inName=sys.argv[1]
outName=inName.replace('.in', '.out')
f1=open(inName, 'r')
out=''
T=int(f1.readline())
for k in range(1,T+1):
    inp=f1.readline().rstrip().split(' ')
    A=int(inp[0])
    B=int(inp[1])
    p=f1.readline().rstrip().split(' ')
    for i in range(0,len(p)):
        p[i]=float(p[i])
    prob={}
    for i in range(1,A+1):
        prob[i]=1.0
        for j in range(0,i-1):
            prob[i]=prob[i]*p[j]
        prob[i]=prob[i]*(1-p[i-1])
    prob[0]=1.0
    for i in range(1,A+1):
        prob[0]=prob[0]-prob[i]
    act=[]
    for i in range(0,len(prob)):
        act.append([])
        for j in range(0,len(prob)):
            if(i==0 and j==0):
                act[i].append(B-A+1)
            else:
                act[i].append(j+(B-(A-j))+1)
                if(not i==0 and not (A-j<i)):
                    act[i][j]=act[i][j]+B+1
        act[i].append(1+B+1)
    minp=0.0
    pp=[]
    for i in range(0,len(prob)+1):
        tp=0.0
        for j in range(0,len(prob)):
            tp=tp+prob[j]*act[j][i]
        pp.append(tp)
    out+='Case #' + str(k)+': '+str(min(pp))+'\n'
f1.close()
f2=open(outName,'w+')
f2.write(out.rstrip("\n"))
f2.close()