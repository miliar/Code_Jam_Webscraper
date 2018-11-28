my_file = open("A-large.in","r")

n= my_file.readline()
n=int(n)
my_file_out = open("output.txt","w")
for i in range(n):
    (a,b)= list(my_file.readline().split())
    b=int(b)
    c=[]
    for j in range(len(a)):
        if a[j]=="-":
            c.append(0)
        else:
            c.append(1)
    count=0
    for j in range(len(a)-b+1):
        if c[j]==0:
            count=count+1
            for k in range(b):
                c[j+k]=1-c[j+k]
    f=0
    for j in range(len(a)):
        if c[j]==0:
            f=1
            break
    if f==0:
        my_file_out.write("Case #%d: %d\n" %(i+1,count))
    else:
        my_file_out.write("Case #%d: IMPOSSIBLE\n" %(i+1))






