t=int(raw_input().strip())
for i in range(t):
    inp=list(raw_input().strip())
    change=0
    change1=[0 for x in range(len(inp))]
    j=len(inp)-1
    y=0
    while(j>0):
        if(int(inp[j])<int(inp[j-1]) and len(str(int("".join(inp))-1))==len(inp)):
            inp[j]="9"
            change1[j]=1
            if(inp[j-1]=="9" and change1[j-1]==1):
                y=1
            else:
                inp[j-1]=str(int(inp[j-1])-1)
            change=change+1
            if(len(inp)-change!=j):
                j=len(inp)
                change=0
        elif(len(str(int("".join(inp))-1))<len(inp)):
            inp=list(str(int("".join(inp))-1))
        j=j-1

    print("Case #"+str((i+1))+": "+str(int("".join(inp))))