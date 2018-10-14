'''
Created on 13-Apr-2013

@author: Bijil
'''

import math

case_sol=[]

t=int(raw_input(''));

for j in range(t):
    ab=(raw_input()).split(' ')
    a=int(ab[0])
    b=int(ab[1])
    
    count=0;
    sq=math.sqrt(float(a))
    intsq=int(sq)
    
    if(sq==intsq):
        num=a;
    else:
        num=pow((intsq+1),2)

    
    while(num<=b):
        if num>b:
            break
        if(str(num) == str(num)[::-1]):
            sq=int(math.sqrt(float(num)))
            if(str(sq) == str(sq)[::-1]):
                count=count+1
        sq=math.sqrt(float(num))
        num=int(pow((sq+1),2))
        
    case_sol.append(count)
    
for j in range(t):
    print 'Case #'+str(j+1)+': '+str(case_sol[j])   
        
    