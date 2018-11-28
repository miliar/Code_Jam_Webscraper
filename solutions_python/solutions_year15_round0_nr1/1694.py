a=open("New Text Document.txt","r")
b=a.read().splitlines()
p=open("output.txt","w")
z=int(b[0])
invit=0
line=1
num=0
result=""
for i in range(z):
    temp=b[line]
    line+=1
    x=temp.split(" ")
    n=int(x[0])
    m=x[1]
    for j in range(n+1):
        if (int(m[j])>0) and (j>num):
            invit+=(j-num)
            num+=(j-num)
            num+=int(m[j])
            
        else:
            num+=int(m[j])   
    result+=str(invit)+"\n"
    invit=0
    num=0
print result
p.write(result)
p.close()