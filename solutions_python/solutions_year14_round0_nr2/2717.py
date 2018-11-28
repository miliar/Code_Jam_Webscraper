fi=open("B-large.in","r")
fo=open("1b.out","w")
lst=(fi.read()).split("\n")
n=int(lst[0])
del lst[0]
i=0
flag=1
yes=1
while i<n:
    line=(lst[i]).split(" ")
    c=float(line[0])
    f=float(line[1])
    x=float(line[2])
    s=2.0
    time=0.0
    i=i+1
    while yes:
        if (time+(c/(s)+(x/(s+f))))>(time+(x/s)):
            time=time + (x/s)
            s="Case #"+str(i)+": "+str(time)+"\n"
            fo.write(s)
            break
        elif (c/s < x/s):
            time=time + (c/s)
            s=s+f         
fi.close()
fo.close()
    
   
