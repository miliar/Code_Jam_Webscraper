rd=raw_input

def gr():
    return [map(int,rd().split()) for _ in range(4)]

def solve(r1,r2,g1,g2):
    x=set(g1[r1])&set(g2[r2])
    if len(x)==1:
        return x.pop()
    elif x:
        return 'Bad magician!'
    else:
        return 'Volunteer cheated!'

for t in range(1,1+int(rd())):
    r1=int(rd())-1
    g1=gr()
    r2=int(rd())-1
    g2=gr()
    print 'Case #%d: %s'%(t,solve(r1,r2,g1,g2))
