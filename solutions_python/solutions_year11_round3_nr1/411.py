# -*- coding: utf-8 -*-

def process_one_case(case):
    n,m,l=case
    rl=[]
    f=True
    for i in range(n):
        ll=[]
        for j in range(m):
            ll.append(l[i][j])
        rl.append(ll)

    for i in range(n):
        for j in range(m):
            if rl[i][j]=='.' or rl[i][j]=='\\' or rl[i][j] =='/':
                continue
            if i==n-1 or j==m-1 or rl[i][j+1] != '#' or rl[i+1][j]!='#' or rl[i+1][j+1]!='#':
                return '\nImpossible'
            rl[i][j]='/'
            rl[i][j+1]='\\'
            rl[i+1][j]='\\'
            rl[i+1][j+1]='/'
            

    rstr=''
    for i in range(n):
        rstr=rstr+'\n'+''.join(rl[i])
    return rstr

def get_one_case(ifs):
    ln=0
    line=ifs.readline()
    line=ifs.readline()
    while len(line)>0:
        line=line.strip()
        if len(line)==0:
            break
        dl=line.strip().split()
        n,m=int(dl[0]),int(dl[1])
        l=[]
        for i in range(n):
            line=ifs.readline().strip()
            l.append(line)
        yield n,m,l
        line=ifs.readline()

def main(argv):
    ifs=open(argv[0],'r')
    ofs=open(argv[0][:-2]+'out','w')
    cc=1    
    for case in get_one_case(ifs):
        r=process_one_case(case)
        ofs.write('Case #%d: %s\n'%(cc,r))
        cc+=1
    print cc
    ofs.close()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
