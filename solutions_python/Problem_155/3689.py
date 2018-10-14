f=open("A-small-attempt10.in",'r')
d=f.read()
n=d.split("\n")
f.close()
n.pop(0)
n.pop(len(n)-1)
f=open("Test.txt",'w')
f.close()
for i in range(0,len(n)):
    FH=0
    HF=0
    for j in range(2,len(n[i])):
        FH+=int(n[i][j])
        if FH==j-1 or FH>j-1:
            continue
        else:
            HF+=(int(j-1)-int(FH))
            FH+=(int(j-1)-int(FH))
    f=open("Test.txt",'a')
    f.write("Case #"+str(i+1)+': '+str(HF)+'\n')
    f.close()
            
