def outp(a,b):
    file=open("output.txt","a")
    s="Case #"+str(a+1)+": "+str(b)+"\n"
    file.write(s)
    file.close
    print(s)

q=open ("output.txt","w")
q.close()
inp = open("A-large.in","r")
a= []
for line in inp:
    if "\n" in line:
        a.append(line[0:-1])
    else:
        a.append(line)
inp.close()
inpNum =int(a.pop(0))
for ii in range(inpNum):
    qn = a.pop(0)
    qn= qn.split(" ")
    R, C = int(qn[0]), int(qn[1])
    grid = []
    for i in range(R):
        grid.append(list(a.pop(0)))
    print(grid)
    did = ["?"]
    for ir in range(R):
        for ic in range(C):
            if grid[ir][ic] in did:
                continue
            name = grid[ir][ic]
            did.append(name)
            
            c = ic
            while True:
                c-=1
                if c<0:
                    break
                if grid[ir][c] != "?":
                    break
            left = c+1
            
            r = ir
            done = False
            while r>0:
                r-=1
                c = ic
                while c >= left:
                    if grid[r][c] != "?":
                        done = True
                        break
                    c-=1
                if done:
                    r+=1
                    break
            up = r
            
            c = ic
            done = False
            while c < C-1:
                c +=1
                r = ir
                while r >= up:
                    if grid[r][c] != "?":
                        done = True
                        break
                    r-=1
                if done:
                    c-=1
                    break
            right = c

            r = ir
            done = False
            while r < R-1:
                r +=1
                c = left
                while c <= right:
                    if grid[r][c] != "?":
                        done = True
                        break
                    c+=1
                if done:
                    r-=1
                    break
            down = r

            for r in range(up, down+1):
                for c in range(left, right+1 ):
                    grid[r][c] = name
    ngrid=""
    for r in grid:
        ngrid += "\n"+"".join(r)
    outp(ii,ngrid)
    
    
