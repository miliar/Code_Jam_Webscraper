final=[]
l=[]
flag=0
index=0
ll=[]
count=0
with open('B-large.in','r') as f:
    #other options with f:-
    #f.readline() f.readlines(),reads all the lines of the file
    for line in f:
        int_list = [int(i) for i in line.split()]
        ll.append(int_list)

t=ll[0][0]
for i in range(t):
    n=ll[i+1][0]
    n=str(n)
    for j in n:
        l.append(int(j))
    #print l
    loop=range(1,len(l))
    for j in reversed(loop):
       
        if l[j]<l[j-1]:
            for k in xrange(j,len(l)):
                l[k]=9
            l[j-1]=l[j-1]-1
              
    a=0
    #print l
    for k in range(len(l)):
        power=(len(l)-k-1)
        a=a+l[k]*(10**power)
    #print a
    #print n
    sum_=0    
    for p in l:
        sum_=sum_+p
    if len(l)>1 and sum_!=len(l)*l[0] and count==1:
        a=a-1
    flag=0
    l=[]
    count=0
    final.append(a)
fo=open("out.txt","wb")
for i in range(t):
    fo.write("Case #"+str(i+1)+": "+str(final[i])+"\n")

fo.close()    

print final
