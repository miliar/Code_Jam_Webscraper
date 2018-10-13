lines=[]
file1=open('D-small-attempt0.in')
for line in file1:
    lines.append(line)
file1.close

def check(X,R,C):
    if (R*C)%X!=0:
        return False
    if X==1:
        return True
    if X>=7:
        return False
    if X<=2:
        return True
    if X==3 and R>1 and C>1:
        return True
    if X==4 and R>2 and C>2:
        return True
    if X==5 and R>2 and C>2:
        return True
    if X==6:
        if R>=6 or C>=6:
            if R>2 and C>2:
                return True
            else:
                return False
        else:
            return False


T=int(lines[0])
ctr=1
f=open('Output.out','w')
while ctr<=T:
    X,R,C=[int(x) for x in lines[ctr].split()]
    Output=check(X,R,C)
    
    if Output:
        f.write("Case #%d: GABRIEL" %ctr)
    else:
        f.write("Case #%d: RICHARD" %ctr)
    ctr+=1
    if ctr<=T:
        f.write("\n")
f.close()
