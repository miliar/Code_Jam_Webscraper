
f = open('cjprelim2a.txt','r')
op = open('qp2.txt','w')
numLines = int(f.readline())
for i in range(numLines):
    op.write('Case #')
    op.write(str(i+1))
    op.write(': ')
    line = f.readline().split();
    N = int(line[0])
    S = int(line[1])
    p = int(line[2])
    higher = 0
    border = 0
    for j in range(N):
        total = int(line[j+3])
        if not (p==1 and total==0):
            if total > 3*p-3:
                higher=higher+1
            elif total > 3*p-5:
                border=border+1
    higher = higher+min([border,S])
    op.write(str(higher))
    op.write('\n')
f.close()
op.close()
