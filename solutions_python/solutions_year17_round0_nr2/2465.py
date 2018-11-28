my_file = open("B-large.in","r")

n=  int(my_file.readline())
a=[]
b=[]

for i in range(n):
    c=my_file.readline()
    a.append(c)
    b.append([0]*(len(a[i])-1))
    for j in range(len(b[i])):
        b[i][j]=(ord(a[i][j])-48)
    f=0
    for j in range(len(b[i])):
        if j+1<len(b[i]) and b[i][j]>b[i][j+1]:
            b[i][j]=b[i][j]-1
            for k in range(j+1,len(b[i])):
                b[i][k]=9
            f=1
            k=j
            break
    if f==1:
        for j in range(k,0,-1):
          if b[i][j-1]>b[i][j]:
                b[i][j-1]=b[i][j-1]-1
                b[i][j]=9
my_file_out = open("output.txt","w")
for i in range(n):
    for j in range(len(b[i])):
        if b[i][j]!=0:
            k=j
            break
    my_file_out.write("Case #%d: " %(i+1))
    for j in range(k,len(b[i])):
        my_file_out.write("%d" %(b[i][j]))
    my_file_out.write("\n")





