from operator import mul
f = open('p1.in','r')
op = open('p1.out','w')
numProbs = int(f.readline())
for i in range(numProbs):
    op.write('Case #')
    op.write(str(i+1))
    op.write(': ')
    line = f.readline().split()
    A = int(line[0])
    B = int(line[1])
    n = f.readline().split()
    nextLine = [float(i) for i in n]
    first = nextLine[0]
    g = [min([first*B+(1-first)*(2*B+1), B+2])]
    print(g)
    for i in range(1,A):
        print(nextLine[0:i+1])
        g.append(min([g[-1]+1, B+2, reduce(mul,nextLine[0:i+1])*(B-i)+(1-reduce(mul,nextLine[0:i+1]))*(2*B-i+1)]))
        print(g)
    op.write(str(g[A-1]))
    op.write('\n')
f.close()
op.close()
