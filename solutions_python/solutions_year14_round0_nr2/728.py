fin = open('B-large.in', 'r');
fout = open('out.out', 'w');

T=int(fin.readline());
for t in range(0, T):
    inp=fin.readline().split();
    C=float(inp[0]); F=float(inp[1]); X=float(inp[2]);
    R=2.0000000;

    ANS=0.0000000000;
    while 1:
        tmp1=X/R; tmp3=C/R; tmp2 = tmp3 + (X/(R+F));
        if tmp2<tmp1:
            ANS = ANS+tmp3; R=R+F;
        else:
            ANS = ANS+tmp1;
            fout.write('Case #%d: %.7f\n' %(t+1, ANS));
            break;
fout.close();


