if __name__=='__main__':
    fin = open('C-large.in','r')
    fout = open('C-large.out','w')
    t = fin.readline()
    for ti in range(int(t)):
        linesplit = fin.readline().split()
        a = int(linesplit[0])
        b = int(linesplit[1])
        cnt=0
        for n in range(a, b):
            strn = str(n)
            mdict = {}
            for col in range(1, len(strn)):
                #cross-over
                strm = strn[col:]+strn[:col]
                # restriction
                if(strm[0]=='0'):
                    continue
                m = int(strm)
                if(m in mdict):
                    continue
                mdict[m] = 1
                if(n < m and m <= b):
                    cnt += 1
        fout.write('Case #'+str(ti+1)+': '+str(cnt)+'\n')
    fin.close()
    fout.close()
