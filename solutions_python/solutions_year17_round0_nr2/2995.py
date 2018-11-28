f1=open("input2",'r')
f2=open("output2.txt",'w')
t = int(f1.readline()[:-1])
for k in range(1, t + 1):
    n=str(f1.readline()[:-1])
    l=list(map(int,list(n)))
    i=len(l)-1
    while i>=1:
        if l[i-1]>l[i]:
            l[i-1]=l[i-1]-1
            l[i]=9
            if i<(len(l)-1):
                for j in range(i+1,len(l)):
                    l[j]=9
        i=i-1
    num=0
    for i in l:
        num=(num*10)+int(i)

    f2.write("Case #{}: {}".format(k,num)+'\n')

