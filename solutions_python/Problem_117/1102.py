#Brute force

data = raw_input()
data2=data.split('\n')
Ncases=int(data2.pop(0))


data3=[map(int,data2[i].split()) for i in range(0,len(data2))]

data4=[]
j=0
for i in range(0,Ncases):
    N=data3[j][0]
    data4.append([data3[i] for i in range(j,j+N+1)])
    j+=N+1




def check(i,j,data):
    n=data[0][0]
    m=data[0][1]
    point=data[i][j]
    row=data[i]
    column=[data[k][j] for k in range(1,n+1)]
    if (max(column) <= point) or (max(row) <= point):
        return True
    else:
        return False
    

def checkCase(case):
    n=case[0][0]
    m=case[0][1]
    for i in range(1,n+1):
        for j in range(0,m):
            if check(i,j,case)==False:
                return "NO"
    return "YES"
            
for i in range(0,Ncases):
    result=checkCase(data4[i])
    print 'Case #{0}: {1}'.format(i+1,result)

##    
    
    
