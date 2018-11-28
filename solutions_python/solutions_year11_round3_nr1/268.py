import sys


def solve(f):
    r,c = map(int, f.readline().split())
    a=[]
    for i in range(r):
        a.append(list(f.readline().strip()))
    solved = True
    for i in range(r):
        ls = 0
        for j in range(c):
            if a[i][j] == '#':
                d=False
                try:
                    if a[i][j-1] == 1 and ls: 
                        a[i][j] = 2;
                        ls-=1
                        d=True
                except Exception, e:
                    print e
                try:
                    if a[i-1][j] == 1:
                        a[i][j] = 3;
                        ls-=1
                        d=True
                except Exception, e:
                    print e
                try:
                    if a[i-1][j] == 2: 
                        ls+=1
                        a[i][j] = 4;
                        d=True
                except Exception, e:
                    print e
                if not d:
                    if i==r-1:
                        return False
                    a[i][j]=1
                    ls+=1
    for i in range(r):
        for j in range(c):
            if a[i][j]==1:
                a[i][j]='/'
            elif a[i][j]==2:
                a[i][j]='\\'
            elif a[i][j]==3:
                a[i][j]='\\'
            elif a[i][j]==4:
                a[i][j]='/'
    sc=[]
    for i in range(c):
        sc.append(0)
    for i in range(r):
        l1=l2=0
        for j in range(c):
            if a[i][j]=='/':
                l1+=1
                sc[j]+=1
            if a[i][j]=='\\':
                l2+=1
                sc[j]-=1
        if l1!=l2:
            return False
    for i in range(c):
        if sc[i]!=0:
            return False
    return a


if __name__ == "__main__":
    f = open(sys.argv[1])
    g = open(sys.argv[2],'w')
    t = int(f.readline())
    for _t in range(t):
        rez = solve(f)
        if not rez:
            g.write("Case #%d:\n Impossible\n" % (_t+1))
        else:
            g.write("Case #%d:\n" % (_t+1))
            for line in rez:
                g.write(''.join(line)+'\n')
                
