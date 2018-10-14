def A():
    fileopen = open('F:\programing\Code\codejam2013\qualification\A.txt')
    line = fileopen.readline()
    T=int(line)
    an=0
    while T>0:
        T=T-1
        an=an+1
        mapp=[]
        ok=[0,0]
        for i in range(4):
            line = fileopen.readline()
            mapp.append(line)
        line = fileopen.readline()

        t=0
        for i in range(4):
            for j in range(4):
                if mapp[i][j]=='.':
                    t=1
                O1=0;
                X1=0;
                if mapp[i][j]=='O':
                    O1=O1+1
                elif mapp[i][j]=='X':
                    X1=X1+1
                elif mapp[i][j]=='T':
                    O1=O1+1
                    X1=X1+1

                O2=0;
                X2=0;
                if mapp[j][i]=='O':
                    O2=O2+1
                elif mapp[j][i]=='X':
                    X2=X2+1
                elif mapp[j][i]=='T':
                    O2=O2+1
                    X2=X2+1
            if O1==4 or O2==4:
                ok[0]=1;
            if X1==4 or X2==4:
                ok[1]=1;

        for i in range(4):
            O1=0;
            X1=0;
            O2=0;
            X2=0;
            if mapp[i][i]=='O':
                O1=O1+1
            elif mapp[i][i]=='X':
                X1=X1+1
            elif mapp[i][i]=='T':
                O1=O1+1
                X1=X1+1

            if mapp[i][3-i]=='O':
                O2=O2+1
            elif mapp[i][3-i]=='X':
                X2=X2+1
            elif mapp[i][3-i]=='T':
                O2=O2+1
                X2=X2+1
        if O1==4 or O2==4:
            ok[0]=1;
        if X1==4 or X2==4:
            ok[1]=1;
        print 'Case #%d' % (an) + ': ',
        if ok[0]==1 and ok[1]==0:
            print 'O won'
        elif ok[0]==0 and ok[1]==1:
            print 'X won'
        elif ok[0]==0 and ok[1]==0 and t==0:
            print 'Game has not completed'
        else:
            print 'Draw'        
    fileopen.close()

if __name__=='__main__':
    A()
