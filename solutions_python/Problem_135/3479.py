def check(a1,a2):
    l=[]
    for j in a1:
        for i in a2:
            if(j==i):
                l.append(i)
    if (len(l)==0):
        return "Volunteer cheated!"
    elif (len(l)==1):
        return l[0]
    else:
        return "Bad magician!"
def magic():
    f=open("A-small-attempt0.in")
    g=open("output.ou", mode='w')
    T=int(f.readline()[:-1])
    for l in range(T):
        r1=int(f.readline()[:-1])
        a1=[f.readline()[:-1] for h in range(4)][r1-1].split(' ')
        r2=int(f.readline()[:-1])
        a2=[f.readline()[:-1] for h in range(4)][r2-1].split(' ')
        o=check(a1,a2)
        g.write("Case #"+str(l+1)+": "+o+"\n")
    f.close()
    g.close()
