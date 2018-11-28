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


f=open('b.inp', 'r')
f1=open('b.out', 'w')
T=int(f.readline())
print (T)


for t in range (1,T+1):

    st=f.readline()
   
 #  L, t, N and C, followed by C integers ai,  
    l=int(st.split(' ')[0])
    vr=int(st.split(' ')[1])
    n=int(st.split(' ')[2])
    c=int(st.split(' ')[3])  

    
    
    v=[]
    v1=list(range(n))
    for i in range (4,4+c):
        v.append(2*int(st.split(' ')[i]) )
    
    j=0    
    for i in range (n):
        if i%c==0:
            j=0
        v1[i]=v[j]
        j+=1
        
 #   print(l,vr,n,c,v1,v)
    
    sum=0
    for i in range (n):
        sum+=v1[i]
    sm=sum    
    print('sum',sum)
    
    if l==0:
        sum=sm
    else:
    
        sum=0
        s=0
        for i in range (n):
            sum+=v1[i]   
            if sum>=vr and s==0:
                mas1=v1[0:i]
                mas1.insert(len(mas1),v1[i]-(sum-vr))
                mas=v1[i+1:len(v1)]
                mas.insert(0, sum-vr)
                s=1
                sum=sum-(sum-vr)
                break
             #   print(i+1,len(v1),v1[i+1:len(v1)])
             #   for i in range (n):
             #       sum+=v1[i]             
        
     #   print(vr,mas1,mas)
        
        i = len(mas)
        while i > 1:
           for j in range(i - 1):
               if mas[j] <mas[j + 1]:
                   swap(mas, j, j + 1)
           i -= 1
        
        for i in range (l):
            if i<len(mas):
                mas[i]=mas[i]/2.0
                
      #  print('ost=',mas)
        
        sum=0
        
        for i in range (len(mas1)):
            sum=sum+mas1[i]    
        
        for i in range (len(mas)):
            sum=sum+mas[i]

  #  if sum%2==0:
  #      print('otv',round(sum))
  #  else:
  #      print('otv',sum)        
    

        
    if sum>sm:
        print('error', str(t)+' : '+str(round(sum))+'  '+str(sm))
        exit()
    print ('Case #'+str(t)+' : '+str(round(sum))+'  '+str(sm))
    if sum%2==0:
        f1.write('Case #'+str(t)+': '+str(round(sum))+'\n')
    else:
        f1.write('Case #'+str(t)+': '+str(round(sum))+'\n') 
   
 

 
f.close()
f1.close()
     
end1 = clock()

print (' время= ',end1-start1)
