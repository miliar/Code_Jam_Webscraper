f=open('D-small-attempt9.in')
g=open('Result.in','w')
T=int(f.readline())
for i in range(T):
    X,R,C=map(int,f.readline().split())
    if X==1:
        g.write('Case #'+str(i+1)+': GABRIEL\n')
    elif X==2:
        if (R*C)%2==0:
            g.write('Case #'+str(i+1)+': GABRIEL\n')
        else:
            g.write('Case #'+str(i+1)+': RICHARD\n')
    elif X==3:
        if (R<3 and C<3) or (R==4 and C==2) or (C==4 and R==2) or (C==4 and R==4) or (R==3 and C==1) or (C==3 and R==1) or (R==4 and C==1) or (C==4 and R==1):
            g.write('Case #'+str(i+1)+': RICHARD\n')
        else:
            g.write('Case #'+str(i+1)+': GABRIEL\n')
    elif X==4:
        if (R==3 and C==4) or (R==4 and C==3) or (R==4 and C==4):
            g.write('Case #'+str(i+1)+': GABRIEL\n')
        else:
            g.write('Case #'+str(i+1)+': RICHARD\n')
g.close()
f.close()
