def solveXs(Xs):
    n = len(Xs)
    avail_row = [ True for _ in range(n)]
    avail_col = [ True for _ in range(n)]
    Xss = [ ['.' for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if Xs[r][c] == 'x':
                Xss[r][c] = 'x'
                avail_row[r] = False
                avail_col[c] = False
    for r in range(n):
        for c in range(n):
            if Xss[r][c] == '.' and avail_row[r] and avail_col[c]:
                Xss[r][c] = 'x'
                avail_row[r] = False
                avail_col[c] = False
    return Xss

def solvePsInHorizontal(Ps,avail_plus,avail_sub):
    n = len(Ps)
    for r in [0,n-1]:
        for c in range(n):
             if Ps[r][c] == '.' and avail_plus[r+c] and avail_sub[r-c]:
                Ps[r][c] = '+'
                avail_plus[r+c] = False
                avail_sub[r-c] = False
    return Ps
def solvePsInVertical(Ps,avail_plus,avail_sub):
    n = len(Ps)
    for r in range(n):
        for c in [0,n-1]:
             if Ps[r][c] == '.' and avail_plus[r+c] and avail_sub[r-c]:
                Ps[r][c] = '+'
                avail_plus[r+c] = False
                avail_sub[r-c] = False
    return Ps



def solvePs(Ps1):
    n = len(Ps1)
    avail_plus = [ True for _ in range(n * 2 -1)]
    avail_sub = [ True for _ in range(n * 2 - 1)]
    Ps2 = [ ['.' for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if Ps1[r][c] == '+':
                Ps2[r][c] = '+'
                avail_plus[r+c] = False
                avail_sub[r-c] = False
    Ps1 = solvePsInHorizontal(Ps1,avail_plus,avail_sub)
    Ps2 = solvePsInVertical(Ps2,avail_plus,avail_sub)
    if score(Ps1) > score(Ps2):
        return Ps1
    else:
        return Ps2

def mergePXs(Xs,Ps):
    n = len(Xs)
    Xss = [ ['.' for _ in range(n)] for _ in range(n)]

    for r in range(N):
        for c in range(N):
            if Xs[r][c] == 'x' and Ps[r][c] == '+':
                Xss[r][c] = 'o'
            elif Ps[r][c] == '+':
                Xss[r][c] = '+'
            else:
                Xss[r][c] = Xs[r][c]
    return Xss
def compare(res, ori):
    works = []
    n = len(res)
    for r in range(n):
        for c in range(n):
            if res[r][c] != ori[r][c]:
                works.append(res[r][c]+" "+str(r+1)+" "+str(c+1))
    return works

def score(res):
    total = 0
    n = len(res)
    for r in range(n):
        for c in range(n):
            if res[r][c] == 'o':
                total += 2
            elif res[r][c] != '.':
                total += 1
    return total

with open("input.txt","r") as reader, open("output.txt","w") as writer:
    cases = int(reader.readline())
    for cs in range(1,cases+1):
        N,M = map(int,reader.readline().split(" "))
        Xs = [ ['.' for _ in range(N)] for _ in range(N)]
        Ps = [ ['.' for _ in range(N)] for _ in range(N)]
        Or = [ ['.' for _ in range(N)] for _ in range(N)]
        for _ in range(M):
            chr,r,c = reader.readline().split(" ")
            r,c = int(r)-1,int(c)-1
            Or[r][c] = chr
            if chr == 'o':
                Xs[r][c] = 'x'
                Ps[r][c] = '+'
            elif chr == 'x':
                Xs[r][c] = 'x'
            elif chr == '+':
                Ps[r][c] = '+'

        Xs_temp = solveXs(Xs)
        Ps_temp = solvePs(Ps)
        Os = mergePXs(Xs_temp,Ps_temp)

        works = compare(Os,Or)
        writer.write("Case #"+str(cs)+": "+str(score(Os))+" "+str(len(works))+"\n")
        for work in works:
            writer.write(work+"\n")
