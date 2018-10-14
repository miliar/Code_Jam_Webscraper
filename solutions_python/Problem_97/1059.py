f=open("C-small-attempt0.in", "r");
f1=open("output.txt","w");
str=f.readline();
for i in range(int(str)):
    s=f.readline();
    rez=0;
    li=s.split();
    lng=len(li[1]);
    
    A=int(li[0]);
    B=int(li[1]);
    x=A;
    dic={};
    while x<=B:
        xstr=repr(x);
        for o in range(lng-1):
            br=o+1;
            prvi=xstr[:br];
            drugi=xstr[br:];
            dr=drugi+prvi;
            
            dr=int(dr);
            if dr<x and dr>=A and dr<=B and len(repr(dr))==lng:
                prob=repr(dr)+xstr
                if(0==(prob in dic)):
                    dic[prob]=1;
                    rez=rez+1;
        
        x=x+1;

    ans="Case #"+repr(i+1)+": "+repr(rez);
    if i!=int(str)-1:
        f1.write(ans+"\n");
    else :
        f1.write(ans);
f.close();
f1.close();



        



    
        
