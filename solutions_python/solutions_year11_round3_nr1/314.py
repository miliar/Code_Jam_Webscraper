import sys
fin=open(sys.argv[1],'r')
fout=open(sys.argv[2],'w')
def solve(floor):
    for i in xrange(len(floor)):
        for j in xrange(len(floor[i])):
            if floor[i][j]=='#':
                if j+1 < len(floor[i]) and floor[i][j+1]=='#':
                    if i+1 < len(floor):
                        if floor[i+1][j]=='#' and floor[i+1][j+1]=='#':
                            floor[i][j]='/'
                            floor[i][j+1]='\\'
                            floor[i+1][j]='\\'
                            floor[i+1][j+1]='/'
                        else:
                            return 0
                    else:
                        return 0
                else:
                    return 0
    return floor
if __name__=='__main__':
    t=int(fin.readline())
    for tt in xrange(1,t+1):
        [r,c]=map(int,fin.readline().split())
        floor=[]
        for i in xrange(r):
            floor.append(list(fin.readline()))
        floor=solve(floor)
        if floor==0:
            fout.write("Case #"+str(tt)+":\n"+"Impossible\n")
        else:
            fout.write("Case #"+str(tt)+":\n")
            for i in xrange(len(floor)):
                fout.write(''.join(floor[i])+'\n')
fin.close()
fout.close()
