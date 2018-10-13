
f=open("A-large.in","r")
t=int(f.readline().strip("\n"))
f2=open("A-large.out","w")
for y in range(1,1+t):
    l=f.readline().strip("\n").split()
    s=list(l[0])
    k=int(l[1])
    i=0
    c=0
    while True:

        while s[i]=='+' and i<=len(s)-k:
            i+=1

        if i<=len(s)-k:
            for j in range(i,i+k):
                s[j]="+" if s[j]=="-" else "-"
            c+=1
        else:
            break


    r=True
    for j in range (len(s)-k,len(s)):
        if s[j]=="-":
            r=False
    if r:
        f2.write("Case #"+str(y)+": "+str(c)+"\n")
    else:
        f2.write("Case #"+str(y)+": "+"IMPOSSIBLE"+"\n")
f.close()
f2.close()


