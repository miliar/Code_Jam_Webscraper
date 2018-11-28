import sys, os
##
file_in = 'A-small-attempt0.in'
file_out = 'A-small.out'
##file_in = 'A-large.in'
##file_out = 'A-large.out'
##file_in = 'test.txt'
##file_out = 'test.out.txt'

f = open(file_in, 'r')
res_f = open(file_out, 'w')

def compute_trees(n, A, B, C, D, x0, y0, M):
    trees = []
    x = x0
    y = y0
    trees.append((x, y))
    for i in range(1,n):
        x = (A * x + B) % M
        y = (C * y + D) % M
        trees.append((x,y))
    return trees

def validate_triangle(c1, c2, c3):
    if (c1[0]+c2[0]+c3[0]) % 3 == 0:
        if (c1[1]+c2[1]+c3[1]) % 3 == 0:
            return True
    return False

def count_triangles(trees):
    count = 0
    for i in range(len(trees)):
        c1 = trees[i]
        trees2 = trees[(i+1):]
        for j in range(len(trees2)):
            c2 = trees2[j]
            trees3 = trees2[j+1:]
            for c3 in trees3:
                if validate_triangle(c1, c2, c3):
                    count += 1
    return count


test_cases_num = 0

l = f.readline().strip('\n')
test_cases_num = int(l)
for i in range(test_cases_num):
    l = f.readline().strip('\n')
    n, A, B, C, D, x0, y0, M = [int(x) for x in l.split()]

    trees = compute_trees(n, A, B, C, D, x0, y0, M)

    v = count_triangles(trees)
    print >> res_f, "Case #%s: %s" % ((i+1), v)


try:
    f.close()
    res_f.close()
except:
    pass

print "done"