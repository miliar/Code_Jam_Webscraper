f = open(r'd:\A-small-attempt.in','r')
fout = open(r'd:\sol_tic.out','w')
t=int(f.readline())
a=[['' for x in xrange(4)] for x in xrange(4)] 
for i in range(0,t):
    fl=0
    fout.write("Case #")
    fout.write(str(i+1))
    fout.write(":")
    fout.write(" ")
    for j in range(0,4):
        a[j]=str(f.readline())
        a[j]=a[j][:-1]
    f.readline()
    
    for j in range(0,4):
        if a[j] in ('XXXX','XXXT','TXXX','OOOO','OOOT','TOOO'):
            fout.write(a[j][1])
            fout.write(" won")
            fl=1
            break
        s=a[0][j]+a[1][j]+a[2][j]+a[3][j]
        if s in ('XXXX','XXXT','TXXX','OOOO','OOOT','TOOO'):
            if s[1]!='.':
                fout.write(s[1])
                fout.write(" won")
                fl=1
                break
    s=a[0][0]+a[1][1]+a[2][2]+a[3][3]
    if s in ('XXXX','XXXT','TXXX','OOOO','OOOT','TOOO'):
            if s[1]!='.':
                fout.write(s[1])
                fout.write(" won")
                fl=1
    s=a[0][3]+a[1][2]+a[2][1]+a[3][0]
    if s in ('XXXX','XXXT','TXXX','OOOO','OOOT','TOOO'):
            if s[1]!='.':
                fout.write(s[1])
                fout.write(" won")
                fl=1
    if fl!=1:
        for j in range(0,4):
            for k in a[j]:
                if k=='.':
                    fl=2
                    break
    if fl==0:
        fout.write("Draw")
    if fl==2:
        fout.write("Game has not completed")
    fout.write("\n")
f.close()
fout.close()

