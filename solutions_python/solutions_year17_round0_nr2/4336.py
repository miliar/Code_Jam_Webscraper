fd=open("B-small-attempt6.txt")
z=fd.read()
z=z.rstrip()
z=z.split("\n")
t=z[0]
fd1=open("output.txt","w")
for i in range(1,int(t)+1):
    n=z[i]
    if int(n)<10:
        fd1.write("Case #"+str(i)+": "+str(n))
        fd1.write("\n")
    else:
        for j in range(int(n),8,-1):
            if int(j)==9:
                fd1.write("Case #"+str(i)+": "+str(j))
                fd1.write("\n")
                break    
            a=list(str(j))
            if sorted(a)==a:
                fd1.write("Case #"+str(i)+": "+str(j))
                fd1.write("\n")
                break
fd1.close()
fd.close()

