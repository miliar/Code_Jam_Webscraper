#!/usr/bin/env python3
"""Google Code Jam Submission
Problem: 2011 Round 2 Problem D
Author: Matt Giuca
"""

import sys

### Input parsing ###

def parse_input(infile):
    """Consume input for a single case from infile.
    Return or yield a data structure describing the input.
    """
    P, W = tuple(map(int, infile.readline().split()))
    wormholes = [tuple(map(int, wh.split(",")))
                 for wh in infile.readline().split()]
    assert len(wormholes) == W
    return P, wormholes

### Algorithm ###

class Vertex:
    def __init__(self, index, dist=None, prevs=None):
        self.index = index
        self.dist = dist
        self.prevs = prevs or set() # set of Vertex (with equal weight)
        self.edges = []
    def __repr__(self):
        return "Vertex({0}, {1}, <{2}>)".format(self.index, self.dist,
            ', '.join([str(p.index) for p in self.prevs]))

def extract_min_dist(Q):
    assert len(Q) > 0
    min_dist_node = Q[0]
    min_dist_index = 0
    min_dist = Q[0].dist
    for i, v in enumerate(Q):
        if v.dist is not None and (min_dist is None or v.dist < min_dist):
            min_dist_node = v
            min_dist_index = i
            min_dist = v.dist
    del Q[min_dist_index]
    return min_dist_node

def followback(seq, cur):
    if len(cur.prevs) == 0:
        yield seq
        return
    seq = [cur] + seq
    for cur in cur.prevs:
        for s in followback(seq, cur):
            yield s

def dijkstra(num_vertices, edges, source=0):
    # http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    verts = [Vertex(i) for i in range(num_vertices)]
    for x,y in edges:
        verts[x].edges.append(verts[y])
        verts[y].edges.append(verts[x])
    start = verts[0]
    target_node = verts[1]
    verts[source].dist = 0
    Q = verts
    while len(Q) > 0:
        # Find element of Q with shortest dist
        u = extract_min_dist(Q)
        if u.dist is None:
            break
        for v in u.edges:
            alt = u.dist + 1
            if v.dist is None or alt < v.dist:
                v.dist = alt
                v.prevs = {u}
            elif alt == v.dist:
                v.prevs.add(u)
    seq = []
    cur = target_node
    #while len(cur.prevs) > 0:
    #    seq.append(cur)
    #    cur = list(cur.prevs)[0]    # XXX nondet
    for s in followback(seq, cur):
        s = [start] + s
        yield s

def calc_threatens(seq):
    """seq: List of planets conquered, INCLUDING home but NOT INCLUDING ai
    home."""
    owned = set()           # ints
    threatened = set()      # ints, superset of owned
    for v in seq:
        owned.add(v.index)
        threatened.add(v.index)
        for e in v.edges:
            threatened.add(e.index)
    return len(threatened) - len(owned)

def handle_case(data):
    """Given the data structure returned by parse_input, return the answer as
    a string or stringable value.
    If parse_input is a generator, should manually call list() on data.
    """
    P, wormholes = data
    seq = list(dijkstra(P, wormholes))
    best_threaten_seq = None
    best_threaten = None
    for s in seq:
        s.pop()
        t = calc_threatens(s)
        if best_threaten is None or t > best_threaten:
            best_threaten = t
            best_threaten_seq = s
    seq = best_threaten_seq
    #print([v.index for v in seq])
    return len(seq)-1, calc_threatens(seq)

### Top-level ###

def main():
    numcases = int(sys.stdin.readline())
    for casenum in range(numcases):
        data = parse_input(sys.stdin)
        conq, threat = handle_case(data)
        print("Case #{0}: {1} {2}".format(casenum+1, conq, threat))

if __name__ == "__main__":
    sys.exit(main())
