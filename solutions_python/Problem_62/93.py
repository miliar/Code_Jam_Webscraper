f = open("data.txt")
g = open("data1.txt", 'w')
j = int(f.readline())

for i in range(j):
    l = f.readline()
    n = int(l.split()[0])
    w = []
    for r in range(n):
        l = f.readline()
        w.append([int(x) for x in l.split()])
    w.sort()
    c = 0
    for r in range(n):
        for s in range(r+1, n):
            if w[s][1] < w[r][1]:
                c += 1
    stri = str(c)
    string = 'Case #' + str(i+1) + ': ' + stri + '\n'
    g.write(string)
    print(string)
