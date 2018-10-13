import sys,math

def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc

lines = sys.stdin.readlines()
it = iter(lines)
num = int(it.next())
for i in range(num):
    case = 1+i
    line = it.next()
    (n, A, B, C, D, x0, y0, M) = [int(i) for i in line.split()]
    (X,Y) =  (x0,y0)
    trees = []
    trees.append((X, Y))
    for i in range(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        trees.append((X, Y))
    numOK = 0
    for tri in xuniqueCombinations(trees,3):
        #print tri
        xc,yc = 0,0
        for vert in tri:
            (xc,yc) = (xc+vert[0],yc+vert[1])
        if xc % 3 == 0 and yc % 3 == 0:
            numOK += 1
    print "Case #"+str(case)+": "+str(numOK) 
                   
        
