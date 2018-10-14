#! /usr/bin/python

# Crop Triangles

import sys

def do_line( input_line ):
    
    [n, A, B, C, D, x, y, M] = [int(k) for k in input_line.split()]

    trees = [[x, y]]

    for i in range(1,n):
        x = ((A*x) + B) % M
        y = ((C*y) + D) % M
        trees.append([x, y])

    print trees # debug

    triangles = 0
    tree_set = [[], [], []]

    for a in range(len(trees)):
        tree_set[0] = trees[a]
        for b in range(a + 1, len(trees)):
            tree_set[1] = trees[b]
            for c in range(b + 1, len(trees)):
                tree_set[2] = trees[c]
                if [(sum([tree_set[j][k] for j in range(3)]) / 3.0) % 1 for k in range(2)] == [0, 0]:
                    triangles = triangles + 1

    return triangles

######################
#   MAIN    #
#####################

input_lines  = file(sys.argv[1]).read().split("\n")
out_handle = file(sys.argv[2], 'w')
ncases = int(input_lines[0])
ncases_done = 0

while ncases_done < ncases:

    ncases_done = ncases_done + 1
    out_value = do_line(input_lines[ncases_done])
    out_string = "Case #" + str(ncases_done) + ": " + str(out_value)
    print out_string
    out_handle.write(out_string + "\n")


out_handle.close()
