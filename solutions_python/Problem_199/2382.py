def solve(fl):
    a=fl.split()
    s=list(a[0])
    k=int(a[1])
    l=len(s)
    f=0
    for i in range (l):
        if s[i]=="-" and i<l-k+1:
            for j in range(k):
                if s[i+j]=="+":
                    s[i+j]="-"
                else:
                    s[i+j]="+"
            f+=1
    i=l-k
    p=True
    while p and i<l:
        if s[i]=="-":
            p=not p
        i+=1
    if p:
        return str(f)
    else:
        return "IMPOSSIBLE"
        
fi = open("A-large.in","r")
fo = open("A-large.out","w")

n = int(fi.readline())

for i in range(1,n+1):
    fl = fi.readline()
    o= "Case #"+str(i)+": "+solve(fl)
    #print o
    fo.write(o+"\n")

fo.close()
fi.close()
print "Done!"
