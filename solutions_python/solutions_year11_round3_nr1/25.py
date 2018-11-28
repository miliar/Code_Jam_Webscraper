def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

c = int(raw_input())
for case in range(1, c+1):
    print "Case #%d:" % case
    r, c = map(int,raw_input().split())
    g = [list(raw_input()) for x in range(r)]
    failed = False
    for x in range(r):
        for y in range(c):
            if g[x][y]=='#':
                if x+1<r and y+1<c and g[x][y+1]=='#' and g[x+1][y]=='#' and g[x+1][y+1]=='#':
                    g[x][y]='/'
                    g[x+1][y+1]='/'
                    g[x][y+1]='\\'
                    g[x+1][y]='\\'
                else:
                    failed = True
                    break
        if failed:
            break
    if failed:
        print "Impossible"
    else:
        print '\n'.join(''.join(g[i]) for i in range(r))
 
