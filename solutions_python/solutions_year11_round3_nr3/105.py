# -*- coding: utf-8 -*-
from time import clock
from math import floor
from math import ceil
from re import sub

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
 

    
import sys
sys.setrecursionlimit(30000)

start1 = clock()


f=open('c.inp', 'r')
f1=open('c.out', 'w')
T=int(f.readline())
print (T)


for t in range (1,T+1):

    st=f.readline()
   
   
    n=int(st.split(' ')[0])
    l=int(st.split(' ')[1])
    h=int(st.split(' ')[2])

    
    st=f.readline()    
    v=[]

    for i in range (n):
        v.append(int(st.split(' ')[i]))
        
    print(n,l,h,v)    
 

    div=0
    for i in range (l,h+1):
         #   print(i)
        kon1=0
        for j in range (n): 
         #   print(i,v[j])
            if i>v[j] :
                if i%v[j]!=0:
                 #   print('no del')
                    kon1=1
                    break
                     #   div=i
            if i<v[j] :
                if v[j]%i!=0:
                #    print('no del')
                    kon1=1 
                    break
                     #   div=i

        if kon1==0:
            div=i
            break        
         
    if div!=0:
            
        print (div)
        f1.write('Case #'+str(t)+': '+str(div)+'\n')
    else:
        print('No')
        f1.write('Case #'+str(t)+': NO\n')
 
 
 
 
f.close()
f1.close()
     
end1 = clock()

print (' время= ',end1-start1)
