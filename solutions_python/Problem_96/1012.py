f=open("B1.in","r")
wf=open("out.txt","w+")
for i in range(int(f.readline())):
    c=f.readline()
    s=c.split()
    n=int(s[0])
    surprises=int(s[1])
    p=int(s[2])
    arr=s[3:]
    g=0
    nonSMin=p+p-1+p-1
    SMin=p+p-2+p-2
    for x in arr:
        if int(x)>=nonSMin:
            if nonSMin<=0:
                if int(x)>=p:
                    g+=1
            else:
                g+=1
        elif surprises>0 and int(x)>=SMin:
            if SMin<=0:
                if int(x)>=p:
                    surprises-=1
                    g+=1
            else:
                surprises-=1
                g+=1
    wf.write("Case #"+str(i+1)+": "+str(g)+"\n")
f.close()
wf.close()
