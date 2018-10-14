#!/usr/bin/python

def solve(Hd, Ad, Hk, Ak, B, D):
    # (Hd, Ad, Hk, Ak)
    encountered_nodes = set()
    
    Hd_0 = Hd
    # (Hd, Ad, Hk, Ak, num_moves)
    nodes = [(Hd, Ad, Hk, Ak, 0)]
    
    def potentialAdd(node):
        Hd, Ad, Hk, Ak, num_moves = node
        encountered_node = (Hd, Ad, Hk, Ak)
        if encountered_node not in encountered_nodes:
            nodes.append(node)
            encountered_nodes.add(encountered_node)
    
    while len(nodes):
        Hd, Ad, Hk, Ak, num_moves = nodes.pop(0)
        if Hk <= 0:
            return num_moves
        if Hd > 0:
            potentialAdd((Hd - Ak, Ad, Hk - Ad, Ak, num_moves + 1))
            if B > 0:
                potentialAdd((Hd - Ak, Ad + B, Hk, Ak, num_moves + 1))
            potentialAdd((Hd_0 - Ak, Ad, Hk, Ak, num_moves + 1))
            if D > 0:
                potentialAdd((Hd - (Ak - D), Ad, Hk, max(Ak - D, 0), num_moves + 1))

    return 'IMPOSSIBLE'


T = int(raw_input())
for t in range(T):
    Hd, Ad, Hk, Ak, B, D = map(int, raw_input().split())
        
    result = solve(Hd, Ad, Hk, Ak, B, D)
    print "Case #%d: %s" % (t + 1, result)
    