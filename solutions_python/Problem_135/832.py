
f=open("qnew.in",'r')

n = int(f.readline().strip('\n'))
nash=open('final.out','w')
k=1
while k <= n:
    

    t=int(f.readline().strip('\n'))
    i=1
    while i <= 4:
        
        
        
        if i==t:
            first=f.readline().strip().split()
        else:
            f.readline()
        i=i+1
        

    tt= int(f.readline())
    j=1
    while j <= 4:
        
        
        if j==tt:
            second=f.readline().strip().split()
        else:
            f.readline()
        j=j+1

    result=0
    num=0
    for i in first:
        for j in second:
            if i==j:
                result=result+1
                num = int(j)
    
    

    if result== 1:
        
        nash.write("Case #"+str(k)+": "+str(num)+"\n" )
        
    elif result == 0:
        nash.write("Case #"+str(k)+": Volunteer cheated!"+"\n" )
        
    else:
        nash.write("Case #"+str(k)+": Bad magician!"+"\n" )
    
    
    k=k+1

f.close()
nash.close()
