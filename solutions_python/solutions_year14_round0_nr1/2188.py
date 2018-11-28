f=open('A-small-attempt0.in', 'r')
f2=open('result', 'w')
for i in range(int(f.readline())):
    a=int(f.readline())
    for j in range(4):
        l=map(int, f.readline().split())
        if (j==a-1):
            l1=l
    b=int(f.readline())
    for j in range(4):
        l=map(int, f.readline().split())
        if (j==b-1):
            l2=l
    common=list(set(l1)&set(l2))
    if len(common)==1:
        f2.write('Case #%d: %d' % (i+1, common[0]))
    elif len(common)==0:
        f2.write('Case #%d: Volunteer cheated!' % (i+1))
    else:
        f2.write('Case #%d: Bad magician!' % (i+1))