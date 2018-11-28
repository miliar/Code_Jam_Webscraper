infile = 'A-small-attempt0.in'
outfile = 'Asmall-out.txt'

f = open(infile, 'r')
out = open(outfile, 'w')
T = int(f.readline())

for m in range(T):
    x = [0]*17
    for l in range(2):
        A = int(f.readline())
        for i in range(4):
            a,b,c,d = f.readline().split()
            if(i!=A-1):
                continue
            x[int(a)] += 1
            x[int(b)] += 1
            x[int(c)] += 1
            x[int(d)] += 1
    print x

    num = 0
    first = 0
    for i,j in enumerate(x):
        if j==2:
            num+=1
            first = i
    print num, first
    out.write('Case #'+str(m+1)+': ')
    if num==1:
        out.write(str(first))
    elif num==0:
        out.write('Volunteer cheated!')
    else:
        out.write('Bad magician!')
    out.write('\n')

out.close()
