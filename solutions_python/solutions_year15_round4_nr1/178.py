import time
##import sys
##sys.setrecursionlimit(10002)
def solve(r,c,m):
    ans=0
    for x in range(r):
        for y in range(c):
            flag=0#;print x,y,m
            if m[x][y]=='.':
                continue
            elif m[x][y]=='^':
                for i in range(x-1,-1,-1):
                    if m[i][y]<>'.':
                        flag=1
                        break
            elif m[x][y]=='v':
                for i in range(x+1,r):
                    if m[i][y]<>'.':
                        flag=1
                        break
            elif m[x][y]=='<':
                for i in range(y-1,-1,-1):
                    if m[x][i]<>'.':
                        flag=1
                        break
            elif m[x][y]=='>':
                for i in range(y+1,c):
                    if m[x][i]<>'.':
                        flag=1
                        break
            if flag:
                continue
            flag=0
            ans+=1
            if m[x][y]!='^':
                for i in range(x-1,-1,-1):
                    if m[i][y]<>'.':
                        flag=1
                        break
                if flag:
                    continue
            if m[x][y]!='v':
                for i in range(x+1,r):
                    if m[i][y]<>'.':
                        flag=1
                        break
                if flag:
                    continue
            if m[x][y]!='<':
                for i in range(y-1,-1,-1):
                    if m[x][i]<>'.':
                        flag=1
                        break
                if flag:
                    continue
            if m[x][y]!='>':
                for i in range(y+1,c):
                    if m[x][i]<>'.':
                        flag=1
                        break
                if flag:
                    continue
            return 'IMPOSSIBLE'
    return ans



def main():
    fi=file('al.in')
    fo=file('a.out','w')
    time0=time.time()
    t=int(int(fi.readline()))
    for ti in range(t):
        time1=time.time()
        r,c=map(int,fi.readline().split())
        m=[]
        for i in range(r):
            m.append(list(fi.readline()))
        ans="Case #%d: %s"%(ti+1,solve(r,c,m))
        print ans,"%.3f"%(time.time()-time1)
        fo.write(ans+'\n')
    print "%.3f"%(time.time()-time0)
    fi.close()
    fo.close()

if __name__ == '__main__':
    main()
