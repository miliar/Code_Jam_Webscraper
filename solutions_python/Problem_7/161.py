
#import matplotlib.pyplot as plt
import sys, math
in_file = file(sys.argv[1], 'r')

num_cases = int(in_file.readline())

def get_trees(n, A, B, C, D, x0, y0, M):
    x,y = x0,y0
    trees = [(x,y)]
    for i in xrange(1,n):
        x = (A*x + B) % M
        y = (C*y + D) % M
        trees.append((x,y))
    return trees

for case in range(1, num_cases + 1):
    parameters = map(int, in_file.readline().split())
    
    trees = get_trees(*parameters)
  
    treex, treey = zip(*trees)
#    print trees
    

    num_tri = 0
    for ind1, tree1 in enumerate(trees[:-2]):
        for ind2, tree2 in enumerate(trees[ind1+1:-1]):
            for ind3, tree3 in enumerate(trees[ind1+ind2+2:]):
#                print tree1, tree2, tree3
                xsum = tree1[0] + tree2[0] + tree3[0]
                if xsum % 3: continue

                ysum = tree1[1] + tree2[1] + tree3[1]
                if ysum % 3: continue
#                print xsum, ysum
#                if xsum/3 in treex and ysum/3 in treey:
                num_tri += 1
#    plt.figure()
#    plt.scatter(treex, treey, c='g', marker='v')
    print 'Case #%d: %d' % (case, num_tri)

#plt.show()

