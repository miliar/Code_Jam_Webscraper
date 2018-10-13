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
    nums=f1.readline().rstrip().split(' ')
    A=int(nums[0])
    B=int(nums[1])
    d={}
    for n in range(A,B+1):
        for i in range(1,len(str(n))):
            nn=((n%(10**i))*(10**(len(str(n))-i)))+(n/(10**i))
            if nn>=A and nn<=B and n!=nn and len(str(n))==len(str(nn)):
                d[(min(n,nn),max(n,nn))]=1
    out+='Case #' + str(k)+': '+str(len(d))+'\n'
f1.close()
f2=open(outName,'w+')
f2.write(out.rstrip("\n"))
f2.close()