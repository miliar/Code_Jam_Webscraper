#!/usr/bin/env python2
def to_diag((r, c)):
    return r + c, r - c
def from_diag((r_plus_c, r_minus_c)):
    ret = (r_plus_c + r_minus_c) / 2, (r_plus_c - r_minus_c) / 2
    assert to_diag(ret) == (r_plus_c, r_minus_c)
    return ret
def complete_matching(edges, matching):
    assert len(matching) == len(set(matching))
    assert len(edges) == len(set(edges))
    matching = set(matching)
    edges = set(edges)
    matched_l = {l for (l, r) in matching}
    matched_r = {r for (l, r) in matching}
    unmatched_edges = {(l, r) for (l, r) in edges if l not in matched_l and r not in matched_r}
    # NetworkX 1.11:
    # Compute a bipartite matching
    # https://networkx.readthedocs.io/en/stable/download.html
    # Packaged for Fedora as: python2-networkx-core-1.11-3.fc25.noarch
    import networkx as nx
    B = nx.Graph()
    U = list(set([('L', l) for (l, r) in unmatched_edges]))
    V = list(set([('R', r) for (l, r) in unmatched_edges]))
    E = [(('L', l), ('R', r)) for (l, r) in unmatched_edges]
    #print 'U', U
    #print 'V', V
    #print 'E', E
    B.add_nodes_from(U, bipartite=0)
    B.add_nodes_from(V, bipartite=1)
    B.add_edges_from(E)
    #print 'B', repr(B)
    match = nx.bipartite.maximum_matching(B)
    #print 'match', match
    l_match = {l: r for ((L, l), (R, r)) in match.iteritems() if L == 'L' and R == 'R'}
    assert len(match) == 2 * len(l_match)
    assert not (set(l_match.iteritems()) & set(matching))
    #print 'return', list(l_match.iteritems())
    return list(l_match.iteritems())
#assert complete_matching([(1, 1), (1, 2), (2, 1), (2, 2), (2, 3)], [(2, 1)]) == [(1, 2)]
for t in xrange(1, 1 + int(raw_input())):
    print 'Case #%d:' % t,
    n, m = map(int, raw_input().split())
    aa = []
    aa_edges = [(r, c) for r in xrange(1, 1 + n) for c in xrange(1, 1 + n)]
    diag = []
    diag_edges = map(to_diag, aa_edges)
    for _ in xrange(m):
        type_, r, c = raw_input().split()
        r = int(r)
        c = int(c)
        if type_ in 'xo':
            aa.append((r, c))
        if type_ in '+o':
            diag.append((r + c, r - c))
    #print 'aa', aa_edges, aa
    extra_aa = complete_matching(aa_edges, aa)
    extra_diag = complete_matching(diag_edges, diag)
    assert not (set(extra_aa) & set(aa))
    assert not (set(extra_diag) & set(diag))
    all_aa = extra_aa + aa
    all_diag = extra_diag + diag
    all_extra = list(set(extra_aa) | set(map(from_diag, extra_diag)))
    assert len(all_aa) == n
    print len(all_aa) + len(all_diag), len(all_extra)
    for r, c in all_extra:
        is_aa = (r, c) in all_aa
        is_diag = to_diag((r, c)) in all_diag
        if is_diag:
            if is_aa:
                type_ = 'o'
            else:
                type_ = '+'
        else:
            assert is_aa
            type_ = 'x'
        print type_, r, c
