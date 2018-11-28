case=int(input())
z=1
while z<=case:
    l=input().split()
    x=int(l[0])
    r=int(l[1])
    c=int(l[2])
    if (r*c)%x!=0:
        print("Case #"+str(z)+": RICHARD")
    elif (x==4 and r==2 and c==4) or (x==4 and r==4 and c==2):
        print("Case #"+str(z)+": RICHARD")
    elif (x==3 and r==1 and c==3) or (x==3 and r==3 and c==1):
        print("Case #"+str(z)+": RICHARD")
    elif (x==4 and r==1 and c==4) or (x==4 and r==4 and c==1):
        print("Case #"+str(z)+": RICHARD")
    elif (x==4 and r==2 and c==2):
        print("Case #"+str(z)+": RICHARD")
    else:
        print("Case #"+str(z)+": GABRIEL")
    z+=1
