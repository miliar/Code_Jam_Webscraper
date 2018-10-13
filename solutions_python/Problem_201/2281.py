import numpy as np
import sys
import itertools

f=open('C-large.in', 'r')
f2=open('bathroom_output3.ou', 'w')

init=0
case=1
aliii=int(f.readline())


while case<= aliii:
    b=f.readline().split(' ')
    #print b
    N=int(b[0])
    K=int(b[1])
    #b_ocup=[1]+ [0]*N+[1]
    #b_ocup=np.array(b_ocup)
    people=0
    zeros=[(N,1)]
    #ones=[1,1]
    counter=1
    while(people+1<K):

        zeros_next=[]
        
        for aux in zeros[::-1]:
            #print zeros_next
            
            if aux[0]%2==0:
                if len(zeros_next)!=0:
                    
                    if aux[0]/2==zeros_next[0][0]:
                        zeros_next[0][1]+=1
                    else:
                        zeros_next=[[aux[0]/2,aux[1]]]+zeros_next
                    if aux[0]/2-1==zeros_next[-1][0]:
                        #zeros_next=[[aux[0]/2,aux[1]]]+zeros_next
                        zeros_next[-1][1]+=aux[1]
                    else:
                        zeros_next=zeros_next+[[aux[0]/2-1,aux[1]]]
                    
                    #if aux[0]/2!=zeros_next[0][0] and aux[0]/2-1!=zeros_next[-1][0]:
                    #    zeros_next=[[aux[0]/2,aux[1]]]+zeros_next+[[aux[0]/2-1,aux[1]]]
                        
                else:
                #print aux
                    
                    zeros_next=[[aux[0]/2,aux[1]]]+zeros_next+[[aux[0]/2-1,aux[1]]]
            else:
                if len(zeros_next)!=0:
                    if (aux[0]-1)/2==zeros_next[-1][0]:
                    
                        zeros_next[-1][1]+=aux[1]*2
                    elif (aux[0]-1)/2==zeros_next[0][0]:
                        zeros_next[0][1]+=aux[1]*2
                    else:
                        zeros_next=zeros_next+[[(aux[0]-1)/2,aux[1]*2]]
                else:
                    
                    zeros_next=zeros_next+[[(aux[0]-1)/2,aux[1]*2]]
        
            #print zeros_next
        people=people+2**counter        
        zeros=zeros_next
        #print people
        #print zeros
        counter+=1
    
        
    #print people
    #print counter
    #print K-(people-2**(counter-1))-2
    
    cumsum=0
    for aux in zeros:
        cumsum+=aux[1]
        if K-(people-2**(counter-1))-2<cumsum:
            max_zeros=aux[0]
            break
    #max_zeros=zeros[K-(people-2**(counter-1))-2]
    #print max_zeros
    
    if max_zeros%2==0:
        max_min=max_zeros/2-1
        max_max=max_min+1
    else:
        max_min=(max_zeros-1)/2
        max_max=max_min
     
    if K==1:
        if N%2==0:
            max_min=N/2-1
            max_max=max_min+1
        else:
            max_min=(N-1)/2
            max_max=max_min
        
        
    #print b_ocup
    print  'Case #'+str(case)+": "+str(max_max)+' '+str(max_min)
    f2.write('Case #')
    f2.write(str(case))
    f2.write(': ')
    f2.write(str(max_max)+' '+str(max_min))
    f2.write('\n')
    case+=1
    print "----------------------------------"
    #num_list=np.array(list(b.split('\n')[0]))