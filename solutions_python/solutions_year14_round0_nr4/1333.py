

def solveDeceive(naomi, ken, points):
    points = 0
    l = len(naomi)
    while l>0:
        if naomi[0] > ken[0]:
            ken = ken[1:]
            points+=1
        else:
            ken = ken[:-1]    
        naomi = naomi[1:]
        l-=1
    return points

def solveNormal(naomi, ken):
    points = 0
    for i in naomi:
        for j in ken:
            f = False
            if j>i:
                ken.remove(j)
                f = True
                break
        if not f:
            ken.remove(ken[0])
            points+=1
    return points

        

fInp = open('p4.inc','r')
fOut = open('p4.out','w')
inp = fInp.readline()
N = int(inp)

for i in range(N):
    fInp.readline()
    nao = map(float, fInp.readline().split())
    ken = map(float, fInp.readline().split())
    nao.sort()
    ken.sort()
    fOut.write("Case #%d: %d %d\n" % (i+1,  solveDeceive(nao,ken,0), solveNormal(nao,ken)) )
    
fInp.close()
fOut.close()