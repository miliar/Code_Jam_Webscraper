# -*- coding: utf-8 -*-
from time import clock
from math import floor
from math import ceil

def raz(ch):
    s=list(range(kol+1))
    for i in range(kol):
        s[i]=0
    
    i=kol
    n = ""
     
    while ch > 0:
        y = str(ch % 2)
        n = y + n
        ch = int(ch / 2)
        s[i]=int(y)
    #    print(y)
        i=i-1
  #  print (s)
    return s


   

def raz1(ch):
    s=list(range(1000))
    for i in range(kol):
        s[i]=0
    
    i=999
    n = ""
     
    while ch > 0:
        y = str(ch % 2)
        n = y + n
        ch = int(ch / 2)
        s[i]=int(y)
    #    print(y)
        i=i-1
  #  print (s)
    s=s[i+1:1000]
    return s

def sum(s1,s2):

    k1=len(s1)
    k2=len(s2)

    
    if k1<k2:
        k=k2
    else:
        k=k1
        
    c=list(range(k))        
    for i in range(1,k+1):
      #  print (-i,i,k1,k2)
        c[-i]=0
        if i<=k1 and i<=k2:
            if s1[-i]==1 and s2[-i]==1:
                c[-i]=0
            else:
                c[-i]=s1[-i]+s2[-i]
            if c[-i]==2:
                 c[-i]==0
        #    print(i,s1[-i],s2[-i],c[-i])
                 
        elif i<=k2:
         #   print(i,s2[-i])
            c[-i]=s2[-i]
        elif i<=k2:
            c[-i]=s1[-i] 
         #   print(i,s1[-i])             
                 
    return c
 
def sb(s):
    sm=0
    for i in range(1,len(s)+1): 
      #  print (s[-i],2**i)
        if s[-i]==1:
            sm=sm+2**(i-1)
    return sm
   
    
import sys
sys.setrecursionlimit(30000)

start1 = clock()


f1=open('a.inp', 'r')
N=int(f1.readline())-1
print (N)



a=''
b=list(range(N+1))
a1=list(range(N+1))


c=list(range(N+1))
f2=open('a.out', 'w')
print ('answer')
for i in range(N+1):
  
   # print (kol)
 
    
    a=f1.readline()
    if a[len(a)-1]=='\n':
        a=a[:-1]
    b[i]=(a.split(" "))
    kol=int(b[i][0])
    b[i]=b[i][1:]

  #  print (kol, b[i]) 
        
    na=1
    na1=1
    na2=1
    k1=0
    k2=0
    s=0
    s1=0
    s2=0
    zap=0
    zap1=0 
    zap2=0    
    an=0
    pk1=0
    pk2=0
    h=1
 
    for j in range(len(b[i])-1):
        if b[i][j]=='O':
            if abs(int(b[i][j+1])-na1)+1>k2:
                s=s+abs(int(b[i][j+1])-na1)+1-k2
                k1=k1+abs(int(b[i][j+1])-na1)+1-k2
                if int(b[i][j+1]==na2) and abs(int(b[i][j+1])-na1)+1==k2 :
                    s=s+1 
            else:
                s=s+1
      

                
          #  s=s+abs(int(b[i][j+1])-na1)+1
                k1=k1+1
        #    print ('O',b[i][j+1],'=',na2,k2,'=',abs(int(b[i][j+1])-na1)+1)   
     #       if int(b[i][j+1]==na2) and abs(int(b[i][j+1])-na1)+1==k2 :
      #              s=s+1     
             #       print('q')                    
            na1=int(b[i][j+1])

            #  pk1=


            k2=0
        
            
        if b[i][j]=='B':
            if abs(int(b[i][j+1])-na2)+1>k1:
                s=s+abs(int(b[i][j+1])-na2)+1-k1
                k2=k2+abs(int(b[i][j+1])-na2)+1-k1
                if  na1==int(b[i][j+1])  and abs(int(b[i][j+1])-na2)+1==k1:
                    s=s+1  
            else:

                s=s+1

        #    s=s+abs(int(b[i][j+1])-na2)+1
                k2=k2+1 
        #    print ('B',na1,'=',b[i][j+1],k1,'=',abs(int(b[i][j+1])-na2)+1)   
      #      if  na1==int(b[i][j+1])  and abs(int(b[i][j+1])-na2)+1==k1:
       #             s=s+1        
           #         print('q')
            na2=int(b[i][j+1])   
  
         #   print(k1)

            k1=0
        if s1!=s:
     #       print ('ход',h,b[i][j],b[i][j+1],s-s1)
            s1=s
            h=h+1
        #     print (s1)
    #    if b[i][j]=='O' or b[i][j]=='B':
    #        print ('ход',b[i][j],b[i][j+1],na1,na2,k1,k2,s) 
 #   print ('s=',s)         
    print ('Case #'+str(i+1)+' ',s)  
    f2.write('Case #'+str(i+1)+': '+str(s))

 
        
         
        


    f2.write('\n')
f2.close()
 
#for i in range(N+1):
 #   print(a[i]) 


f1.close()


end1 = clock()

print (' время= ',end1-start1)
