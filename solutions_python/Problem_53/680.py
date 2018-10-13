andar=open("input.in","r")
bahar=open("output.txt","w")
a=int(andar.readline())
counter=1
while(a):
    b=andar.readline()
    b=b.split()
    b[0]=int(b[0])
    b[1]=int(b[1])+1
    if(b[1]%pow(2,b[0])):
        s="Case #"+str(counter)+": "+"OFF"+"\n"
        bahar.write(s)
        counter=counter+1
    else:
        s="Case #"+str(counter)+": "+"ON"+"\n"
        bahar.write(s)
        counter=counter+1
    a=a-1
