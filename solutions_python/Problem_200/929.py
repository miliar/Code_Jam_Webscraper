with open("B-large.in") as file:
    arr=file.readlines()
cases=int(arr[0])
for case in range(cases):
    s=list(arr[case+1].rstrip())
    l=len(s)
    pos=0
    tidy=False
    while pos<l-1:
        if(int(s[pos+1])<int(s[pos])):
           for i in range(pos+1,len(s)):
               s[i]="9"
           s[pos]=str(int(s[pos])-1)
           pos-=2
        pos+=1
        if(pos<0):
            pos=0
    n=int("".join(s))
    print("Case #{}: {}".format(case+1,n))
