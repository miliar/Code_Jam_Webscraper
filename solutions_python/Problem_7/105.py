f = open('A-small-attempt0.in')
output = open('A-small.out', 'w')

N = int(f.readline())
for c in range(1,N+1):
    metrics = f.readline()[:-1].split()
    metrics = map(int, metrics)
    n = metrics[0]
    A = metrics[1]
    B = metrics[2]
    C = metrics[3]
    D = metrics[4]
    x0 = metrics[5]
    y0 = metrics[6]
    M = metrics[7]
    
    trees = []
    X = x0
    Y = y0
    trees.append((X, Y))
    for i in range(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        trees.append((X, Y))
    
    output.write('Case #%u: ' % c)
    count = 0
    
    if len(trees) < 3:
        pass
    else:
        for x in range(0,len(trees)):
            for y in range(x+1,len(trees)):
                for z in range(y+1,len(trees)):
                    p = trees[x]
                    q = trees[y]
                    r = trees[z]
                    cent_x = (p[0] + q[0] + r[0]) % 3
                    cent_y = (p[1] + q[1] + r[1]) % 3
                    if cent_x == 0 and cent_y == 0:
                        count += 1
                        
    output.write(str(count) + '\n')    

f.close()
output.close()