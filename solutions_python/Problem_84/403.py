t=int(raw_input())

for tt in range(t):
    r,c=map(int,raw_input().split())
    l=[]
    for i in range(r):
        l.append(list(raw_input()))
    sirve=True
    for i in range(r-1):
        for j in range(c-1):
            if l[i][j]=='#':
                if l[i][j+1]=='#' and l[i+1][j+1]=='#' and l[i+1][j+1]=='#':
                    l[i][j]='/'
                    l[i+1][j]='\\'
                    l[i][j+1]='\\'
                    l[i+1][j+1]='/'
                else:
                    sirve=False
    for i in range(r):
        for j in range(c):
            if l[i][j]=='#':
                sirve=False
    print "Case #%d:"%(tt+1)
    if sirve:
        for x in l:
            r=""
            for y in x: r=r+y
            print r
    else:
        print "Impossible"
