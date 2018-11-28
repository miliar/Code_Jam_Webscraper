testcases=int(input());
def nsorted(l):
    for i in range(len(l)-1):
        if(l[i]<=l[i+1]):
           pass;
        else:
           return True;
    return False;
def update(l):
    for i in range(len(l)-1):
        if(l[i]>l[i+1]):
               p=int(l[i]);
               p=p-1;
               c=len(l)-i;
               l=l[0:i]+[str(p)]+['9' for i in range(c-1)];
    return l;
for t in range(testcases):
    n=int(input());
    n1=[i for i in str(n)]
    while nsorted(n1) and n>0:
        n1=update(n1);
    s=''.join(n1);
    if(s[0]=='0'):
        print("Case #"+str(t+1)+': '+str(s[1:]));
    else:
        print("Case #"+str(t+1)+': '+str(s));


 
