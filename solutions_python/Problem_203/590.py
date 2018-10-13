f = open("input.in", "r")

t = f.readline().replace("\n", "")
t = int(t)


def expand(cake, i, j):
    #try to expand as a square
    
    #first orizonal
    l = j - 1
    while(l >= 0 and cake[i][l] == '?'):
        l -= 1
    r = j + 1
    while(r < C and cake[i][r] == '?'):
        r += 1
    if r -l > 0:
        #now nets see if i can expand vertically down
        dd = 0
        nope = False
        while(i+dd + 1 < R and not(nope)):
            nope = False
            for f in range(l + 1, r):
                if not(cake[i + dd + 1][f] == '?'):
                    nope = True 
                    break
            if nope == False:
                dd += 1
        
        dt = 0
        nope = False
        while(i -dt - 1 >= 0 and not(nope)):
            nope = False
            for f in range(l + 1, r):
                if not(cake[i -dt - 1][f] == '?'):
                    nope = True 
                    break
            if nope == False:
                dt += 1
        
        #now apply changes
        s = i - dt
        e = i + dd + 1

        for b in range(s, e):
            for m in range(l + 1, r):
                cake[b][m] = cake[i][j]

    else:
        #only vertically
        dd = 0
        while(i+dd + 1 < R and cake[i + dd + 1][j] == '?'):
            dd+=1
        
        dt = 0
        while(i -dt - 1 >= 0 and cake[i - dt - 1][j] == '?'):
            dt+=1
        
        s = i - dt
        e = i + dd + 1
        
        for b in range(s, e):
            cake[b][j] = cake[i][j]
            
out = open("outfile.out", "w")
for i in range(t):
    vals = f.readline().split()
    R = int(vals[0])
    C = int(vals[1])

    cake = []
    for j in range(R):
        chars = list(f.readline().replace("\n", ''))
        cake.append(chars)
    
    doneletters = set()

    print(cake)
    print("--------")
    for h in range(R):
        for q in range(C):
            if cake[h][q] not in doneletters and cake[h][q] != '?':
                doneletters.add(cake[h][q])
                expand(cake, h, q)

    
    out.write("Case #{}:\n".format(i+1))
    for h in range(R):
        for q in range(C):
            out.write("{}".format(cake[h][q]))
        out.write("\n")
out.close()
            
    