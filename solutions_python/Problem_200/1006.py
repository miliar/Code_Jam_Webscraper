
import math



g = open('output.txt', 'w')

f = open('B-large.in', 'r')

t= int(f.readline())
for i in range(t):
    
    arr=list(f.readline())
    arr2=[]
    for j in range(len(arr)-1):
        arr2=arr2+[int(arr[j])]
    res=-1
    for j in range(len(arr2)-1):
        if (arr2[len(arr2)-1 -j] < arr2[len(arr2)-2 -j]):
            res=len(arr2)-2 -j
    res2=-1
    if res!=-1:
        for j in range(res):
            if arr2[j]!=arr2[res]:
                res2=j

    myres=[]
    if res==-1:
        myres=str(arr2).replace("[", "").replace("]", "").replace(", ", "")
    else:
        if res2==-1 and arr2[0]==1:
            myres="9"*(len(arr2)-1)
        else:
            myres = str(arr2[0:res2+1]).replace("[", "").replace("]", "").replace(", ", "")+ str(arr2[res2+1]-1) + "9"*(len(arr2)-2-res2)
    out="Case #"+str(i+1)+": "+ myres+"\n"
    g.write(out)
g.close()
        

