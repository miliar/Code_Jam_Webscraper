fob=open('A-small-attempt5.in.txt','r')
caseNum=int(fob.readline())
for x in range(0,caseNum):
    ans1=fob.readline().split()
    f1=fob.readline().split()
    f2=fob.readline().split()
    f3=fob.readline().split()
    f4=fob.readline().split()
    ans2=fob.readline().split()
    s1=fob.readline().split()
    s2=fob.readline().split()
    s3=fob.readline().split()
    s4=fob.readline().split()
    t=[]
    u=[]
    if ans1[0]=='1':
        for i in range(0,4):
            t.append(f1[i])
    elif ans1[0]=='2':
        for i in range(0,4):
            t.append(f2[i])
    elif ans1[0]=='3':
        for i in range(0,4):
            t.append(f3[i])
    elif ans1[0]=='4':
        for i in range(0,4):
            t.append(f4[i])
    if ans2[0]=='1':
        for i in range(0,4):
            u.append(s1[i])
    elif ans2[0]=='2':
        for i in range(0,4):
            u.append(s2[i])
    elif ans2[0]=='3':
        for j in range(0,4):
            u.append(s3[j])
    elif ans2[0]=='4':
        for i in range(0,4):
            u.append(s4[i])
    stack=[]
    for y in range(0,4):
        for z in range(0,4):
            if t[y]==u[z]:stack.append(t[y])
    if len(stack)==0:print("Case #"+str(x+1)+": "+"Volunteer cheated!")
    elif len(stack)>1:print("Case #"+str(x+1)+": "+"Bad magician!")
    elif len(stack)==1:print("Case #"+str(x+1)+": "+str(stack[0]))
        
