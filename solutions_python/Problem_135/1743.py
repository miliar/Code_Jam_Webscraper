def solve(L,y):
    
    case=0 
    num=int(L[0][0])
  
    a=L[num]
    num=int(L[5][0])

    b=L[num+5]
    t=0
    
        

    t=0
    lens=0

    
    for x in a:
          
           v= b.count(x)
           
           lens+=1
           if(v==1):
                   t+=1

    if(t>1):
                
                return 2

    if(t==0):
                
                return 3
    for x in a:
        for j in b:
            if(j==x):
                y[0]=j
                return 1

   

                               


L=list()
A=list()
index=0



f2 = open('A-small-attempt4.in','r')
f3 = file('g_1.in','w')
for i in f2:
    tmp=''
    tmp="".join(i)
    r=tmp.split('\n')
    r=r[0].split(' ')
    L.append(r)    
        
  
n=int(L[0][0])
print(n)
i=1
j=11
caselist=["Bad magician!","Volunteer cheated!"]
for k in range(0,n):
                u= L[i+k*10:j+k*10]
                
                y=[0]
                case=solve(u,y)
                tmp=''
                if(case==1):
                    tmp="Case #"+str(k+1)+": "+str(y[0])+'\n'
                    
                else:
                    tmp="Case #"+str(k+1)+": "+caselist[case-2]+'\n'

                f3.write(tmp)
                print(tmp)








f2.close

f3.close
