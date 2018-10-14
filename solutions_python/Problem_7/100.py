def make_trees(n, A, B, C, D, x0, y0, M):
    trees = []

    X = x0
    Y = y0
    trees.append((X,Y))

    for i in range(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        trees.append((X,Y))

    return trees


def make_valid_triangles(trees):

    N_trees = len(trees)

    valid_triangles = 0
    for t1 in range(N_trees - 2):
        for t2 in range(t1 + 1, N_trees - 1):
            for t3 in range(t2 + 1, N_trees):
                p1 = trees[t1]
                p2 = trees[t2]
                p3 = trees[t3]

                if (p1[0] + p2[0] + p3[0]) % 3 == 0 and (p1[1] + p2[1] + p3[1])% 3 == 0:
                    valid_triangles += 1

    return valid_triangles

def main():

##    f = open('A-test.in', 'r')
    f = open('A-small-attempt0.in', 'r')

    N_cases = int(f.readline().split()[0])

    for case in range(N_cases):
        n, A, B, C, D, x0, y0, M = [int(x) for x in f.readline().split()]

        trees = make_trees(n, A, B, C, D, x0, y0, M)

        valid_triangles = make_valid_triangles(trees)

        print 'Case #%d: %d' % ((case + 1), valid_triangles)

    f.close()

main()