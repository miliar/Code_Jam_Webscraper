from collections import defaultdict


def augment(u, bigraph, visit, match):
    for v in bigraph[u]:
        if not visit[v]:
            visit[v] = True
            if match[v] is None or augment(match[v],  bigraph, visit, match):
                match[v] = u       # chemin augmentant trouvé
                return True
    return False



def max_bipartite_matching2(bigraph):
    """Bipartie maximum matching
    :param bigraph: adjacency list, index = vertex in U,
                                    value = neighbor list in V
    :comment: U and V can have different cardinalities
    :returns: matching list, match[v] == u iff (u, v) in matching
    :complexity: `O(|V|*|E|)`
    """
    nU = len(bigraph)
    # the following line works only in Python version ≥ 2.5
    # nV = max(max(adjlist, default=-1) for adjlist in bigraph) + 1
    nV = 0
    for adjlist in bigraph:
        for v in adjlist:
            if v + 1 > nV:
                nV = v + 1
    match = [None] * nV
    for u in range(nU):
        augment(u, bigraph, [False] * nV, match)
    return match


def main(l1, l2):
    m = len(l1) + len(l2)
    if len(l1) > len(l2):
        l1, l2 = l2, l1
    l1.sort()
    l2.sort()
    f1 = l1.count(1)
    f2 = l2.count(1)
    nf1 = len(l1) - f1
    nf2 = len(l2) - f2
    nf2 -= min(nf2, f1)
    nf1 -= min(nf1, f2)
    y = f1 + f2 + max(nf1, nf2)
    k = min(nf1, nf2)
    # on doit former k couples
    l1 = l1[f1:]
    l2 = l2[f2:]
    bigraph = []
    for i in range(len(l1)):
        bigraph.append([j for j in range(len(l2)) if
                        l2[j] != l1[i]])
    ans = max_bipartite_matching2(bigraph)
    z = max(0, k - (len(ans) - ans.count(None)))
    return y, z


for t in range(int(input())):
    n, c, m = map(int, input().split())
    l1 = []
    l2 = []
    for _ in range(m):
        a, b = map(int, input().split())
        if b == 1:
            l1.append(a)
        else:
            l2.append(a)
    y, z = main(l1, l2)
    print("Case #%s: %s %s" % (t + 1, y, z))
