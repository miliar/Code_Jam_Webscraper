
def check(n):
    arr=list(str(n))
    le=len(arr)
    if(le==1):
        return 1
    flag=0
    for x in range(le-1):
        if(int(arr[x])>int(arr[x+1])):
            flag=-1
            break
    if(flag==-1):
        return 0
    else:
        return 1
        
    
with open('test.txt','r') as f:
    line=(f.read().splitlines())
    
temp=['1','2','3','4','5','6','7','8','9','0']
final=[]
for x in range(1,int(line[0])+1):
    arr=int(line[x])
    while(not (check(arr))):
        arr=arr-1
    final.append(arr)

with open('final.txt','w') as fi:
    for x in range(int(line[0])):
        fi.write('Case #'+str(x+1)+': '+str(final[x])+'\n')
        
