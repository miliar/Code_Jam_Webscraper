def f(m):
    H=len(m)
    W=len(m[0])
    ans=[[]]*H
    letters="abcdefghijklmnopqrstuvwxyz"
    l=0
    for i in range(H):
        ans[i]=["*"]*W
    #  y-- > 0
    # x      1
    # |      2
    # \/     H-1
    for i in range(H):
        for j in range(W):
            x, y = i, j
            #North, West, East, South.
#            hist=[]
            while ans[x][y]=="*":
#                hist.append((x,y))
                nx, ny = x, y
                if x>0 and m[nx][ny] > m[x-1][y]:
                    nx, ny = x-1, y
                if y>0 and m[nx][ny] > m[x][y-1]:
                    nx, ny = x, y-1
                if y<W-1 and m[nx][ny] > m[x][y+1]:
                    nx, ny = x, y+1
                if x<H-1 and m[nx][ny] > m[x+1][y]:
                    nx, ny = x+1, y
                #no where to flow -- sink
                if x==nx and y==ny:
                    ans[x][y]=letters[l]
                    l+=1
                    break
                x, y = nx, ny
            ans[i][j]=ans[x][y]
#            let=ans[x][y]
#            for p in hist:
#                ans[p[0]][p[1]]=let
    return ans

from time import time
if __name__ == "__main__":
    start_time=time()
    output = open('d:\output', 'w')
    data = open("d:\in", "r")
    N = int(data.readline())
    for case in range(1, N + 1):
        h, w = map(int, data.readline().rstrip('\n').split(' '))
        m = []
        for i in range(h):
            m.append(map(int, data.readline().rstrip('\n').split(' ')))
        print '--------------'
        print "\n".join(" ".join(map(str, line)) for line in m)
        s="Case #%d:\n%s\n" % (case, "\n".join(" ".join(line) for line in f(m)))
        print s,
        output.write(s)
    print time()-start_time


