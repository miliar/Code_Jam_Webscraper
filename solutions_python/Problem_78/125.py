# -*- coding: utf-8 -*-
from time import clock
from math import floor
from math import ceil



    
import sys
sys.setrecursionlimit(30000)

start1 = clock()


f=open('a.inp', 'r')
f1=open('a.out', 'w')
T=int(f.readline())
print (T)


for t in range (1,T+1):

    st=f.readline()
   
   
    n=int(st.split(' ')[0])
    pd=int(st.split(' ')[1])
    pg=int(st.split(' ')[2])

    d=0
    if (pd<pg and pg==100) or (pd>pg and pg==0):
        d=0
    else:
        for i in range(1,n+1):
            if pd*i%100==0:
                j=i
                vs=pd*i/100
                while True:
          #          print(i,j,vs,j*pg/100)
                    if j*pg%100==0 and vs<=j*pg/100:
                        
                        d=1
                        break
                    else:
                        j=j+1
            if d==1:
                break
    
    
    print ('Case #'+str(t)+' ',d)  
    if d:
        f1.write('Case #'+str(t)+': Possible\n')
    else:
         f1.write('Case #'+str(t)+': Broken\n')   
         
             
            


f.close()
f1.close()
     
end1 = clock()

print (' время= ',end1-start1)
