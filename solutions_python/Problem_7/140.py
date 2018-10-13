import sys

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "(%d, %d)" % (self.x, self.y)

def main(file):
    n_cases = int(file.readline().strip())
    for i in range(n_cases):
        trees = []
        n, a, b, c, d, x_0, y_0, m = [int(j) for j in file.readline().split()]
        X = x_0
        Y = y_0
        trees.append(Point(X,Y))
        for k in range(n-1):
            X = (a * X + b) % m
            Y = (c * Y + d) % m
            trees.append(Point(X,Y))
        print "Case #%d: %d" % (i+1, solve(trees))

def solve(trees):
    num_solutions = 0
    for tree1 in trees:
        for tree2 in [tree for tree in trees if tree != tree1]:
            for tree3 in [tree for tree in trees if (tree != tree1 and tree != tree2)]:
                center = Point((tree1.x + tree2.x + tree3.x)/3.0, (tree1.y + tree2.y + tree3.y)/3.0)
                if int(center.x) == center.x and int(center.y) == center.y:
                    num_solutions += 1
    return (num_solutions/6)

if __name__ == "__main__":
    main(open(sys.argv[1]))


