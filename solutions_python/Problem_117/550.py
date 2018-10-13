import sys

def Lawnmower(fname):
    with open(fname) as file:
        line = file.readline()
        T=int(line)
        for case in range(1,T+1):
            mapa=[]
            maxren=[]
            maxcol=[]
            result=0
            [N,M]=[int(i) for i in file.readline().split()]
            for n in range(0,N):
                mapa.append([int(i) for i in file.readline().split()])
                maxren.append(max(mapa[n]))
            for m in range(0,M):
                maxcol.append(max([mapa[n][m] for n in range(0,N)]))
            n=0
            result = 'YES'
            while n<N and result=='YES':
                m=0
                while m<M:
                    if mapa[n][m]<maxren[n] and mapa[n][m]<maxcol[m]:
                        result='NO'
                        break
                    m+=1
                n+=1
            print("Case #{0}: {1}".format(case,result))
    file.close()
