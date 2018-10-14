import string

ifile = open("A-large.in")
fs = ifile.read().split("\n")
ifile.close()

T = int(fs[0])

out = []

NMidx = 1
for t in range(0,T):
    line = fs[NMidx].split(' ')
    row = int(line[0])
    col = int(line[1])

    arr = []
    for r in range(0,row):
        arr.append([])
        for c in range(0,col):
            arr[r].append(fs[NMidx+r+1][c])

    for r in range(0,row-1):
        for c in range(0,col-1):
            if arr[r][c] == '#' and arr[r+1][c] == '#' and arr[r][c+1] == '#' and arr[r+1][c+1] == '#':
                arr[r][c] = '/'
                arr[r+1][c+1] = '/'
                arr[r+1][c] = '\\'
                arr[r][c+1] = '\\'

    impos = False
    for r in range(0,row):
        for c in range(0,col):
            if arr[r][c] =='#':
                impos = True

    if not impos:
        stemp = []
        for r in range(0,row):
            stemp.append(string.join(arr[r],''))
        res = string.join(stemp,'\n')

    if impos:
        out.append("Case #"+str(t+1)+":\n%s"%str('Impossible'))
    else:
        out.append("Case #"+str(t+1)+":\n%s"%res)
    NMidx+=1+row

ofile = open("output.txt","w")
ofile.write(string.join(out,"\n"))
ofile.close()
