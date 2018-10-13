q=open("in.txt","r")
b=q.read()
b=b.split()
w=open("out","w")
i=1
z=1
while 1:
    a=b[i]
    c=b[i+1]
    d=a
    ans=0
    while int(d)<int(c):
        d=str(d)
        e=""
        e=d[1:]+d[0]
        l=[]
        for j in range(len(d)-1):
            if int(e)>int(d) and int(e)<=int(c) and e not in l:
                l.append(e)
                ans+=1
                #print d,e
            str(e)
            e=e[1:]+e[0]
        d=int(d)+1
    l="Case #"+str(z)+": "+str(ans)+"\n"
    w.write(l)
    i=i+2
    z+=1
    if i>=len(b):break
w.close()
q.close()
    
