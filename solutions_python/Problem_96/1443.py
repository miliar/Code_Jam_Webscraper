a=open("B-large.in","r")
b=open("B-large.out","w")
count=a.readline();
k=1
for t in a:
        b.write("Case #"+repr(k)+": ")
        t=t.split();
        n=int(t[0])
        s=int(t[1])
        p=int(t[2])
        result=0
        for i in range(3,3+n):
                ti=int(t[i])
                if ti%3==0:
                        if ti/3>= p:
                                result+=1
                                continue
                        if s>0 and ti>0:
                                if ti/3+1>=p:
                                        s-=1
                                        result+=1
                                        continue
                elif ti/3+1 >= p:
                        result+=1
                        continue
                elif s>0:
                        if ti%3==0:
                                if ti/3+1>= p:
                                        result+=1
                                        s-=1
                                        continue
                        elif ti/3+2 >= p:
                                if ti%3==1 and ti/3+2==p: continue
                                result+=1
                                s-=1
                                continue
        b.write(repr(result)+"\n")
        k+=1
b.close();
