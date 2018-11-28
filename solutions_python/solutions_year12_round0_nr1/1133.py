f=open("A-small-attempt0.in", "r");
o=open("out.txt","w");
str=f.readline();
for i in range(int(str)):
    s=f.readline();
    r='';
    for j in s:
        if j=='a':
            r+='y';
        elif j=='b':
            r+='h';           
        elif j=='c':
            r+='e';
        elif j=='d':
            r+='s';
        elif j=='e':
            r+='o';    
        elif j=='f':
            r+='c';
        elif j=='g':
            r+='v';
        elif j=='h':
            r+='x';           
        elif j=='i':
            r+='d';
        elif j=='j':
            r+='u';
        elif j=='k':
            r+='i';    
        elif j=='l':
            r+='g';
        elif j=='m':
            r+='l';
        elif j=='n':
            r+='b';           
        elif j=='o':
            r+='k';
        elif j=='p':
            r+='r';
        elif j=='q':
            r+='z';    
        elif j=='r':
            r+='t';
        elif j=='s':
            r+='n';
        elif j=='t':
            r+='w';           
        elif j=='u':
            r+='j';
        elif j=='v':
            r+='p';
        elif j=='w':
            r+='f';    
        elif j=='x':
            r+='m';
        elif j=='y':
            r+='a';    
        elif j=='z':
            r+='q';
        else:
            r+=j;
    ans="Case #"+repr(i+1)+": "+r;
    print ans
    o.write(ans);
f.close();
o.close();
