
import math



f2 = open('output.txt', 'w')

f1 = open('B-large (2).in', 'r')

t= int(f1.readline())
for i in range(t):
    s=f1.readline().split()
    ac=int(s[0])
    aj=int(s[1])
    arr=[]
    for j in range(ac):
        s=f1.readline().split()
        arr.append([int(s[0]),int(s[1]),0])
    for j in range(aj):
        s=f1.readline().split()
        arr.append([int(s[0]),int(s[1]),1])
    arr=sorted(arr)
    c=[0,0]
    c[arr[0][2]]=arr[0][1]-arr[0][0]
    
    
    for j in range(1,ac+aj):
        c[arr[j][2]]=c[arr[j][2]] + arr[j][1]-arr[j-1][1]
        if arr[j][2]!=arr[j-1][2]:
            c[arr[j-1][2]]=c[arr[j-1][2]] + arr[j][0]-arr[j-1][1]
    tmp=arr[0][0]+60*24-arr[ac+aj-1][1]
    if arr[0][2]==arr[ac+aj-1][2]:
        c[arr[0][2]]=c[arr[0][2]]+tmp
    else:
        c[0]=c[0]+tmp
        c[1]=c[1]+tmp
    res=0
    for j in range(1,ac+aj):
        if arr[j][2]!=arr[j-1][2]:
            res=res+1
    if arr[0][2]!=arr[ac+aj-1][2]:
        res=res+1
    l=[[],[]]
    for j in range (1,ac+aj):
        if arr[j][2]==arr[j-1][2]:
            l[arr[j][2]].append(arr[j][0]-arr[j-1][1])
    if arr[0][2]==arr[ac+aj-1][2]:
        l[arr[0][2]].append(arr[0][0]+60*24-arr[ac+aj-1][1])
    sortl=[[],[]]
    sortl[0]=sorted(l[0],reverse=True)
    sortl[1]=sorted(l[1],reverse=True)
    ind=0

    for j in range(2):
        while c[j] < 12*60:
            c[j]=c[j] + sortl[1-j][ind]
            ind=ind+1
            res=res+2
    
    
            
        
    
    f2.write("Case #" +str(i+1) +": "+str(res) + "\n")
f2.close()
        

