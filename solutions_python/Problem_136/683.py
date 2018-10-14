source="C:\Users\Mani\Desktop\cj\B-large.in"
dest="C:\Users\Mani\Desktop\cj\Output.txt"
fin=open(source)
fout=open(dest,'w')
t=int(fin.readline())

for i in range(t):
    p=fin.readline()
    p=p.split(" ")
    p=map(float,p)
    c=p[0]
    f=p[1]
    x=p[2]
    n=0
    s=0
    r=2

    if x<c:
        s=x/r

    else:    
        while n<x:
            s=s+c/r
            n=n+c
            if n>=c:
                a=s+((x-n)/r)
                b=s+((x-(n-c))/(r+f))
                if b<a:
                    n=n-c
                    r=r+f
                else:
                    c=x-n

    fout.write("Case #"+str(i+1)+": "+str(format(s,'.7f'))+"\n")

fin.close()
fout.close()
