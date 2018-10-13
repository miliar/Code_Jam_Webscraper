#!/usr/bin/python

import sys

INPUT = sys.stdin
INPUT = open(sys.argv[1],'r')

def getline():
    return INPUT.readline()[:-1]

def trace(*strs):
    print >> sys.stderr, '..',
    for str in strs:
        print >> sys.stderr, str,
    print >> sys.stderr

import Queue

n_cases = int(getline())
trace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    trace()
    trace( 'Case #', case_num )

    (H, W) = map(int, getline().split())
    altitude_of_ = []
    basin_ = []
    for h in range(1, H+1):
        row = map(int, getline().split())
        assert len(row) == W
        altitude_of_.append(row)
        basin_.append( [None] * W )
    assert len(altitude_of_) == H

    def off_map(i, j):
        return i <= -1 or i >= H or j <= -1 or j >= W

    def on_map(i,j):
        return 0 <= i and i < H and 0 <= j and j < W

    neighbor_deltas = [
        (-1,0), # North
        (0,-1), # West
        (0,+1), # East
        (+1,0), # South
    ]

    def flow_neighbor( i, j ):
        lowest_neighbor_alt = sys.maxint
        for (di,dj) in neighbor_deltas:

            (n_i, n_j) = (i+di, j+dj)
            if off_map(n_i, n_j):
                # This "neighbor" doesn't exist.
                continue
            a = altitude_of_[n_i][n_j]
            if a < lowest_neighbor_alt:
                lowest_neighbor_alt = a
                (lowest_n_i, lowest_n_j) = (n_i, n_j)

        if lowest_neighbor_alt >= altitude_of_[i][j]:
            # this cell is a sink
            return None
        else:
            return (lowest_n_i, lowest_n_j)

    def explore_basin( start_i, start_j, basin_label ):
        # Label all cells in the same basin as cell (i,j).

        # First, find the low point of the basin.
        (i,j) = (start_i, start_j)
        while True:
            fn = flow_neighbor(i,j)
            if fn is None:
                # we have reached the low point
                (low_i,low_j) = (i,j)
                break
            (i,j) = fn

        # Then, work up/out/back from there.
        q = Queue.Queue()
        q.put( (low_i, low_j) )
        while not q.empty():
            (i,j) = q.get()

            # If this cell has already been labelled,
            # it must have been labelled with this basin.
            if basin_[i][j] is not None:
                assert basin_[i][j] == basin_label
                continue

            basin_[i][j] = basin_label

            # Find any neighbors of this cell
            # for which it is the flow-neighbor.
            for (di,dj) in neighbor_deltas:
                (n_i, n_j) = (i+di, j+dj)
                if off_map( n_i, n_j ):
                    continue
                if flow_neighbor(n_i,n_j) == (i,j):
                    q.put( (n_i,n_j) )

        assert basin_[start_i][start_j] == basin_label

    basin_label = 'a'
    for i in range(0, H):
        for j in range(0, W):
            if basin_[i][j] is None:
                explore_basin( i, j, basin_label )
                basin_label = chr(1+ord(basin_label))

    print 'Case #%d:' % case_num
    for i in range(0, H):
        for j in range(0, W):
            print basin_[i][j],
        print

    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
