file_object=open("in1.in","r")
file_object1=open("output.txt","w")
x=file_object.readline()
x=int(x)
p=0
for line in file_object:
    a=int(line)
    j=a+1
    while j!=0:
        j=int(j)-1
        b=str(j)
        c=int(b[0])
        d=0
        i=1
        while(i<len(b)):
            print j
            if (int(b[i])>c):
                c=int(b[i])
            elif(int(b[i])==c):
                f=i
            else:
                c=b[0:(i+1)]
                for l in range(i+1,len(b),1):
                    c=c+"0"
                j=str(c)
                d=1
                break
            i=i+1
            


        if d==0:
            j=int(j)+1
            print c
            p=p+1
            s="case #"+str(p)+": "+str(b)+"\n"
            file_object1.write(s)
            break
        
file_object.close()
file_object1.close()
