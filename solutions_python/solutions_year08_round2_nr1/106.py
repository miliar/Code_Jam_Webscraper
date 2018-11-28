def solve(n, A, B, C, D, x0, y0, M):
    mod = [(x0, y0)]
    for i in range(n-1):
        x0 = (A*x0 + B) % M
        y0 = (C*y0 + D) % M
        mod.append((x0, y0)) 
    
    max = len(mod)
    num = 0
    for i in range(max):
        for j in range(i+1, max):
            for k in range(j+1, max):
                    if (mod[i][0] + mod[j][0] + mod[k][0]) % 3 == 0:
                        if (mod[i][1] + mod[j][1] + mod[k][1]) % 3 == 0:
                            num += 1 
    return num


#fname = "A.in"
fname = "A-small-attempt0.in"
fin = open(fname, "r")
fOutName = fname.split(".")[0] + ".out"
fout = open(fOutName, "w")
num = int(fin.readline().strip("\n"))
for i in xrange(1, num + 1):
    n, A, B, C, D, x0, y0, M = [int(x) for x in fin.readline().split()]
    str = "Case #%d: %d" % (i, solve(n, A, B, C, D, x0, y0, M))
    print str
    fout.write(str + "\n") 
fin.close()
fout.close()
