
from collections import *
from copy import *
from math import *

def multiplication (mul,a,b):
    c = mul[a[-1]][b[-1]]
    if len(a)!=len(b):
        c='-'+c
    if len(c)>2:
        c=c[-1]
    return c

if __name__=='__main__':
    input=open('C-large.in.txt','r+')
    output=open('C-large.out.txt','w+')

    numCases = int(input.readline().strip())
    mul = dict()
    mul['1']=dict()
    mul['1']['1']='1'
    mul['1']['i']='i'
    mul['1']['j']='j'
    mul['1']['k']='k'

    mul['i']=dict()
    mul['i']['1']='i'
    mul['i']['i']='-1'
    mul['i']['j']='k'
    mul['i']['k']='-j'

    mul['j']=dict()
    mul['j']['1']='j'
    mul['j']['i']='-k'
    mul['j']['j']='-1'
    mul['j']['k']='i'

    mul['k']=dict()
    mul['k']['1']='k'
    mul['k']['i']='k'
    mul['k']['i']='j'
    mul['k']['j']='-i'
    mul['k']['k']='-1'
    
    for case in range(1,numCases+1):
        line=input.readline().strip().split()
        l=int(line[0])
        x=int(line[1])
        line=input.readline().strip()
        forward = []
        reverse=[]
        forward.append('1')
        for i in range(l):
           forward.append(multiplication(mul,forward[-1],line[i]))

        reverse.append('1')
        for i in range(1,l+1):
            reverse.append(multiplication(mul,line[-i],reverse[-1]))

        complete = []
        complete.append('1')
        for i in range(3):
            complete.append(multiplication(mul,complete[-1],forward[-1]))
        
        score = 'NO'
        if complete[int(fmod(x,4))]=='-1':
            i=1
            while score=='NO' and i<=l:
                j=0
                while score=='NO' and j<4:
                    if multiplication(mul,complete[j],forward[i])=='i':
                        h=1
                        while score=='NO' and h<=l:
                            k=0
                            while score=='NO' and k<4:
                                if multiplication(mul,reverse[h],complete[k])=='k':
                                    s=j+k+1+int(h+i>l)
                                    if s<=x:
                                        score='YES'
                                k+=1
                            h+=1
                    j+=1
                i+=1    
                    
            
        #print multiplication(mul,'-1','-k')
        #print forward
        #print complete
        output.write("Case #%d: %s\n"%(case,score))
        

    input.close()
    output.close()