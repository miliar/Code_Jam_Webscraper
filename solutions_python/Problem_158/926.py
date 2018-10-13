a=open("input.txt","r")
b=a.read().splitlines()
p=open("small.txt","w")
z=int(b[0])
result=""
for i in range(z):
    o=b[i+1].split(" ")
    x=int(o[0])
    m=int(o[1])
    n=int(o[2])
    if (m*n)%x==0:
        if x>2 :
            if (m*n)>x:
                if min(m, n)>float(x/2):
                    result+="Case #"+str(i+1)+": "+"GABRIEL"+"\n"
                else:
                    result+="Case #"+str(i+1)+": "+"RICHARD"+"\n"
            else:
                result+="Case #"+str(i+1)+": "+"RICHARD"+"\n"
        else:
            
            if (n*m)>=x:
                result+="Case #"+str(i+1)+": "+"GABRIEL"+"\n"
            else:
                result+="Case #"+str(i+1)+": "+"RICHARD"+"\n"
    else:
        result+="Case #"+str(i+1)+": "+"RICHARD"+"\n"
p.write(result)
p.close()