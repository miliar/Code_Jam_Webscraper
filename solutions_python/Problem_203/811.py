x = int(input())
for q in range(x):
    chars = []
    y = input()
    r = int(y[:y.index(' ')])
    c = int(y[y.index(' ')+1:])
    arr = [['?' for i in range(c)] for j in range(r)]
    for i in range(r):
        t = input()
        for j in range(c):
            if t[j] != '?':
                arr[i][j] = t[j]
                chars.append([t[j], i, j])
    for p in range(len(chars)):
        i = chars[p][1]
        j = chars[p][2]
        u = i
        b = i
        m = j
        n = j
        try:
            while True:
                if arr[u-1][j] == '?' and u-1>= 0:
                    u -= 1
                    arr[u][j] = chars[p][0]
                else:
                    break
        except:
            pass
        try:
            while True:
                if arr[b+1][j] == '?' and b+1 < r:
                    b += 1
                    arr[b][j] = chars[p][0]
                else:
                    break
        except:
            pass
        try:
            while True:
                gc = True
                for k in range(u, b+1):
                    if arr[k][m-1] != '?' or m-1<0:
                        gc = False
                        break
                if gc:
                    for k in range(u, b+1):
                        arr[k][m-1] = chars[p][0]
                    m -= 1
                else:
                    break
        except:
            pass
        try:
            while True:
                gc = True
                for k in range(u, b+1):
                    if arr[k][n+1] != '?' or m-1>=c:
                        gc = False
                        break
                if gc:
                    for k in range(u, b+1):
                        arr[k][n+1] = chars[p][0]
                    n += 1
                else:
                    break
        except:
            pass
    print("Case #" + str(q+1) + ":")
    for i in range(r):
        pp = ''
        for j in range(c):
            pp += arr[i][j]
        print(pp)

