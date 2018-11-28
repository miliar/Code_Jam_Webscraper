#!/usr/bin/env python 
################################################################################
# Jeffrey A. Sandoval
# http://www.cs.rice.edu/~jasandov
#
# Google Code Jam 2009
# Qualification Round
# September 3, 2009
#
# Problem B:  Watersheds
################################################################################
# This problem reminds me of data-flow analysis because I can solve it
# using a fixed point iterative algorithm.  Each cell drains to itself
# or one of its neighbors.  A "sink" is any cell that drains to
# itself.  The goal is to partition the cells in groups that drain to
# the same sink.  Then, each group, called a basin, should be labeled
# in order from the NW to the SE (row by row).
#
# My approach is to traverse the altitude map once to determine the
# "immediate" drain for each cell.  Then I traverse the altitude map
# again to approximate the sink for each cell by initializing it to
# the immediate drain.  Then, I iterate and refine the sink map as
# follows: the sink of a cell is the sink of the immediate drain for a
# cell.  I iterate until the sink map does not change, indicating that
# I've reached a fixed point.
#
# At this point the sink map will contain coordinates of the sinks, so
# each basin can be referred to by its sink.  To finish, I just map
# sink coordinates to a label, in order, and print out the final basin
# map.
#
################################################################################

import sys
import logging
import array


#logging.basicConfig(level=logging.DEBUG)

def main():
    input = sys.stdin

    # T specifies the number of maps
    T = int(input.readline().strip())
    logging.info("T = %d", T)

    for t in range(T):
        # H specifies the height of a map
        # W specifies the width of a map
        (H, W) = tuple(map(int, input.readline().split()))
        # M contains the map as a list of lists
        M = []
        for i in range(H):
            row = map(int, input.readline().split())
            M.append(row)
        # process this map
        processMap(t + 1, H, W, M)

# Label the sinks with letters instead of coordinates
def labelSinks(H, W, S):
    # labels holds all possible labels
    labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    assert len(labels) == 26
    for label in labels:
        assert len(label) == 1

    # just add some extra labels for debugging purposes
    for i in range(1000):
        labels.append("l" + str(i))

    # the next label index that is free
    labelIndex = 0

    # map sinks to labels
    labelMap = {}
    for r in range(H):
        for c in range(W):
            sink = S[r][c]
            if (sink not in labelMap):
                logging.info("labeling " + str(sink) + " as " + str(labels[labelIndex]))
                labelMap[sink] = labels[labelIndex]
                labelIndex += 1

    # fill in each element in a label map
    L = [ [None]*W for i in range(H) ]
    for r in range(H):
        for c in range(W):
            L[r][c] = labelMap[S[r][c]]

    # return the map of labels
    return L

# convert a label map to a string that is suitable for printing
def labelMapToString(H, W, L):
    ret = ""
    for r in range(H):
        row = ""
        for c in range(W):
            row += " " + str(L[r][c])
        ret += (row.strip() + "\n")
    return ret.strip()

# Process the map
def processMap(I, H, W, M):
    # points contains the coordinates of all the items in the map
    points = []
    for r in range(H):
        for c in range(W):
            points.append((r, c))

    # neighbors contains a list of neighbor coordinates for each location
    neighbors = [ [None]*W for i in range(H) ]
    for (r, c) in points:
        neighbors[r][c] = []

    # add northern neighbors
    for c in range(W):
        for r in range(1, H): neighbors[r][c].append(((r - 1), c))

    # add western neighbors
    for r in range(H):
        for c in range(1, W): neighbors[r][c].append((r, (c - 1)))

    # add eastern neighbors
    for r in range(H):
        for c in range(W - 1): neighbors[r][c].append((r, (c + 1)))

    # add southern neighbors
    for c in range(W):
        for r in range(H - 1): neighbors[r][c].append(((r + 1), c))


    # D contains the "drain" map, which indicates for each cell the
    # coordinates of the immediate cell into which it drains
    D = [ [(None, None)]*W for i in range(H) ]
    for (r, c) in points:
        min_alt = M[r][c]
        drain = (r, c)
        for (nr, nc) in neighbors[r][c]:
            if (M[nr][nc] < min_alt):
                min_alt = M[nr][nc]
                drain = (nr, nc)
        D[r][c] = drain


    # S contains the "sink" map, which indicates the sink for each
    # cell; we will first initilize the sink map to be equal to the
    # drain map. Then we will iteratively refine the sink map until a
    # fixed point is reached.
    S = [ [(None, None)]*W for i in range(H) ]
    for (r, c) in points:
        S[r][c] = D[r][c]

    # Iterate to compute the fixed point of the "sink" map
    changed = True
    while (changed):
        changed = False
        #L = labelSinks(H, W, S)
        #logging.info("Iterating:\n" + str(labelMapToString(H, W, L)))
        for (r, c) in points:
            (dr, dc) = D[r][c]
            sink = S[dr][dc]
            if (sink != S[r][c]):
                S[r][c] = sink
                changed = True

    L = labelSinks(H, W, S)
    logging.info("H = %d", H)
    logging.info("W = %d", W)
    logging.info("M = " + str(M))
    logging.info("D = " + str(D))
    logging.info("S = " + str(S))
    logging.info("L = " + str(L))
    print "Case #" + str(I) + ":"
    print labelMapToString(H, W, L)


main()
