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


f1=open('c.inp', 'r')
N=int(f1.readline())-1
print (N)



a=''
b=list(range(N+1))
a1=list(range(N+1))


c=list(range(N+1))
f2=open('c.out', 'w')
print ('answer')
for i in range(N+1):
    kol=int(f1.readline())-1
   # print (kol)
 
    
    a=f1.readline()
    if a[len(a)-1]=='\n':
        a=a[:-1]

    b[i]=a.split(" ")

  #  print (b[i]) 
    
    cik=list(range(2**(kol+1)-1))
  #  cik=list(range(1000))
  #  cik[0]=list(range(1000))
    
    O=0
    
  #  for j in range(1,1000): 
  #      cik[j]=list(range(1000))
  #      cik[j]=raz1(j)
  #      print (cik[j])
    
    
    for j in range(kol+1): 
        O=O+int(b[i][j])
        
    if O%2==1:
      #  print ('NO')
        print ('Case #'+str(i+1)+': NO')
        f2.write('Case #'+str(i+1)+': NO')
 
    else:
        
     
    
            for j in range(1,2**(kol+1)-1): 
                cik[j]=list(range(kol))
                cik[j]=raz(j)
            
            mx=0
            for j in range(1,2**(kol+1)-1):
           #     print (cik[j])
                S=0
                S1=0
                S2=0
                tm=0
              #  print (b[i])
             #   print (cik[j])
                for g in range(kol+1):
                #    print (j,g)
                    if cik[j][g]==0:
                        S=S+int(b[i][g])
                       
                     #   tm=sb(sum(raz1(S2),raz1(int(b[i][g]))))
                     #   S2=tm
                        S2=S2^int(b[i][g])
                        
                 #       print ('S2=',int(b[i][g]),raz1(int(b[i][g])),S2,raz1(S2),sum(raz1(S2),raz1(int(b[i][g]))),sb(sum(raz1(S2),raz1(int(b[i][g])))))
                       
                    else:
                 #       print ('S1=',int(b[i][g]),raz1(int(b[i][g])),S1,raz1(S1),sum(raz1(S1),raz1(int(b[i][g]))),sb(sum(raz1(S1),raz1(int(b[i][g])))))
                       # tm=sb(sum(raz1(S1),raz1(int(b[i][g]))))
                       
                        S1=S1^int(b[i][g])

                        
                        
                        
             #   print (i,j,g,S,S1, cik[j],b[i])
                
#                print (S,s1,S1,s2)
                
                  
                #    print ('SO',O,'SR',S,'S1',S1,'S2',S2)
        
                if S2==S1:
                    if mx<S:
                        mx=S
                   #     print (cik[j])
                
                        
          #  print('mx',mx)
            if mx==0:
                print ('Case #'+str(i+1)+': NO')
                f2.write('Case #'+str(i+1)+': NO')
            else:
                print ('Case #'+str(i+1)+': '+str(mx))
                f2.write('Case #'+str(i+1)+': '+str(mx))
 
        
         
        


    f2.write('\n')
f2.close()
 
#for i in range(N+1):
 #   print(a[i]) 


f1.close()


end1 = clock()

print (' время= ',end1-start1)
