ans=""
for i in range(int(raw_input())):
    x,r,c=map(int,raw_input().split())
    R="RICHARD"
    G="GABRIEL"
    if x==1:
        t=G
    if x==2:
        if (r*c)%2==0:
            t=G
        else:
            t=R
    if x==3:
        if (r*c)%3==0 and (r*c)>3 :
            t=G
        else:
            t=R
    if x==4:
        if(r*c)==12 or (r*c)==16:
            t=G
        else:
            t=R
   
    ans=ans+"Case #"+str(i+1)+": "+str(t)+"\n"
print ans    
