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
    f1.write('Case #'+str(t)+':\n')
    st=f.readline()
   
   
    r=int(st.split(' ')[0])
    c=int(st.split(' ')[1])
    #  pd=int(st.split(' ')[1])
  #  pg=int(st.split(' ')[2])
    k=[]  

    for i in range (r): 
        st=f.readline()
     #   print(st)
        k1=[]
        for j in st: 
            if j=='\n':
                break
            k1.append(j)
        k.append(k1)
      
    print('case ',r,c,k)
    
    a=chr(92)
    print(a)    
    kon=0
    for i in range (r): 
        for j in range (c): 
            if i!=r-1 and j!=c-1 and k[i][j]=='#':
                print(i,j)
                if  k[i+1][j]=='#' and k[i][j+1]=='#' and k[i+1][j+1]=='#':
                    k[i][j]='/'
                    k[i+1][j+1]='/'
                    k[i+1][j]=a
                    print(len(k[i+1][j]))
                    k[i][j+1]=a
                else:
                    kon=1
            if kon:
                break
        if kon:
            break                

    for i in range (r):
        for j in range (c):
            if (k[i][j]=='#'):
                kon=1
            if kon:
                break
        if kon:
            break  
            
    if kon:
        print ('imposs')
        f1.write('Impossible\n')
    else:
        for i in range (r):
            print (k[i])
        for i in range (r):
            for j in range (c):
                f1.write(str(k[i][j]))
            f1.write('\n')
            
        
        

    
 #   for i in range (90,100):
 #       print(chr(i))
        
  #  print (ord(input()))
 #   print (rpi)
  #  for i in range(n):
  #      f1.write(str(rpi[i])+'\n')
 
         
             
            


f.close()
f1.close()
     
end1 = clock()

print (' время= ',end1-start1)
