'''
Created on Apr 14, 2012

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
    N=int(inp[0])
    S=int(inp[1])
    p=int(inp[2])
    t=[]
    for i in range(3,len(inp)):
        t.append(int(inp[i]))
    c=0
    cand=[]
    for i in range(0,N):
        if(t[i]>(p-1)*3):
            c=c+1
        elif(t[i]>=(p-1)*3-1 and t[i]>=3):
            cand.append(t[i])
    c=c+min(S,len(cand))
    out+='Case #' + str(k)+': '+str(c)+'\n'
f1.close()
f2=open(outName,'w+')
f2.write(out.rstrip("\n"))
f2.close()