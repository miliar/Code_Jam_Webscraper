import sys

def ongrid(a,b,c):
    if ((a[0]+b[0]+c[0])%3==0) and ((a[1]+b[1]+c[1])%3==0):
        return True
    else:
        return False

def solve(infilename, outfilename):
    infile, outfile = open(infilename), open(outfilename, 'w')
    cases = int(infile.next().strip())
    for case in range(cases):
        n, A, B, C, D, x0, y0, M = [int(x) for x in infile.next().strip().split(' ')]
        poss = 0
        trees = [(x0,y0)]
        X, Y = x0, y0
        for i in range(1, n):
            X = (A * X + B) % M
            Y = (C * Y + D) % M
            trees.append((X,Y))
        for i in range(0,len(trees)-2):
            for j in range(i+1,len(trees)-1):
                for k in range(j+1,len(trees)):
                    if ongrid(trees[i],trees[j],trees[k]):
                        poss += 1   
        
        outfile.write('Case #'+str(case+1)+': '+str(poss)+'\n')

if __name__ == '__main__':
    solve(sys.argv[1], sys.argv[2])
