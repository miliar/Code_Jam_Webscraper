
import math


def add(arr1,arr2,a,b):
    if a==0:
        return
    if arr1==[]:
        arr1.append(a)
        arr2.append(b)
        return
    if arr1[len(arr1)-1]==a:
        arr2[len(arr2)-1]+=b
        return
    arr1.append(a)
    arr2.append(b)
    

g = open('output.txt', 'w')

f = open('C-small-2-attempt0.in', 'r')

t= int(f.readline())
for i in range(t):
    
    arr=f.readline().split()
    n=int(arr[0])
    k=int(arr[1])
    arr1=[n]
    arr2=[1]
    cur1=arr1[0]
    cur2=arr2[0]

    while k>cur2:
        arr1= arr1[1:len(arr1)]
        arr2= arr2[1:len(arr2)]
        
        
        add(arr1,arr2,math.floor(cur1/2),cur2)
        add(arr1,arr2,math.floor((cur1-1)/2),cur2)
        
        k=k-cur2
        cur1=arr1[0]
        cur2=arr2[0]
    out="Case #"+str(i+1)+": "+str(math.floor(cur1/2)) +" "+ str(math.floor((cur1-1)/2))+"\n"
    g.write(out)
g.close()
        

