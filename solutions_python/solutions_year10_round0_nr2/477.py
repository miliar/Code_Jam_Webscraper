import glob
import os

#len(t)>1
#t[i]>=t[i+1]
def diffs(t1):
    return [t1[i-1]-t1[i] for i in range(1,len(t1))]

#len(t)>1
def gcf_list(t2):
    gcf=t2[0]
    for i in range(1,len(t2)):
        gcf=euc(gcf,t2[i])
    return gcf
        
def euc(a,b):
    if(a==0):
        return b
    while(b!=0):
        if(b>a):
            tt=a
            a=b
            b=tt
        tt=b
        b=a%b
        a=tt
    return a
        
for fname in glob.glob("*.in"):
    fin=open(fname, "r")
    fout=open(fname + ".out", "w+")
    output=[]

    
    for casenum in range(1,1+int(fin.readline())):
        t=[int(x) for x in fin.readline().split()[1:]]
        t.sort()
        t.reverse()
        gcf2=gcf_list(diffs(t))
        if(gcf2<=1): res=0
        else: res=gcf2-(t[-1]%gcf2)
        if(gcf2==res): res=0
        output.append("Case #%i: %i"%(casenum,res))
        print([x+res for x in t])

    fin.close()
    fout.write("\n".join(output))
    fout.close()

