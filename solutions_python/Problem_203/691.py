def find(s, e, a, h):
    sr, sc = s
    er, ec = e
    for i in range(sr, er+1):
        for j in range(len(h[i])):
                c, x = h[i][j]
                if c < sc:
                    continue
                if c > ec:
                    break
                return i, c, x

def solve(s, e, a, h):
    sr, sc = s
    er, ec = e
    if not(sr == er and  sc < ec or sc == ec and sr < er or sr < er and sc < ec):
        return
    r, c, x = find(s, e, a, h)

    tr, tc = -1, -1
    for i in range(r, er+1):
        for j in range(sc, c+1):
            if a[i][j] != '?' and a[i][j] != x:
                tr = i-1
                break
        if tr != -1:
            break
    if tr == -1:
        r = er
    else:
        r = tr

    for i in range(c, ec+1):
        for j in range(sr, r+1):
            if a[j][i] != "?" and a[j][i] != x:
                tc = i-1
                break
        if tc != -1:
            break
    if tc == -1:
        c = ec
    else:
        c = tc

    for i in range(sr, r+1):
        for j in range(sc, c+1):
            a[i][j] = x

    solve((r+1, sc), (er, c), a, h)
    solve((sr, c+1), (er, ec), a, h)
       
    
    

if __name__ == "__main__":
    t = int(input())
    for i in range(1, t+1):
        r, c = [int(x) for x in input().split(" ")]
        a = [['?' for i in range(c)] for j in range(r)]    
        h = [[] for i in range(r)]
        for j in range(r):
            x = input()
            for k in range(c):
                a[j][k] = x[k]
                if x[k] != '?':
                    h[j].append((k, x[k]))

        solve((0, 0), (r-1, c-1), a, h)
        print ("Case #%d:" % i)
        for i in range(len(a)):
            for j in range(len(a[i])):
                print (a[i][j], end='')
            print ()


                
