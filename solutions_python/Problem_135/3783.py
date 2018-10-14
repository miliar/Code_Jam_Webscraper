##1 2 3 4
##5 6 7 8
##9 10 11 12
##13 14 15 16

def main():
    ma1=[]
    ma2=[]
    rownum=int(input())
    
    
    for i in range(0,4):
        ma1.append(input().split(" "))
        
    rownum2=int(input())
    for i in range(0,4):
        ma2.append(input().split(" "))
        
    read2(ma2,rownum2,ma1,rownum)
    

def read1(ma1,rownum):
    a=ma1[rownum-1][0]
    b=ma1[rownum-1][1]
    c=ma1[rownum-1][2]
    d=ma1[rownum-1][3]
    return [a,b,c,d]
    
    

def read2(ma2,rownum2,ma1,rownum):
    
        
    table=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range (0,4):
        y=int(ma2[rownum2-1][i])
        table[hash(y)]=y
        
    x=read1(ma1,rownum)
    if checkSame(x,ma2,rownum2) is False:
        
        for t in range(0,4):
            j=int(x[t])
            
            if table[hash(j)]!= 0:
                print("Case #"+str(p)+":",j)
                break
        else:
            print("Case #"+str(p)+": Volunteer cheated!")
                
            
    else:
        print("Case #"+str(p)+": Bad magician!")


def checkSame(x,ma2,rownum2):
    z=read1(ma2,rownum2)
    
    x.sort()
    
    z.sort()
    
    count=0
    for q in x:
        count+=z.count(q)
    
    if x==z:
        return True
    
    elif count>1:
        
        return True
    else:
        
        return False
                
                    
        
    
    
    
T=int(input())
if T <=100 and T>=1:
    for p in range(1,T+1):
        main()    
    
        
