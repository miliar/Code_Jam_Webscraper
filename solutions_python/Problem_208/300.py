def solve(n, q, es, d, uv):
#    print (n, q, es, d, uv)
    m = [[[float("inf") for i in range(n)] for j in range(n)] for k in range(n)]  
    r = [[[0 for i in range(n)] for j in range(n)] for k in range(n)]  
    mm = [[float("inf") for i in range(n)] for j in range(n)]
    for i in range(n):
        m[i][i][i] = 0
        r[i][i][i] = es[i][0]
        mm[i][i] = 0

    for i in range(n):
        for j in range(n):
            if d[i][j] != -1 and d[i][j] <= es[i][0]:
                m[i][j][i] = d[i][j] / es[i][1]
                r[i][j][i] = es[i][0] - d[i][j]
                mm[i][j] = m[i][j][i]
            
    for i in range(n):
        for j in range(i+1):
            for k in range(n):
                if r[k][i][j] == 0 and mm[k][j] == float("inf"):
                    continue
                    
                for l in range(n):
#                    for ii in range(n):
#                        print (mm[ii])
#                    print ()
                    if d[i][l] != -1 and r[k][i][j] - d[i][l] >=0:
                        if m[k][l][j] > m[k][i][j] + d[i][l] / es[j][1]:
                            m[k][l][j] = m[k][i][j] + d[i][l] / es[j][1]
                            r[k][l][j] = r[k][i][j] - d[i][l]
                        if mm[k][l] > m[k][l][j]:
                            mm[k][l] = m[k][l][j]
                    
                    if m[k][l][j] > mm[k][j] + m[j][l][j]:
                        m[k][l][j] = mm[k][j] + m[j][l][j]
                        r[k][l][j] = r[j][l][j]
                        if mm[k][l] > m[k][l][j]:
                            mm[k][l] = m[k][l][j]
    
    res = []
    for i in range(q):
        u, v = uv[i]
        res.append(str(mm[u-1][v-1]))

    return ", ".join(res)
    

if __name__ == "__main__":
    t = int(input())
    for i in range(1, t+1):
        n, q = [int(x) for x in input().split(" ")]
        es = [(0,0)] * n
        for j in range(n):
            es[j] = [int(x) for x in input().split(" ")]
        d = [[] for j in range(n)]
        for j in range(n):
            d[j] = [int(x) for x in input().split(" ")]
        uv = [(0,0)] * q
        for j in range(q):
            uv[j] = [int(x) for x in input().split(" ")]
        res = solve(n, q, es, d, uv)
        print ("Case #%d: %s" % (i, res))

