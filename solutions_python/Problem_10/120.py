f=open("A-large.in")
w=open("a-large.out",'w')
s=f.read().split('\n')
n=int(s.pop(0))
for i in range(n):
    line1=s.pop(0).split(' ')
    line2=s.pop(0).split(' ')
    p=int(line1[0])
    k=int(line1[1])
    l=int(line1[2])
    impossible=False
    letterf=[]
    num=1
    for j in line2:
        letterf.append([int(j),num])
        num+=1
    letterf.sort()
    letterf.reverse()
    keys=dict()
    z=0
    for letter in letterf:
        keys[letter[1]]=z/k+1
        z+=1
        if(z/k>p): impossible=True
    #print keys
    total=0
    for j in letterf:
        total+=keys[j[1]]*j[0]
    w.write("Case #"+str(i+1)+": "+str(total)+'\n')
w.close()
f.close()
