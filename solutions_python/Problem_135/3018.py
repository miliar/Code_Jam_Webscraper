f = open("A-small-attempt0.in","r")
f1 = open("outfile.txt","w")
t = int(f.readline())
for i in range(t):
    count=0
    a1 = int(f.readline())-1
    for j in range(4):
        if a1==j:
            a1str=f.readline().split(" ")
        else:
            waste=f.readline()
    a2 = int(f.readline())-1
    for j in range(4):
        if a2==j:
            a2str=f.readline().split(" ")
        else:
            waste=f.readline()
    for j in range(4):
        for k in range(4):
            if int(a1str[j])==int(a2str[k]):
                count += 1
                num = a1str[j]
    if count == 0:
        ans = "case #"+str(i+1)+": "+"Volunteer cheated!\n"
        f1.write(ans)
    elif count ==1:
        ans = "case #"+str(i+1)+": "+str(num)+"\n"
        f1.write(ans)
    else:
        ans="case #"+str(i+1)+": "+"Bad magician!\n"
        f1.write(ans)
f1.close()
            
