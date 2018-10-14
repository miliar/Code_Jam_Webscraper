f=open("B-large.in", "r");
o=open("output.txt","w");
str=f.readline();
for i in range(int(str)):
    s=f.readline();
    rez=0;
    li=s.split();
    n=li.pop(0);
    sup=li.pop(0);
    sup=int(sup);
    p=li.pop(0);
    
    p=int(p);
    mali=p-1;
    if mali<0:
        mali=0;
    
    manji=p-2;
    if manji<0:
        manji=0;
    proba=mali+mali+p;
    druga=manji+manji+p;
    
    for x in li:
        x=int(x);
        if proba<=x:
            rez=rez+1;
        elif sup>0:
            
            if druga<=x:
                
                rez=rez+1;
                sup=sup-1;
    ans="Case #"+repr(i+1)+": "+repr(rez);
    if i!=int(str)-1:
        o.write(ans+"\n");
    else :
        o.write(ans);

f.close();
o.close();
