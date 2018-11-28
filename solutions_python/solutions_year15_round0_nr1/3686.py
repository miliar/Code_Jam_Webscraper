f=open("Hola.txt",'w')
f.close()
f=open("A-small-attempt5.in",'r')
d=f.read()
n=d.split("\n")
f.close()
n.pop(0)
n.pop(len(n)-1)
for i in range(0,len(n)):
    L=0
    H=0
    for j in range(2,len(n[i])):
        L+=int(n[i][j])
        if L==j-1 or L>j-1:
            continue
        else:
            H+=(int(j-1)-int(L))
            L+=(int(j-1)-int(L))
    f=open("Hola.txt",'a')
    f.write("Case #"+str(i+1)+': '+str(H)+'\n')
    f.close()
            
