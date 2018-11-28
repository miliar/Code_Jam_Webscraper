from __future__ import division

dataset = 'small'
#dataset = 'large'

fin = open('A-%s.in' % dataset, 'r')
fout = open('A-%s.out' % dataset, 'w')

# psuedo-code
#X = x0, Y = y0
#print X, Y
#for i = 1 to n-1
#  X = (A * X + B) mod M
#  Y = (C * Y + D) mod M
#  print X, Y
# psuedo-code

ncases = int(fin.readline())
for case in xrange(1,ncases+1):
    [n, A, B, C, D, x0, y0, M] = [int(thing) for thing in fin.readline().split(' ')]
    #print n,A,B,C,D,x0,y0,M
    X,Y = x0,y0
    trees = [(X,Y)]
    for i in xrange(n-1):
        X = (A*X + B) % M
        Y = (C*Y + D) % M
        trees.append((X,Y))
    #print len(trees), n
    answer = 0
    for i in xrange(n):
        for j in xrange(i+1,n):
            for k in xrange(j+1,n):
                #print i,j,k
                ((x1,y1), (x2,y2), (x3,y3)) = (trees[i], trees[j], trees[k])
                #print (x1,y1), (x2,y2), (x3,y3)
                if ((x1+x2+x3)%3 == 0) and ((y1+y2+y3)%3 == 0):
                    answer += 1
    output = "Case #%d: %d" % (case,answer)
    print output
    fout.write(output+'\n')

fout.close()