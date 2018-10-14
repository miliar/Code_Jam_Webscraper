T=input()
for j in range(1,T+1):
    n=input()
    b=[]
    for i in range(4):
     l=[int(x) for x in raw_input().split()]
     if(i==n-1):
         b=l
    d=input()
    p=[]
    for i in range(4):
     l=[int(x) for x in raw_input().split()]
     if(i==d-1):
         p=l     
    count=0
    final=0
    for i in p:
        if(i in b):
            final=i
            count+=1
    if(count==1):
        print "Case #",j,": ",final
    elif(count>1):    
        print "Case #",j,": Bad magician!"
    else:
        print "Case #",j,": Volunteer cheated!"
