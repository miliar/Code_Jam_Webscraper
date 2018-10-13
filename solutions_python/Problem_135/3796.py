op= open('Input.txt', 'r')
en=open('Output.txt', 'w')
x=int(op.readline())

for i in range(1, x+1):
    #take all inputs
    ans1=int(op.readline())
    r11=op.readline().split()
    r12=op.readline().split()
    r13=op.readline().split()
    r14=op.readline().split()
    if ans1==1:
        s=r11
    elif ans1==2:
        s=r12
    elif ans1==3:
        s=r13
    elif ans1==4:
        s=r14
    ans2=int(op.readline())
    r21=op.readline().split()
    r22=op.readline().split()
    r23=op.readline().split()
    r24=op.readline().split()
    if ans2==1:
        p=r21
    elif ans2==2:
        p=r22
    elif ans2==3:
        p=r23
    elif ans2==4:
        p=r24

    #compare the two answers
    card=100
    output=2
    for n in s:
        for m in p:
            if n==m:
                if card==100:
                   card=int(n)
                   output=1
                else:
                    card=200
                    output=3

    if output==1:
        en.write("Case #%d: %d\n" % (i, card))
    elif output==2:
        en.write("Case #%d: Volunteer cheated!\n" % i)
    elif output==3:
        en.write("Case #%d: Bad magician!\n"% i)
op.close()
en.close()
