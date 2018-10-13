fin = open('B-large.in', 'r')
fout = open('bAns.txt', 'w')

def goodlinehor(mas, a, n):
    m = mas[n]
    for i in notusedcols:
        if m[i] > a:
            return 0
    return 1

def goodlinever(mas, a, n):
    m = getcol(mas, n)
    for i in notusedrows:
        if m[i] > a:
            return 0
    return 1

def getcol(mas, n):
    ans = [i[n] for i in mas]
    return ans

def findminimum(mas):
    ans = 1000
    row = 1000
    col = 1000
    for i in notusedrows:
        for j in notusedcols:
            if mas[i][j] < ans:
                ans = mas[i][j]
                row = i
                col = j
    return [row, col]
                

T = int(fin.readline())
for i in range(T):
    N, M = map(int, fin.readline().split())
    goodcols = []
    goodrows = []
    notusedrows = [j for j in range(N)]
    notusedcols = [j for j in range(M)]
    lawn = [map(int, fin.readline().split()) for j in range(N)]
    r, c = findminimum(lawn)
    ans = ''
    while r != 1000:
        h, v = goodlinehor(lawn, lawn[r][c], r), goodlinever(lawn, lawn[r][c], c)
        if not h and not v:
            ans = 'bad'
            break
        if h:
            notusedrows.remove(r)
            goodrows.append(r)
        else:
            notusedcols.remove(c)
            goodcols.append(c)
        r,c = findminimum(lawn)
    fout.write('Case #' + str(i + 1) + ': ')
    if ans == 'bad':
        fout.write('NO\n')
    else:
        fout.write('YES\n')



fin.close()
fout.close()
