answer=[]
g=open("arun.in","r")
h=open("output.txt","w")
n=int(g.readline())
for i in range(n):
    a=int(g.readline())
    print a
    card=[]
    for i in range(4):
        b=g.readline()
        card+=[b[:-1].split()]
    c=int(g.readline())
    for i in range(4):
        b=g.readline()
        card+=[b[:-1].split()]
    count=0
    for i in range(0,4):
        for j in range(0,4):
            if card[a-1][i]==card[3+c][j]:
                if(count==0):
                    card_no=card[a-1][i]
                count+=1
    if(count==0):
        answer+=["Volunteer cheated!"]
    elif(count>1):
        answer+=["Bad magician!"]
    else:
        answer+=[card_no]
for i in range(n):
    string="Case #"+str(i+1)+": "+answer[i]+"\n"
    h.write(string)
g.close()
h.close()
