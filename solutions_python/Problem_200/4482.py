t=int(input(""));
x=[];
for i in range(t):
    k=int(input(""));
    x.append(k);
cnt=1;
for k in x:
    l=[];
    while k>0:
        temp=k;
        while temp>0:
            p=temp%10;
            l.append(p);
            temp=int(temp/10);
        l.reverse();
        z=l;
        str1="".join(str(x) for x in z);
        l.sort();
        p=l;
        str2="".join(str(x) for x in p);
        if str1==str2:
            #print(k);
            break;
        k=k-1;
        l=[];
    print("Case #"+str(cnt)+": "+str(k));
    cnt=cnt+1;
            





