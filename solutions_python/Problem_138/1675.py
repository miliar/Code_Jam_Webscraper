def solve(N,K):
    result=[0,0]


   
    N.sort(reverse=True)
    K.sort(reverse=True)
    n=len(N)
    
    
    i=0
    i2=0
    j=n-1
    e=0
    while(e!=n):
        if(float(N[i])>float(K[i2])):
                result[0]+=1
                i+=1
        else:
            j-=1
        
        i2+=1
        e+=1
    
    
    N.sort(reverse=True)
    K.sort(reverse=True)
    i=0
    i2=0
    j=n-1
    e=0
    while(e!=n):
        if(float(N[i])>float(K[i2])):
            
            if(float(N[i])>float(K[j])):
                result[1]+=1
            j-=1
        else:
            i2+=1
        
        i+=1
        e+=1


   

    return result                    


L=list()
f2 = open('D-large.in','r')
f3 = file('g_4.in','w')
for i in f2:
    tmp=''
    tmp="".join(i)
    r=tmp.split('\n')
    r=r[0].split(' ')
    L.append(r)    
        
  
n=int(L[0][0])

i=2


for k in range(1,n+1):
               
                case=solve(L[i],L[1+i])
                i+=3
                tmp=''
                
                tmp="Case #"+str(k)+": "+str(case[0])+' '+str(case[1])+'\n'
                    
                
                
                f3.write(tmp)





print("end")

f2.close

f3.close



