import sys

#sys.stdin = open("in.txt")
sys.stdin = open("C:\\Users\\Kuldeep\\Downloads\\A-large.in")
sys.stdout = open("C:\\Users\\Kuldeep\\Desktop\\out.txt",'w')

t = int(raw_input())

for tc in range(1,t+1):
    row = []
    mark = []
    r, c = map(int,raw_input().split())
    for i in range(r):
        mark.append([])
        row.append([])
        st = raw_input()
        for j in range(c):
            mark[i].append(0)
            row[i].append(st[j])
    
    flag = 0
    for i in range(r):
        for j in range(c):
            if row[i][j] == '#' and mark[i][j]==0:
                if i+1<r and j+1<c and row[i+1][j] == '#' and row[i+1][j+1]=='#' and row[i][j+1]=='#':
                    mark[i][j]=1
                    mark[i][j+1]=1
                    mark[i+1][j]=1
                    mark[i+1][j+1]=1
                    row[i][j]='/'
                    row[i][j+1]='\\'
                    row[i+1][j]='\\'
                    row[i+1][j+1]='/'
                else:
                    flag = 1
                    break
        if flag:
            break
    
    print("Case #"+str(tc)+": ")
    
    if flag:
        print 'Impossible'
    else:
        for i in range(r):
            for j in range(c):
                sys.stdout.write(row[i][j])
            print ''